from os import listdir
import os
from os.path import isfile, join
mypath = 'fish_data/labels/validation'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
  os.system("copy " + "fish_data/images/train/" + str(i).replace("txt", ".png") + " " + "fish_data/images/validation")

