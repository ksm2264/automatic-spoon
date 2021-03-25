#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 18:13:28 2021

@author: karl
"""

import numpy as np
import pandas as pd
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

tab = pd.read_csv('timestamps_seconds.csv').dropna()

base_vid_path = '/media/karl/DATA/vid/'

for subj in tab['Subject']:
    
    raw_vid_str = base_vid_path + subj +'.mp4'
    
    print(raw_vid_str)