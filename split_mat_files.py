#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:12:52 2021

@author: karl
"""


import pandas as pd
import scipy.io as sio
import numpy as np

tab = pd.read_csv('timestamps_seconds.csv').dropna()

base_mat_path = '/media/karl/DATA/bigMats/'

target_mat_folder = '/media/karl/DATA/berk_submats/'

for subj in tab['Subject']:
    
    big_mat_str = base_mat_path + subj +'.mat'
    
    print(big_mat_str)
    
    
    bigMat = sio.loadmat(big_mat_str,squeeze_me=True,struct_as_record=False)
    
    wfi = bigMat['rEye'].index
    
    wfi = wfi-1
    
    steps = bigMat['steps_HS_TO_StanceLeg_XYZ']
    step_idx = np.array(steps[:,:2]).astype(int)
    steps[:,:2] = wfi[step_idx]
    steps = steps[:,:3]
    
    markerNames = bigMat['shadowMarkerNames']
    shadow = bigMat['shadow_fr_mar_dim']
    
    rGazeXYZ = bigMat['rGazeXYZ'] 
    lGazeXYZ = bigMat['lGazeXYZ']
    
    rEyeCen = bigMat['rEyeballCenterXYZ'] 
    lEyeCen = bigMat['lEyeballCenterXYZ']
    
    norm_pos_x = bigMat['gaze'].norm_pos_x
    norm_pos_y = bigMat['gaze'].norm_pos_y
    
    headMat = bigMat['headRotMat_row_col_fr']
    
    wfi = list(wfi)
    
    for walk in range(1,5):
        
        startFr=tab.loc[tab['Subject']==subj]['Walk ' +str(walk) + ' Start'].values[0]
        endFr = tab.loc[tab['Subject']==subj]['Walk ' +str(walk) + ' End'].values[0]
        
        midFr = (startFr + endFr)/2
        
        startFr = startFr*30
        endFr = endFr*30
        midFr = midFr*30
        
        startDex = wfi.index(int(startFr))
        midDex = wfi.index(int(midFr))
        endDex = wfi.index(int(endFr))
        
        #%% p1 walk
        
        p1_walk = {}
        
        p1_dexer = np.arange(startDex,midDex+1)
        
        this_wfi = np.array(wfi[startDex:midDex+1])
        p1_walk['wfi'] = this_wfi
        p1_walk['shadow'] = shadow[p1_dexer]
        p1_walk['rEyeCen'] = rEyeCen[p1_dexer]
        p1_walk['lEyeCen'] = lEyeCen[p1_dexer]
        p1_walk['rGazeXYZ'] = rGazeXYZ[p1_dexer]
        p1_walk['lGazeXYZ'] = lGazeXYZ[p1_dexer]
        p1_walk['norm_pos_x'] = norm_pos_x[p1_dexer]
        p1_walk['norm_pos_y'] = norm_pos_y[p1_dexer]
        p1_walk['headMat'] = headMat[:,:,p1_dexer]
        p1_walk['markerNames'] = markerNames
        
         #%% p2 walk
        
        p2_walk = {}
        
        p2_dexer = np.arange(midDex,endDex+1)
        
        this_wfi = np.array(wfi[midDex:endDex+1])
        p2_walk['wfi'] = this_wfi
        p2_walk['shadow'] = shadow[p2_dexer]
        p2_walk['rEyeCen'] = rEyeCen[p2_dexer]
        p2_walk['lEyeCen'] = lEyeCen[p2_dexer]
        p2_walk['rGazeXYZ'] = rGazeXYZ[p2_dexer]
        p2_walk['lGazeXYZ'] = lGazeXYZ[p2_dexer]
        p2_walk['norm_pos_x'] = norm_pos_x[p2_dexer]
        p2_walk['norm_pos_y'] = norm_pos_y[p2_dexer]
        p2_walk['headMat'] = headMat[:,:,p2_dexer]
        p2_walk['markerNames'] = markerNames
        
        #%% save
        
        target_mat_str_p1 = target_mat_folder + subj + '_' + str(walk)+'_p1.mat'
        target_mat_str_p2 = target_mat_folder + subj + '_' + str(walk)+'_p2.mat'

        
        sio.savemat(target_mat_str_p1,p1_walk)
        sio.savemat(target_mat_str_p2,p2_walk)