#!/home/USERNAME/anaconda3/bin/python3.4

import webbrowser
import sys
import pyperclip
import re

if len(sys.argv) > 1:
    #get address from command line
    address = ' '.join(sys.argv[1:])
    address = re.findall(r"[\w']+", address)
    str1 = ' '.join(address)
   
else:
    #get address from clipboard
    address = pyperclip.paste()
    address = re.findall(r"[\w']+", address)
    str1  = ' '.join(address)

webbrowser.open('http://www.google.com/maps/place/' + str1)
