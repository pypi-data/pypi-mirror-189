"""
@author: Bishal Thapaliya
@email: bthapaliya16@gmail.com
"""

from os import sep as _sep
import torch as _torch
import os as _os
from coinstac_sparse_dinunet import config as _conf
from coinstac_sparse_dinunet.utils import tensorutils as _tu
import numpy as _np
import coinstac_sparse_dinunet.utils as _utils
import torch.nn as nn
from timeit import default_timer as timer

class COINNLearner:
    def __init__(self, trainer=None, mp_pool=None, **kw):
        self.cache = trainer.cache
        self.input = trainer.input
        self.state = trainer.state
        self.trainer = trainer
        self.global_modes = self.input.get('global_modes', {})
        self.pool = mp_pool
        self.dtype = f"float{self.cache['precision_bits']}"
        self.device = trainer.device["gpu"]
        self.cache['log_dir'] = _os.path.join(
            self.state['outputDirectory'],
            self.cache['task_id'],
            f"fold_0"
        )
        _os.makedirs(self.cache['log_dir'], exist_ok=True)
        # self.cache["timelogsDirectory"] = _os.path.join(
        #     self.state['transferDirectory']
        # ) 
        self.timelogs={}
        #_os.makedirs(self.cache['timelogsDirectory'], exist_ok=True)


    
    def get_model_sps(self, model):
        nonzero = total = 0
        for name, param in model.named_parameters():
            if 'mask' not in name:
                tensor = param.detach().clone()
                # nz_count.append(torch.count_nonzero(tensor))
                nz_count = _torch.count_nonzero(tensor).item()
                total_params = tensor.numel()
                nonzero += nz_count
                total += total_params
        
        tensor = None
        # print(f"TOTAL: {total}")
        abs_sps = 100 * (total-nonzero) / total
        return abs_sps
    
    def applyMasksInStep(self) -> dict:
        out = {}
        masks = _tu.load_masks(self.state['baseDirectory'] + _sep + _conf.masks_file)
        #grads = _tu.load_arrays(self.state['baseDirectory'] + _sep + self.input['avg_grads_file'])
        first_model = list(self.trainer.nn.keys())[0]
        self.trainer.nn[first_model]= self.trainer.unregister_mask(self.trainer.nn[first_model])
        self.trainer.apply_mask_to_model(self.trainer.nn[first_model], masks)
        self.trainer.register_pre_hook_mask(masks)
        #self.trainer.nn[first_model]= self.trainer.apply_mask_to_model(self.trainer.nn[first_model], grads)
        return out


    def step(self) -> dict:
        out = {}
        #grads = _tu.load_arrays_learner(self.state['baseDirectory'] + _sep + self.input['masks_file'])
        grads = _tu.load_arrays(self.state['baseDirectory'] + _sep + self.input['avg_grads_file'])
        grad_index = 0
        first_model = list(self.trainer.nn.keys())[0]
        for i, param in enumerate(self.trainer.nn[first_model].named_parameters()):
            if 'mask' not in param[0]:
                param[1].grad = _torch.tensor(grads[grad_index], dtype=_torch.float32).to(self.device)
                grad_index += 1

        first_optim = list(self.trainer.optimizer.keys())[0]
        self.trainer.optimizer[first_optim].step()
        return out

    def backward(self):
        out = {}
        first_model = list(self.trainer.nn.keys())[0]
        first_optim = list(self.trainer.optimizer.keys())[0]

        self.trainer.nn[first_model].train()
        self.trainer.optimizer[first_optim].zero_grad()
        its = []
        for _ in range(self.cache['local_iterations']):
            batch, nxt_iter_out = self.trainer.data_handle.next_iter()
            #Log forward pass time
            forwardelapsed=0
            start = timer()
            it = self.trainer.iteration(batch)
            end = timer()
            forwardelapsed = forwardelapsed + (end - start)
            self.timelogs["forward_pass_per_batch"] = forwardelapsed
            it['loss'].backward()
            its.append(it)
            out.update(**nxt_iter_out)
        return self.trainer.reduce_iteration(its), out

    # def to_reduce(self):
    #     it, out = self.backward()
    #     first_model = list(self.trainer.nn.keys())[0]
    #     out['grads_file'] = _conf.grads_file
    #     grads = _tu.extract_grads(self.trainer.nn[first_model], dtype=self.dtype)
    #     _tu.save_arrays(
    #         self.state['transferDirectory'] + _sep + out['grads_file'],
    #         _np.array(grads, dtype=object)
    #     )
    #     out['reduce'] = True
    #     return it, out

    def generateGradsForMasks(self):
        #it, out = self.backward()
        out={}
        first_model = list(self.trainer.nn.keys())[0]
        out['grads_file'] = _conf.grads_file
        #Extract grads
        weights_array=[]
        for layer in self.trainer.nn[first_model].modules():
            if isinstance(layer, nn.Conv2d) or isinstance(layer, nn.Linear):
                    #grads.append(_torch.abs(layer.weight_mask.grad))
                    weights_array.append(caste_ndarray(layer.weight.data.detach().cpu().numpy(), self.dtype))

        # _tu.save_arrays_reducer(
        #     self.state['transferDirectory'] + _sep + "weights_to_send.npy",
        #     _np.array((weights_array), dtype=object)
        # )
        # for layer in self.trainer.nn[first_model].modules():
        #     if isinstance(layer, nn.Conv2d) or isinstance(layer, nn.Linear):
        #         grads.append(caste_ndarray(layer.weight.grad.detach().cpu().numpy(), self.dtype))

        #Get model sparsity 
        model_sparsity = self.get_model_sps(self.trainer.nn[first_model])
        finalgrads = []
        for param_grads in weights_array:
            non_zero_grad_indices = _np.array(_np.nonzero(param_grads))
            values_nonzero = param_grads[_np.nonzero(param_grads)]
            sps_grads = _torch.sparse_coo_tensor(non_zero_grad_indices, values_nonzero,(param_grads.shape))
            finalgrads.append(sps_grads)

        _tu.save_arrays(
            self.state['transferDirectory'] + _sep + out['grads_file'],
            finalgrads
        )
        # with open(self.state['outputDirectory'] + _os.sep + self.cache['task_id'] + '/inspect_logs.json', 'a+') as file:
        #      file.write("\n Inside reduce_for_masks of learner. Generating grads for masking.. ")
        
        out['reduce_for_masks'] = True
        return out


    def to_reduce(self):
        #Log backward prop time
        elapsed=0
        start = timer()
        it, out = self.backward()
        end = timer()
        elapsed = elapsed + (end - start)
        self.timelogs["backward_prop_time"] = elapsed

        first_model = list(self.trainer.nn.keys())[0]
        out['grads_file'] = _conf.grads_file

        # with open(self.state['outputDirectory'] + _os.sep + self.cache['task_id'] + '/inspect_logs.json', 'a+') as file:
        #      file.write("\n Inside reduce of learner. Generating grads for optimization. ")

        #Extract grads
        grads = _tu.extract_grads(self.trainer.nn[first_model], dtype=self.dtype)
        # with open(self.state['outputDirectory'] + _os.sep + self.cache['task_id'] + '/inspect_logs.json', 'a+') as file:
        #     file.write("\n Inside reduce for  gradients. ")
        
        #Get model sparsity 
        model_sparsity = self.get_model_sps(self.trainer.nn[first_model])
        finalgrads = []
        for param_grads in grads:
            non_zero_grad_indices = _np.array(_np.nonzero(param_grads))
            values_nonzero = param_grads[_np.nonzero(param_grads)]
            sps_grads = _torch.sparse_coo_tensor(non_zero_grad_indices, values_nonzero,(param_grads.shape))
            finalgrads.append(sps_grads)

        localelapsed=0
        start = timer()
        _tu.save_arrays(
            self.state['transferDirectory'] + _sep + out['grads_file'],
            finalgrads
        )
        end = timer()
        localelapsed = localelapsed + (end - start)

        self.timelogs["local_grads_save_time"] = localelapsed
        self.timelogs["model_sparsity"] = str(model_sparsity)

        #Write into logger
        with open(self.state['outputDirectory'] + _os.sep + self.cache['task_id'] + '/time_logs.json', 'a+') as file:
            file.write("\n" + str(self.timelogs))
        
        out['reduce'] = True
        return it, out

def caste_ndarray(a, dtype='float32'):
    return a.astype(dtype)