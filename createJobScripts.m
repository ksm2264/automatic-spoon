close all
clearvars

fid = fopen('berk_jobs_batch_1.sh','w');

fprintf(fid,'#!/bin/bash \n \n');

clipList = dir('/media/karl/DATA/berk_subclips/*.mp4');

for idx = 1:50
    clip_name = split(clipList(idx).name,'.');
    clip_name = clip_name{1};
    
    fprintf(fid,['cp base_js jobscripts/' clip_name '_jobscript \n']);
    fprintf(fid,['sed -i ''s/s3_0/' clip_name '/g'' jobscripts/' clip_name '_jobscript \n']);
    fprintf(fid,['sbatch jobscripts/' clip_name '_jobscript \n']);
    
end

fid = fopen('berk_jobs_batch_2.sh','w');

fprintf(fid,'#!/bin/bash \n \n');


for idx = 51:length(clipList)
    clip_name = split(clipList(idx).name,'.');
    clip_name = clip_name{1};
    
    fprintf(fid,['cp base_js jobscripts/' clip_name '_jobscript \n']);
    fprintf(fid,['sed -i ''s/s3_0/' clip_name '/g'' jobscripts/' clip_name '_jobscript \n']);
    fprintf(fid,['sbatch jobscripts/' clip_name '_jobscript \n']);
    
end

fid = fopen('berk_jobs_batch_prep_vid_folders.sh','w');

fprintf(fid,'#!/bin/bash \n \n');

for idx = 1:length(clipList)
    
    clip_name = split(clipList(idx).name,'.');
    clip_name = clip_name{1};
    fprintf(fid,['mkdir ' clip_name '\n']);
    
end


fid = fopen('move_vids.sh','w');

fprintf(fid,'#!/bin/bash \n \n');

for idx = 1:length(clipList)
    
    clip_name = split(clipList(idx).name,'.');
    clip_name = clip_name{1};
    fprintf(fid,['mv ' clip_name '.mp4 ' clip_name '/' '\n']);
    
end


fid = fopen('split_vids.sh','w');

fprintf(fid,'#!/bin/bash \n \n');

for idx = 1:length(clipList)
    
    clip_name = split(clipList(idx).name,'.');
    clip_name = clip_name{1};
    fprintf(fid,['ffmpeg -i ' clip_name '/' clip_name '.mp4 ' clip_name '/%%00d.png \n']);
    
end

fid = fopen('p3_berk_jobs_batch_1.sh','w');

fprintf(fid,'#!/bin/bash \n \n');

for idx = 1:50
    clip_name = split(clipList(idx).name,'.');
    clip_name = clip_name{1};
    
    fprintf(fid,['cp norm_js jobscripts/' clip_name '_jobscript \n']);
    fprintf(fid,['sed -i ''s/s3_0/' clip_name '/g'' jobscripts/' clip_name '_jobscript \n']);
    fprintf(fid,['sbatch jobscripts/' clip_name '_jobscript \n']);
    
end

fid = fopen('p3_berk_jobs_batch_2.sh','w');

fprintf(fid,'#!/bin/bash \n \n');


for idx = 51:length(clipList)
    clip_name = split(clipList(idx).name,'.');
    clip_name = clip_name{1};
    
    fprintf(fid,['cp norm_js jobscripts/' clip_name '_jobscript \n']);
    fprintf(fid,['sed -i ''s/s3_0/' clip_name '/g'' jobscripts/' clip_name '_jobscript \n']);
    fprintf(fid,['sbatch jobscripts/' clip_name '_jobscript \n']);
    
end