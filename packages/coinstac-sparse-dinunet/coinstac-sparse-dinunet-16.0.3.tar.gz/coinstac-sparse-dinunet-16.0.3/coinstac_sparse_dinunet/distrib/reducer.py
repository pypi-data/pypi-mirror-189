"""
@author: Bishal Thapaliya
@email: bthapaliya16@gmail.com
"""

import os as _os
from functools import partial as _partial
import datetime as _datetime
import numpy as _np
import shutil as _shutil
import sys
import time as _time
import traceback as _tback
from os import sep as _sep
import coinstac_sparse_dinunet.config as _conf
from coinstac_sparse_dinunet.config.keys import Key
import coinstac_sparse_dinunet.utils.tensorutils as _tu
import torch as _torch
from timeit import default_timer as timer
import coinstac_sparse_dinunet.utils as _utils

def _multi_load(file_key, state, site, site_vars):
    grads_file = state['baseDirectory'] + _os.sep + site + _os.sep + site_vars[file_key]
    return _tu.load_arrays(grads_file)


class COINNReducer:

    def _load(self, file_key):
        return list(
            self.pool.starmap(
                _partial(_multi_load, file_key, self.state), self.input.items()
            )
        )
    

    def _average(self, file_key):
        #Log time to load all the gradients time
        remoteelapsed=0
        start = timer()
        sites_data = self._load(file_key)
        end = timer()
        remoteelapsed = remoteelapsed + (end - start)
        self.timelogs["remote_load_all_grads"] = remoteelapsed

        
        gpu_data = []
        for data in list(zip(*sites_data)):
            avg = _torch.from_numpy(_np.array(data)).to(self.device, non_blocking=True).mean(0)
            gpu_data.append(avg)

        return [data.cpu().numpy().astype(self.dtype) for data in gpu_data]

    def __init__(self, trainer, mp_pool, **kw):
        self.cache = trainer.cache
        self.input = trainer.input
        self.state = trainer.state
        self.trainer = trainer
        self.pool = mp_pool
        self.dtype = f"float{self.cache['precision_bits']}"
        self.device = trainer.device['gpu']
        self.cache['log_dir'] = _os.path.join(
            self.state['outputDirectory'],
            self.cache['task_id'],
            f"fold_0"
        )
       
        _os.makedirs(self.cache['log_dir'], exist_ok=True)
        self.timelogs={}
        #self.my_logger = open(self.cache['log_dir'] + _os.sep + f"locallogs.json", 'a+')
        #self.my_logger.write("\n ******************************************************************")

    def reduce(self):
        """ Average each sites gradients and pass it to all sites. """
        out = {
            'avg_grads_file': _conf.avg_grads_file
        
        }
        # with open(self.state['outputDirectory'] + _os.sep + self.cache['task_id'] + '/inspect_remote_logs.json', 'a+') as file:
        #      file.write("\n Inside reduce of reducer. Averaging grads for optimization.. ")

        average_grads = self._average('grads_file')
        allremoteelapsed=0
        start = timer()

        #Convert average_grads to sparse matrix for transmission
        finalgrads = []
        for param_grads in average_grads:
            non_zero_grad_indices = _np.array(_np.nonzero(param_grads))
            values_nonzero = param_grads[_np.nonzero(param_grads)]
            sps_grads = _torch.sparse_coo_tensor(non_zero_grad_indices, values_nonzero,(param_grads.shape))
            finalgrads.append(sps_grads)

        #Log time for gather and save
        _tu.save_arrays(
            self.state['transferDirectory'] + _os.sep + out['avg_grads_file'],
            finalgrads
        )
        end = timer()
        allremoteelapsed = allremoteelapsed + (end - start)
        self.timelogs["remote_gather_and_avg_write"] = allremoteelapsed

        with open(self.state['outputDirectory'] + _os.sep + self.cache['task_id'] + '/timelogsremote.json', 'a+') as file:
                file.write("\n" + str(self.timelogs))
        
        _shutil.copy(self.state['outputDirectory'] + _os.sep + self.cache['task_id'] + '/timelogsremote.json', self.state['transferDirectory'] + _os.sep + "timelogsremotetransfer.json")

        out['update'] = True
        return out

    def reduceForMasks(self):
        
        """ Average each sites gradients and pass it to all sites. """
        out = {
            'masks_file': _conf.masks_file
        
        }
        # self.my_logger.write("\n *************************************************")
        average_grads = self._average('grads_file')

        # _tu.save_arrays_reducer(
        #     self.state['transferDirectory'] + _os.sep + 'averaged_file_check.npy',
        #     _np.array((average_grads), dtype=object)
        # )
        # with open(self.state['outputDirectory'] + _os.sep + self.cache['task_id'] + '/inspect_remote_logs.json', 'a+') as file:
        #      file.write("\n Inside reduce of reducer. Averaging grads for generating masks.. ")
             
        #Gather masks 
        keep_masks = self.get_mask_from_grads(average_grads, 0.1)
        
        # #Convert masks to sparse matrix for transmission
        # sparsemask = []
        # for param_grads in average_grads:
        #     non_zero_grad_indices = _np.array(_np.nonzero(param_grads))
        #     values_nonzero = param_grads[_np.nonzero(param_grads)]
        #     sps_grads = _torch.sparse_coo_tensor(non_zero_grad_indices, values_nonzero,(param_grads.shape))
        #     sparsemask.append(sps_grads)

        #Log time for gather and save
        _tu.save_arrays(
            self.state['transferDirectory'] + _os.sep + out['masks_file'],
            keep_masks
        )
        
        # _tu.save_arrays_reducer(
        #     self.state['transferDirectory'] + _os.sep + out['avg_grads_file'],
        #     _np.array((keep_masks), dtype=object)
        # )

        out['masks_update'] = True
        return out


    def get_mask_from_grads(self, averaged_weights, keep_ratio):

        grads_abs = []
        for grads in averaged_weights:
            grads_abs.append(_torch.abs(_torch.tensor(grads)))
    
        # Gather all scores in a single vector and normalise
        all_scores = _torch.cat([_torch.flatten(x) for x in grads_abs])
        norm_factor = _torch.sum(all_scores)
        all_scores.div_(norm_factor)

        num_params_to_keep = int(len(all_scores) * keep_ratio)
        threshold, _ = _torch.topk(all_scores, num_params_to_keep, sorted=True)
        acceptable_score = threshold[-1]

        keep_masks = []
        for g in grads_abs:
            #keep_masks[name] = ((values / norm_factor) >= acceptable_score).float()
            keep_masks.append(((g / norm_factor) >= acceptable_score).float())

        return keep_masks