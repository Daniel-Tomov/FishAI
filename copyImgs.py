from os import listdir
import pathlib
import os
from os.path import isfile, join
import time


mypath = 'yolo/fish_data/labels/validation'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(onlyfiles)
#time.sleep(100)
for i in onlyfiles:
  if "seven" in i:
    fromPath = str(pathlib.PureWindowsPath(r'videos/7/' + i.replace("txt", "png")))
    toPath = str(pathlib.PureWindowsPath(r'yolo/fish_data/images/validation/' + i.replace("txt", "png")))
    os.system("copy " + fromPath + " " + toPath)

