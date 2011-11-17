#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./checkCalibration.py
#
# (c) 2011 Dominik Wabersich <dominik.wabersich [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# created 2011-10-14
# last mod 2011-10-14 DW
#

from psychopy import visual

from achrolab.eyeone import EyeOne
from achrolab.monitor import Monitor
from achrolab.tubes import Tubes
from achrolab.colortable import ColorTable

eyeone = EyeOne.EyeOne()#dummy=True)
mywin = visual.Window(size=(2048,1536), monitor='mymon',
        color=(0,0,0), screen=1)    # If you get an UnboundLocalError: set screen=0, default screen=1
mon = Monitor(eyeone, mywin)
tub = Tubes(eyeone, calibfile="./achrolab/calibdata/lastParameterTubes.pkl")
tub.calibrateEyeOne()

color_table = ColorTable(mon, tub)
color_table.loadFromPickle("./achrolab/calibdata/color_table_20110126_1332.pkl")

# measuring part
color_table.measureColorListMonitor()
color_table.measureColorListTubes()

# checking part
color_list = []
for i in range(5):
    color_list.append( "color" + str(129 + i) )

color_table.checkColorTable(index_list=color_list)
