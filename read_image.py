## dependencies py3
# numpy --> MAc pip3 install numpy
# additional dependencies brew install cmake pkg-config
#for reding different image formats--> brew install jpeg libpng libtiff openexr
# brew install eigen tbb
# for the latest updates--> download it from source channel --> git clone https://github.com/opencv/opencv


import cv2 # open any youtube tutorial or see open cv docs for installation on specific os
import numpy as np # library for numbers
import sys #required module  for reading from system
import os.path # reauired for reading path of a file

#I need a input and output file which I try to pass as system arguments --> validation

if len(sys.argv) !=3:
    print ("input_file output_file") % (sys.argv[0])
    sys.exit()
else: 
    input_file =sys.argv[1]
    output_file = sys.argv[2]

if not os.path.isfile(input_file):
    print ("No such file") % input_file
    sys.exit()

DEBUG = 0




