#Blender command line scripting attempt
#
#--- Changelog ---
#-----------------
# for use with
#--------------------------------------

import bpy
#import numpy as np
import sys
import os
import glob
import optparse

#number of frames per timestep
frame_count = 0

###
o = optparse.OptionParser()
o.set_description('Suck a bag of dicks')

o.add_option('--glob_pat',type=str,
    help='location of .raw files for glob')

opts,args = o.parse_args(sys.argv[5:])
###

file_list = glob.glob(opts.glob_pat)
animate_length = len(file_list)
skip_length = 0
files = sys.argv[5:]

#initialize counters
rot_begin = 0. #frame to start animation on
rot_end = 705. #frame to stop fade on
animation_end_frame = 705
i = 0
raw_file_counter = 0

#print('the last argument is:'+str(sys.argv))

#--- make sure proper textures are displayed
bpy.data.materials['Material'].use_textures[0] = True
bpy.data.materials['Material'].use_textures[1] = False

for filepath in sorted(file_list):
    if (raw_file_counter < animate_length-1):
        #--- Render time evolution
        bpy.data.scenes["Scene"].frame_start = i
        bpy.data.scenes["Scene"].frame_end = i+frame_count
        bpy.data.textures["hydrogen"].voxel_data.filepath = filepath

        #--- Start animating ---#
        #print("rendered frame (a): {:}, file: {:}".format(i, filepath))
        bpy.ops.render.render(animation=True)
        i = i+frame_count+1
        raw_file_counter += 1
    else:
        bpy.data.scenes["Scene"].frame_start = i
        bpy.data.scenes["Scene"].frame_end = animation_end_frame
        #print('rendered frame (b): {:}, file: {:}'.format(i, filepath))
        bpy.ops.render.render(animation=True)
