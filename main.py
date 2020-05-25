#!/usr/bin/python
# Author:   @BlankGodd

import os

path = os.getcwd()
new_path = os.path.join(path,'blyrics')
try:
    os.chdir(new_path)
except:
    pass
print(os.getcwd())

from blyrics.tool import Tool

Tool()

