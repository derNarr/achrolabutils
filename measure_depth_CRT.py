#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./measure_depth.py
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: Script for measuring monitor; define how many measurements,
# if you want to recalibrate i1, etc.
#
# input: --
# output: --
#
# created 2011-10-14
# last mod 2014-05-13 NU

import sys
sys.path.append("D:\\software\\achrolabutils")
sys.path.append("D:\\software\\")

import time
from achrolab import printing
from ctypes import c_float
from achrolab.eyeone import eyeone, constants
from psychopy import visual

from stimuli import eizoGS320

#############################
#   Measurement values   ####
#############################
# colors: list of colors that should be measured
# imi: inter measurement interval
colors = range(256)
imi = 0.5

#############################
# Repeat Measure-Process ####
#############################
# times: times variable repeats the whole measurement process 'times' times
#       and asks to press the eyeone button before every new time.
# each: how often every stimulus will be repeated
# recalibrate: if times > 1, you can set 'recalibrate' to true, to recalibrate
#       for every measurement process
times = 1
each = 5
recalibrate = False

#############################
# Measuring Information  ####
#############################
# prefix: file prefix (in the filename)
prefix = "./LCD_luminance_"
#############################

eyeone = eyeone.EyeOne(dummy=False) # EyeOne Object

# set EyeOne Pro variables
if(eyeone.I1_SetOption(constants.I1_MEASUREMENT_MODE,
    constants.I1_SINGLE_EMISSION) ==
        constants.eNoError):
    print("Measurement mode set to single emission.")
else:
    print("Failed to set measurement mode.")
if(eyeone.I1_SetOption(constants.COLOR_SPACE_KEY,
    constants.COLOR_SPACE_CIExyY) == constants.eNoError):
    print("Color space set to CIExyY.")
else:
    print("Failed to set color space.")

# Initialization of spectrum and colorspace
colorspace = (c_float * constants.TRISTIMULUS_SIZE)()
spectrum = (c_float * constants.SPECTRUM_SIZE)()
spec_list = []
color_list = []

#set monitor color
mywin = visual.Window([1280,1024], monitor="mymon", color=0,
        screen=0, colorSpace="rgb255", allowGUI=False, units="pix")
    # teststim=SquareStim(mywin,color=500, size=1024)

    #background = eizoGS320.decode_color((mywin.color[0], mywin.color[1], mywin.color[2]))
    #if not(background[0] == background[1]):
    #print("WARNING: There is something wrong with the background color")
teststim = visual.GratingStim(mywin, tex=None, units='norm', pos=(0, 0), size=2,
                          colorSpace=mywin.colorSpace,
                          color=100)
# while color > 0:
#     teststim.draw()
#     mywin.flip()
#     color-=10
#     teststim.setColor(eizoGS320.encode_color(color, color))
#     print("something")
#     if event.getKeys(keyList='escape'):
#         break

# import pdb #@@@
# pdb.set_trace() #@@@
# print 'stop here' #@@@

def measure(color):
    print "Color:" + str(color)
    teststim.setColor(color)
    teststim.draw()
    mywin.flip()
    time.sleep(imi)
    # Trigger measurement
    if(eyeone.I1_TriggerMeasurement() != constants.eNoError):
        print("Measurement failed.")
    # retrieve Color Space
    if(eyeone.I1_GetTriStimulus(colorspace, 0) != constants.eNoError):
        print("Failed to get color space.")
    else:
        print("Color Space " + str(colorspace[:]) + "\n")
        color_list.append(colorspace[:])
                # Write justmeasure color file containing the data
                # f2.write(str(colorspace[:])[1:-1])
                #f2.write("\n")
        # retrieve spectrum
    if(eyeone.I1_GetSpectrum(spectrum, 0) != constants.eNoError):
        print("Failed to get spectrum.")
    else:
        print("Spectrum: " + str(spectrum[:]) + "\n")
        spec_list.append(spectrum[:])
    # write data to file
    file.write_data_txt(grayvals=[color, color], rgb=None, xyY=colorspace,
            voltage=None, spec_list=spectrum, delimiter="\t")


with printing.CalibDataFile(prefix=prefix) as file:
    for n in range(times):
        print("\nRound " + str(n + 1) + " of " + str(times) + ".\n")
        # Put color changing code here, swap measurements dependence for
        # some color dependence, and set times to number of recalibrations
        # (perhaps batches of small numbers)
        # Then recalibrate, repeat for all colours
        if (recalibrate or (eyeone.I1_TriggerMeasurement() ==
            constants.eDeviceNotCalibrated)):
            # Calibration of EyeOne
            print("\nPlease put EyeOne Pro on calibration plate and press \n key to start calibration.")
            while(eyeone.I1_KeyPressed() != constants.eNoError):
                time.sleep(0.1)
            if (eyeone.I1_Calibrate() == constants.eNoError):
                print("Calibration done.")
            else:
                print("Calibration failed.")

        print("\nPlease put EyeOne Pro in measurement position and press \n key to start measurement.")

        while(eyeone.I1_KeyPressed() != constants.eNoError):
            time.sleep(0.1)
        print("Starting measurement...")
        for color in colors:
            for i in range(each):
                measure(color)

