#! /usr/bin/env python
import numpy as np,sys,os
for filename in sys.argv[1:]:
    print filename,'-->',
    D = np.fromfile(filename,dtype=np.float32)
    #blender likes data to be 8 bit lord help us
    if False:
        D -= D.min() #subtract the min
                    # this will let us maximize the stretch
                    # in the earlier parts of reionization
                    # but has the downside of changing the
                    # colormap
    D = 255/D.max()

    #write it back out
    outfile = os.path.basename(filename)+'.raw'
    F = open(outfile)
    D.astype(np.uint8).tofile(outfile)
    print outfile
