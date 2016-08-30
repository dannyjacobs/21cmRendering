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
intro = False
i = 0
animation_end_frame = 1300
raw_file_counter = 0

#print('the last argument is:'+str(sys.argv))

#--- make sure proper textures are displayed
bpy.data.materials['Material'].use_textures[0] = False
bpy.data.materials['Material'].use_textures[1] = False
bpy.data.materials['Material'].use_textures[2] = True

for filepath in sorted(file_list, reverse=True):
    if intro:
        #--- Render time evolution
        bpy.data.scenes["Scene"].frame_start = 0
        bpy.data.scenes["Scene"].frame_end = i-1
        bpy.data.textures["hydrogen_pink"].voxel_data.filepath = filepath

        #--- Start animating ---#
        print("rendered frame (a): {:}, file: {:}".format(i, filepath))
        bpy.ops.render.render(animation=True)
        intro = False
        #i = i+frame_count+1
        #raw_file_counter += 1
    else:
        if (raw_file_counter < animate_length-101): #trim the last 100 files off
            bpy.data.scenes["Scene"].frame_start = i
            bpy.data.scenes["Scene"].frame_end = i+frame_count+1
            bpy.data.textures["hydrogen_pink"].voxel_data.filepath = filepath
            print('rendered frame (b): {:}, file: {:}'.format(i, filepath))
            bpy.ops.render.render(animation=True)
            i = i+frame_count+1
            raw_file_counter += 1
        else:
            bpy.data.scenes["Scene"].frame_start = i
            bpy.data.scenes["Scene"].frame_end = animation_end_frame
            bpy.data.textures["hydrogen_pink"].voxel_data.filepath = filepath
            print('rendered frame (c): {:}, file: {:}'.format(i, filepath))
            bpy.ops.render.render(animation=True)
            #trim the last 100 files off
            sys.exit()
