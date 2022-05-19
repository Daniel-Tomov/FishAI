from os import listdir
import os
from os.path import isfile, join
mypath = 'fish_data/images/train'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
  os.system("echo 0 0 0 0 0 > fish_data/labels/train/" + str(i).replace('.png', '') + ".txt")
