#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:35:15 2021

@author: karl
"""

import glob
import numpy as np

fileList = glob.glob('/media/karl/DATA/berk_subclips/*.mp4')


gpu_dict = {}
all_list = []

for file in fileList:
    
    this_name = file.split('/')[-1].split('.')[0]
    
    gpu_dict[this_name] = False
    all_list.append(this_name)
    
np.save('gpu_dict_berk.npy',gpu_dict)
np.save('all_list_berk.npy',all_list)