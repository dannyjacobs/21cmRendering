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
i=0
fade_begin = 0. #frame to start animation on
fade_end = 300. #frame to stop fade on
raw_file_counter = 0
skip_count = 0

emission_change = 1./(fade_end - fade_begin)

print('the last argument is:'+str(sys.argv))
files = sys.argv[5:]
#print(type(files[]))
#file_list = os.listdir(files)

#--- make sure proper textures are displayed
bpy.data.materials['Material'].use_textures[0] = True
bpy.data.materials['Material'].use_textures[1] = True

#print(files)
#subdir = files
#print(glob.glob(files[0]))

glob_test = glob.glob(opts.glob_pat)

for file in sorted(glob_test):
    print("the filename is: {:}".format(file))

#for file in files:
	#print(len(files))
#	print(file)


sys.exit()

for subdir, dir, files in os.walk(files):
    for file in files:
        filepath = subdir + os.sep + file

        animate_length = len(glob.glob(subdir+os.sep+'*'))
        skip_length = animate_length/3

        #print('animate length is {:}'.format(animate_length))

        if filepath.endswith(".raw") and (skip_count >= skip_length-1):
            #print('im in a loop')
            #print(file)
            #--- Render beginning fade between dark matter and hydrogen textures
            while (fade_begin < fade_end):
                bpy.data.scenes["Scene"].frame_start = int(fade_begin)
                bpy.data.scenes["Scene"].frame_end = int(fade_begin)
                bpy.data.textures["dark_matter"].voxel_data.filepath = filepath
                bpy.data.textures["hydrogen"].voxel_data.filepath = filepath

                #bpy.ops.render.render(animation=True)
                #print("rendered frame: {:}".format(fade_begin))
                bpy.data.materials['Material'].texture_slots[1].emission_color_factor -= emission_change
                #print('emission color: {:}'.format(bpy.data.materials['Material'].texture_slots[1].emission_color_factor))
                #bpy.ops.render.render(animation=True)

                print('rendered frame: {:}, file: {:}'.format(fade_begin, file))
                fade_begin += 1
                i = fade_end

            bpy.data.materials['Material'].use_textures[1] = False
            #animate_length = (2/3)*animate_length
            if (raw_file_counter <= animate_length):
                #--- Render time evolution
                bpy.data.scenes["Scene"].frame_start = i
                bpy.data.scenes["Scene"].frame_end = i+frame_count
                #print(filepath)
                #print('hrmpf')
                bpy.data.textures["hydrogen"].voxel_data.filepath = filepath

                #--- Start animating ---#
                print("rendered frame: {:}, file: {:}".format(i, file))
                #bpy.ops.render.render(animation=True)
                i = i+frame_count+1
                #print("increase frame: {:}".format(i))
                #print(raw_file_counter)
                raw_file_counter += 1
        skip_count += 1



#for fileName in file_list[:int(len(file_list)/3.)]:
#    print('im in a loop')
#    bpy.data.scenes["Scene"].frame_start = i
#    bpy.data.scenes["Scene"].frame_end = i+frame_count
#    text_name = str(fileName)
#    print(text_name)
#    print('hrmpf')
#    bpy.data.textures["dark_matter"].voxel_data.filepath = str(files[0]+text_name)


    #for j in reversed(range(0,6)):
    #    bpy.data.textures["Texture"].color_ramp.elements[j].position += color_change
    #print(bpy.data.textures["Texture"].voxel_data.filepath)
    #print(text_name)

    #bpy.ops.render.render(animation=True)

    i=i+frame_count+1
