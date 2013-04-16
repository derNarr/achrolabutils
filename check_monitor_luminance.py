#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./check_monitor_luminance.py
#
# (c) 2012 Nora Umbach <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: (1) Measure luminance of monitor:
#               (1.1) up
#               (1.2) down
#               (1.3) random
#
# input: --
# output: --
#
# created 2012-09-13 NU
# last mod 2013-01-29 11:31 KS

import sys
sys.path.append("../achrolabutils")
sys.path.append("..")

import time
import random
from psychopy import visual

from stimuli import eizoGS320

from achrolab.eyeone.eyeone import EyeOne
from achrolab.calibmonitor import CalibMonitor

eyeone = EyeOne()

mywin = visual.Window([1024,1536], monitor='mymon', color=(155,155,17),
        screen=1, colorSpace="rgb255", allowGUI=False)

mon = CalibMonitor(eyeone, mywin)

eyeone.calibrate()

###### (1) Measure luminance of monitor ######

ncol = 860
# measure colors from 0 to 860; if you want a certain range, adjust col_list
# for all three methods (up, down, random)

###### (1.2) up ######
col_list = range(ncol)
xyY_list = list()

print("up")

dataFile = open('D:/software/achrolabutils/calibdata/measurements/monitor_up_' +
        time.strftime("%Y%m%d_%H%M") + '.csv', 'w')

# add headline to files
dataFile.write('color' + ',' + 'x' + ',' + 'y' + ',' + 'Y' + '\n')

for color in col_list:
    xyY_list.append(mon.measureGratingStimColor(eizoGS320.encode_color(color,
        color)))
    print(color)

for i in range(len(col_list)):
    dataFile.write(str(col_list[i]) + ',' + str(xyY_list[i][0][0]) + ',' +
            str(xyY_list[i][0][1]) + ',' + str(xyY_list[i][0][2]) + '\n')

# close dataFile
dataFile.close()

###### (1.2) down ######
col_list.reverse()
xyY_list = list()

print("down")

dataFile = open('D:/software/achrolabutils/calibdata/measurements/monitor_down_'
        + time.strftime("%Y%m%d_%H%M") + '.csv', 'w')

# add headline to files
dataFile.write('color' + ',' + 'x' + ',' + 'y' + ',' + 'Y' + '\n')

for color in col_list:
    xyY_list.append(mon.measureGratingStimColor(eizoGS320.encode_color(color,
        color)))
    print(color)

for i in range(len(col_list)):
    dataFile.write(str(col_list[i]) + ',' + str(xyY_list[i][0][0]) + ',' +
            str(xyY_list[i][0][1]) + ',' + str(xyY_list[i][0][2]) + '\n')

# close dataFile
dataFile.close()

###### (1.3) random ######
col_list = random.sample(range(ncol), ncol)
xyY_list = list()

print("random")

dataFile = open('D:/software/achrolabutils/calibdata/measurements/monitor_random_' + time.strftime("%Y%m%d_%H%M") + '.csv', 'w')

# add headline to files
dataFile.write('color' + ',' + 'x' + ',' + 'y' + ',' + 'Y' + '\n')

for color in col_list:
    xyY_list.append(mon.measureGratingStimColor(eizoGS320.encode_color(color,
        color)))
    print(color)

for i in range(len(col_list)):
    dataFile.write(str(col_list[i]) + ',' + str(xyY_list[i][0][0]) + ',' +
            str(xyY_list[i][0][1]) + ',' + str(xyY_list[i][0][2]) + '\n')

# close dataFile
dataFile.close()


