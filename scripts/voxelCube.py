#!/home/marston/anaconda/bin/python
import numpy as np
import sys
import os

#specify dimensions header
resolution = 512
nx, ny, nz, nframes = resolution, resolution, resolution, resolution
header = np.array([nx,ny,nz,nframes])

for fileName in sys.argv[1:]:
	
#load data
	#fileName = sys.argv[1]
	data = np.load(fileName)
	data -= data.min()
	data = data/data.max()
	pointdata = data.flatten()
	pointdata *= 255/pointdata.max()
	print "File: %s" % fileName[18:22]
	print "Min: %3.5f" % data.min()
	print "Mean: %3.5f" % np.mean(data)
	print "Max: %3.5f" % data.max()

	#open and write to file
	binfile = open('{:}.raw'.format(os.path.basename(fileName)),'wb')
	#for i in range(0,nframes):
	pointdata.astype(np.uint8).tofile(binfile)

