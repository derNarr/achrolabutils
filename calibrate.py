#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./calibrate.py
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: find matching color for monitor and wall 
#
# input: --
# output: --
#
# created
# last mod 2012-06-20, KS

from achrolab.eyeone.eyeone import EyeOne
from achrolab.calibmonitor import CalibMonitor
from achrolab.calibtubes import CalibTubes
from achrolab.colortable import ColorTable
from achrolab.colorentry import ColorEntry
from achrolab.calibrate import Calibrate

from psychopy import visual

from monitor import eizoGS320

eyeone = EyeOne()

mywin = visual.Window([1024,1536], monitor='mymon', color=(155,155,17),
        screen=1, colorSpace="rgb255", allowGUI=False)

calibmonitor = CalibMonitor(eyeone, mywin)
calibtubes = CalibTubes(eyeone)

#calibtubes.is_calibrated = True
calibrate = Calibrate(calibmonitor, calibtubes)
colortable = ColorTable()

color1 = ColorEntry("color850", patch_stim_value=eizoGS320.encode_color(850, 850))
color2 = ColorEntry("color600", patch_stim_value=eizoGS320.encode_color(600, 600))
color3 = ColorEntry("color390", patch_stim_value=eizoGS320.encode_color(390, 390))

## MONITOR
#calibrate.calibmonitor.startMeasurement()
#calibrate._measureColorEntryMonitor(color1, n=20)
#calibrate._measureColorEntryMonitor(color2, n=20)
#calibrate._measureColorEntryMonitor(color3, n=20)
#
#with open("measured_colors_monitor.txt", "w") as f:
#    for color in (color1, color2, color3):
#        f.write(str(color.name)+"\n")
#        f.write(str(color.patch_stim_value)+"\n")
#        f.write(str(color.monitor_xyY)+"\n")
#        f.write(str(color.monitor_xyY_sd)+"\n")
#        f.write(str(color.voltages)+"\n")
#        f.write(str(color.tubes_xyY)+"\n")
#        f.write(str(color.tubes_xyY_sd)+"\n")
#
#
## TUBES
#colors = (color1, color2, color3)
filenames = ("calibdata/parameter_tubes_00_abs.pkl",
        "calibdata/parameter_tubes_50_abs.pkl",
        "calibdata/parameter_tubes_75_abs.pkl")
#
#for i in range(len(filenames)):
#    print("NEXT COLOUR!")
#    calibrate.calibtubes.startMeasurement()
#    calibtubes.loadParameter(filename=filenames[i])
#
#    start_voltages = colors[i].voltages
#    (voltages, xyY, spectrum) = calibrate.adjustManualPlot(
#            colors[i].monitor_xyY, start_voltages)
#    voltages_vision = calibrate.adjustManualVision(
#            colors[i].patch_stim_value, voltages)
#    colors[i].voltages = voltages_vision
#    calibrate.calibtubes.startMeasurement()
#    calibrate._measureColorEntryTubes(colors[i], n=20)
#
#with open("measured_colors.txt", "w") as f:
#    for color in (color1, color2, color3):
#        f.write(str(color.name)+"\n")
#        f.write(str(color.patch_stim_value)+"\n")
#        f.write(str(color.monitor_xyY)+"\n")
#        f.write(str(color.monitor_xyY_sd)+"\n")
#        f.write(str(color.voltages)+"\n")
#        f.write(str(color.tubes_xyY)+"\n")
#        f.write(str(color.tubes_xyY_sd)+"\n")

# only for color3
calibtubes.loadParameter(filename=filenames[0])
voltages_vision = calibrate.adjustManualVision(
        color3.patch_stim_value, [1024, 1539, 1483])
color3.voltages = voltages_vision
f.write(str(color3.name)+"\n")
f.write(str(color3.patch_stim_value)+"\n")
f.write(str(color3.monitor_xyY)+"\n")
f.write(str(color3.monitor_xyY_sd)+"\n")
f.write(str(color3.voltages)+"\n")
f.write(str(color3.tubes_xyY)+"\n")
f.write(str(color3.tubes_xyY_sd)+"\n")

