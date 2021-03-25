#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:13:28 2021

@author: karl
"""

import pandas as pd
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

tab = pd.read_csv('timestamps_seconds.csv').dropna()

base_vid_path = '/media/karl/DATA/vid/'

target_subclip_folder = '/media/karl/DATA/berk_subclips/'

for subj in tab['Subject']:
    
    raw_vid_str = base_vid_path + subj +'.mp4'
    
    print(raw_vid_str)
    
    for walk in range(1,5):
        
        startFr=tab.loc[tab['Subject']==subj]['Walk ' +str(walk) + ' Start'].values[0]
        endFr = tab.loc[tab['Subject']==subj]['Walk ' +str(walk) + ' End'].values[0]
        
        midFr = (startFr + endFr)/2
        
        target_vid_str_p1 = target_subclip_folder + subj + '_' + str(walk)+'_p1.mp4'
        target_vid_str_p2 = target_subclip_folder + subj + '_' + str(walk)+'_p2.mp4'
        
        ffmpeg_extract_subclip(raw_vid_str,startFr,midFr,target_vid_str_p1)
        ffmpeg_extract_subclip(raw_vid_str,midFr,endFr,target_vid_str_p2)
        print(walk)