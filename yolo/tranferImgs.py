from os import listdir
import pathlib
import os
from os.path import isfile, join
mypath = 'fish_data/labels/validation'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
  if "two" in i:
    trainPath = str(pathlib.PureWindowsPath(r'fish_data/images/train/' + i.replace("txt", "png")))
    valPath = str(pathlib.PureWindowsPath(r'fish_data/images/validation/' + i.replace("txt", "png")))
    os.system("copy " + trainPath + " " + valPath)

