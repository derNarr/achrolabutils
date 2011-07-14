#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./calibrate.py
#
# (c) 2010-2011 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2011-07-12, DW
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ATTENTION: calibrate.py does NOT work at the moment in this directory
# --> Copy this file to achrolab to make it work (even better: FIX THIS) 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from psychopy import visual,event,core
import pickle,time
from exceptions import ValueError

from colorentry import ColorEntry
from eyeone import EyeOne
from monitor import Monitor
from tubes import Tubes
from colortable import ColorTable

eyeone = EyeOne.EyeOne()#dummy=True)
mywin = visual.Window(size=(2048,1536), monitor='mymon',
                color=(0,0,0), screen=1)
mon = Monitor(eyeone, mywin)
tub = Tubes(eyeone)
tub.calibrateEyeOne()

#interessting colors
color_list = []
for i in range(5):
    color_list.append( "color" + str(129 + i) )

color_table = ColorTable(mon, tub)

color_table.loadFromPickle("./calibdata/color_table_20110126_1332.pkl")
#color_table.createColorList(patch_stim_value_list=[0.3,0.2])
#color_table.createColorList(
#        patch_stim_value_list=[x/127.5 - 1 for x in range(0,256)])

#color_table.measureColorListMonitor()
color_table.findVoltages(name_list=color_list)
color_table.saveToPickle("./calibdata/color_table_" + 
        time.strftime("%Y%m%d_%H%M") +".pkl")
color_table.saveToCsv("./calibdata/color_table_" + 
        time.strftime("%Y%m%d_%H%M") +".csv")

#color_table.findVoltagesTuning(name_list=color_list)
#color_table.measureColorListTubes()
#color_table.saveToPickle("./calibdata/color_table_" + 
#        time.strftime("%Y%m%d_%H%M") +".pkl")
#color_table.saveToCsv("./calibdata/color_table_" + 
#        time.strftime("%Y%m%d_%H%M") +".csv")
#color_table.showColorList(name_list=color_list)

#color_table.showColorList()
    



