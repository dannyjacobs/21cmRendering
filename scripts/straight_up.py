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

#initialize counters
rot_begin = 0. #frame to start animation on
rot_end = 300. #frame to stop fade on
animation_end_frame = 300
i = 0
raw_file_counter = 0

#print('the last argument is:'+str(sys.argv))

#--- make sure proper textures are displayed
#bpy.data.materials['Material'].use_textures[2] = True
#bpy.data.materials['Material'].use_textures[0] = False

for filepath in sorted(file_list, reverse=True):
    bpy.data.textures["hydrogen_pink"].voxel_data.filepath = filepath
    bpy.ops.render.render(animation=True)
