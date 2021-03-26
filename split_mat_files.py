#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 12:12:52 2021

@author: karl
"""


import pandas as pd
import scipy.io as sio

tab = pd.read_csv('timestamps_seconds.csv').dropna()

base_vid_path = '/media/karl/DATA/vid/'

target_mat_folder = '/media/karl/DATA/berk_submats/'

for subj in tab['Subject']:
    
    raw_vid_str = base_vid_path + subj +'.mp4'
    
    print(raw_vid_str)
    
    for walk in range(1,5):
        
        startFr=tab.loc[tab['Subject']==subj]['Walk ' +str(walk) + ' Start'].values[0]
        endFr = tab.loc[tab['Subject']==subj]['Walk ' +str(walk) + ' End'].values[0]
        
        midFr = (startFr + endFr)/2
        