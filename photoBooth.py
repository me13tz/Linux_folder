#!/usr/bin/python3.4

import sys
import os
import os.path
import time

fcount = 0

def photoBooth():
    global fcount
    suffix = (".jpg")
    if os.path.isfile("/home/cassius/Documents/python files/photodir/1.jpg"):
        print("File Found")
        ###command to print file out to external printer here
        newstr = (str(fcount)+suffix)
        os.system("mv 1.jpg /home/cassius/Documents/python\ files/{}".format(newstr))
        fcount += 1
        photoBooth()
    else:
        time.sleep(.5)
        print('.', end='')
        sys.stdout.flush()
        photoBooth()

photoBooth()
