#!/usr/bin/python3.5

import os

###change file extension for batch of files in Linux:
#for file in os.listdir('/home/USERNAME/Documents/testDir/'):
#    fileName = str(file[:-4])
#    newFileExt = ".rtf"
#    newFileName = fileName + newFileExt
#    os.rename('/home/USERNAME/Documents/testDir/'+file, '/home/USERNAME/Documents/testDir/'+newFileName)
#print("Done.")

###change the file name (only) using incrementing ints
#a=0
#for file in os.listdir('/home/USERNAME/Documents/testDir/'):
#    fileExt = str(file[-4:])
#    newFileName = "NEW00"+ str(a) + fileExt
#    os.rename('/home/USERNAME/Documents/testDir/'+file, '/home/USERNAME/Documents/testDir/'+newFileName)
#    a += 1
#print("Done.")


###change both file name and extension:
a=0
for file in os.listdir('/home/USERNAME/Documents/testDir/'):
    fileExt = ".txt"
    newFileName = "IMG00"+ str(a) + fileExt
    os.rename('/home/USERNAME/Documents/testDir/'+file, '/home/USERNAME/Documents/testDir/'+newFileName)
    a += 1
print("Done.")

