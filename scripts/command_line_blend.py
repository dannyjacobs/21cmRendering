#Blender command line scripting attempt
#
#--- Changelog ---
#-----------------
# 8/10/2016 - adjusted script to work in windows environment
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


#initialize counter

fade_begin = 0. #frame to start animation on
fade_end = 300. #frame to stop fade on
i = fade_end
raw_file_counter = 0
skip_count = 0
load = True

emission_change = 1./(fade_end - fade_begin)

print('the last argument is:'+str(sys.argv))
files = sys.argv[5:]

#--- make sure proper textures are displayed
bpy.data.materials['Material'].use_textures[0] = True
bpy.data.materials['Material'].use_textures[1] = True


file_list = glob.glob(opts.glob_pat)
animate_length = len(file_list)
skip_length = animate_length/3

for filepath in sorted(file_list):
    if (skip_count >= skip_length-1):
        #--- Render beginning fade between dark matter and hydrogen textures
        while (fade_begin < fade_end):
            if load:
                bpy.data.textures["hydrogen"].voxel_data.filepath = filepath
                bpy.data.textures["dark_matter"].voxel_data.filepath = filepath
                load = False
            bpy.data.scenes["Scene"].frame_start = int(fade_begin)
            bpy.data.scenes["Scene"].frame_end = int(fade_begin)
            bpy.data.materials['Material'].texture_slots[1].emission_color_factor -= emission_change
            bpy.data.materials['Material'].texture_slots[1].emission_factor -= emission_change
            #print('emission color: {:}'.format(bpy.data.materials['Material'].texture_slots[1].emission_color_factor))
            bpy.ops.render.render(animation=True)
            print('rendered frame: {:}, file: {:}'.format(fade_begin, filepath))
            fade_begin += 1

        #turn dark matter texture off
        bpy.data.materials['Material'].use_textures[1] = False
        #animate_length = (2/3)*animate_length
        if (raw_file_counter <= animate_length):
            #--- Render time evolution
            bpy.data.scenes["Scene"].frame_start = i
            bpy.data.scenes["Scene"].frame_end = i+frame_count
            bpy.data.textures["hydrogen"].voxel_data.filepath = filepath

            #--- Start animating ---#
            print("rendered frame: {:}, file: {:}".format(i, filepath))
            #bpy.ops.render.render(animation=True)
            i = i+frame_count+1
            raw_file_counter += 1
    else:
        print('skipped: {:}'.format(filepath))
    skip_count += 1
