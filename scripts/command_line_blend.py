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

#number of frames per timestep
frame_count = 0


#initialize counter
i=301
begin = 0 #frame to start animation on
raw_file_counter = 0

#color change
color_change = 0.2/(len(sys.argv[-1:]))

print('the last argument is:'+str(sys.argv[-1:]))
files = sys.argv[-1:]
print(type(files))
#file_list = os.listdir(files[0])

for subdir, dir, files in os.walk(files[0]):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".raw"):
            #print('im in a loop')

            #--- Render beginning zoom in frames w/ just the first .raw
            if (begin < i):
                bpy.data.scenes["Scene"].frame_start = begin
                bpy.data.scenes["Scene"].frame_end = i
                bpy.data.textures["dark_matter"].voxel_data.filepath = filepath
                #bpy.ops.render.render(animation=True)
                begin = i
                print(begin)

            animate_length = len(glob.glob(subdir+os.sep+'*'))
            print('animate length is {:}'.format(animate_length/3.))
            if (raw_file_counter <= animate_length/3.):
                #--- Render time evolution
                bpy.data.scenes["Scene"].frame_start = i
                bpy.data.scenes["Scene"].frame_end = i+frame_count
                #print(filepath)
                #print('hrmpf')
                bpy.data.textures["dark_matter"].voxel_data.filepath = filepath

                #--- Start animating ---#
                #bpy.ops.render.render(animation=True)
                i = i+frame_count+1
                #print(raw_file_counter)
                raw_file_counter += 1

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
