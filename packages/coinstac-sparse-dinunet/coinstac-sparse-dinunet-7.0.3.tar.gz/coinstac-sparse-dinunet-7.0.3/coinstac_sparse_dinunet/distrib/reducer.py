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
        #self.my_logger.write("\n The number of sites data is "+ str(len(sites_data)))
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
        # self.cache["timelogsDirectory"] = _os.path.join(
        #     self.state['transferDirectory']
        # )

        # _os.makedirs(self.cache['timelogsDirectory'], exist_ok=True)
        #self.timelogger = open(self.cache['timelogsDirectory']+"/time_logs_remote.json", 'w+')
        self.timelogs={}
        # self.my_logger = open(self.cache['log_dir'] + _os.sep + f"locallogs.json", 'a')

    # def reduce(self):
    #     """ Average each sites gradients and pass it to all sites. """
    #     out = {
    #         'avg_grads_file': _conf.avg_grads_file
    #     }
    #     _tu.save_arrays(
    #         self.state['transferDirectory'] + _os.sep + out['avg_grads_file'],
    #         _np.array(self._average('grads_file'), dtype=object)
    #     )

    #     out['update'] = True
    #     return out

    def reduce(self):
        """ Average each sites gradients and pass it to all sites. """
        out = {
            'avg_grads_file': _conf.avg_grads_file
        }
        #Log time to load all the gradients time
        allremoteelapsed=0
        start = timer()
        #Log time for gather and save
        _tu.save_arrays_reducer(
            self.state['transferDirectory'] + _os.sep + out['avg_grads_file'],
            _np.array(self._average('grads_file'), dtype=object)
        )
        end = timer()
        allremoteelapsed = allremoteelapsed + (end - start)
        self.timelogs["remote_gather_and_avg_write"] = allremoteelapsed

        self.cache[Key.TIME_LOGS_REMOTE] = self.timelogs
        # _utils.save_scores(
        #     self.cache,
        #     self.state['outputDirectory'] + _os.sep + self.cache['task_id'],
        #     file_keys=[Key.TIME_LOGS_REMOTE]
        # )

        #_utils.save_time_logs_remote(self.timelogs,)
        with open(self.state['outputDirectory'] + _os.sep + self.cache['task_id'] + '/timelogsremote.json', 'a+') as file:
                file.write("\n" + str(self.timelogs))
        
        _shutil.copy(self.state['outputDirectory'] + _os.sep + self.cache['task_id'] + '/timelogsremote.json', self.state['transferDirectory'] + _os.sep + "timelogsremotetransfer.json")
    
        # with open(self.state['transferDirectory'] + '/timelogsremotenew.json', 'a+') as file:
        #         file.write("\n" + str(self.timelogs))

        # out['results_zip'] = f"{self.cache['task_id']}_{self.cache['agg_engine']}_"
        # out['results_zip'] += '_'.join(str(_datetime.datetime.now()).split(' '))

        # _shutil.make_archive(
        #     f"{self.state['transferDirectory']}{_os.sep}{out['results_zip']}",
        #     'zip',
        #     self.state['outputDirectory'] + _os.sep + self.cache['task_id']
        # )
        #return out
        # with open(self.state['transferDirectory'] + _os.sep  +'time_logs_remote.json', 'a+') as file:
        #     file.write("\n" + str(self.timelogs))
        # _utils.save_time_logs_remote(self.timelogs,self.state['transferDirectory'])
        #_shutil.copy(self.cache['timelogsDirectory'] + '/time_logs_remote.json', f"{self.state['outputDirectory']}{_sep}timelogsremote.json")
        #_shutil.copy(self.cache['timelogsDirectory'] + '/time_logs_remote.json', f"{self.state['transferDirectory']}{_sep}timelogsremote.json")
                #Write into logger
  

        # _tu.save_arrays_reducer(
        #     self.state['outputDirectory'] + _os.sep + 'reduceravggrads.npy',
        #     _np.array(self._average('grads_file'), dtype=object)
        # )
        out['update'] = True
        return out
