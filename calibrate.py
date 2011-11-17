#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./calibrate.py
#
# (c) 2010-2011 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2011-10-14 DW

from psychopy import visual
import time

from achrolab.eyeone import EyeOne
from achrolab.monitor import Monitor
from achrolab.tubes import CalibTubes
from achrolab.colortable import ColorTable

eyeone = EyeOne.EyeOne()
mywin = visual.Window(size=(2048,1536), monitor='mymon',
        color=(0,0,0), screen=1)    # If you get an UnboundLocalError: set screen=0, default screen=1
mon = Monitor(eyeone, mywin)
tub = CalibTubes(eyeone, calibfile="./achrolab/calibdata/lastParameterTubes.pkl")
tub.calibrateEyeOne()

#interessting colors
color_list = []
for i in range(5):
    color_list.append( "color" + str(129 + i) )

color_table = ColorTable(mon, tub)

color_table.loadFromPickle("./achrolab/calibdata/color_table_20110126_1332.pkl")
# contains several infos, especially information about the color, which
# the algorithm (findVoltages and fVTuning) is about to converge to

#color_table.createColorList(patch_stim_value_list=[0.3,0.2])   # when calibrating for the first time
#color_table.createColorList(patch_stim_value_list=[x/127.5 - 1 for x in range(0,256)])

color_table.findVoltages(name_list=color_list)
color_table.saveToPickle("./achrolab/calibdata/color_table_" + 
        time.strftime("%Y%m%d_%H%M") +".pkl")
color_table.saveToCsv("./achrolab/calibdata/color_table_" + 
        time.strftime("%Y%m%d_%H%M") +".csv")

color_table.findVoltagesTuning(name_list=color_list)
color_table.saveToPickle("./calibdata/color_table_" + 
        time.strftime("%Y%m%d_%H%M") +".pkl")
color_table.saveToCsv("./calibdata/color_table_" + 
        time.strftime("%Y%m%d_%H%M") +".csv")

#color_table.showColorList(name_list=color_list)

