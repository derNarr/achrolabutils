#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./measure_depth.py
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: Script for measuring monitor or tubes; define how many measurements,
# if you want to recalibrate i1, etc.
#
# input: --
# output: --
#
# created 2011-10-14
# last mod 

import time
import printing
from ctypes import c_float
from achrolab.eyeone import eyeone, constants
from contextlib import closing
from psychopy import visual
from monitor import eizoGS320

#############################
#   Measurement values   ####
#############################
# imi: inter measurement interval
#measurement = 5  #changed to colour dependence, use times now    ####
imi = 0.5                ####
#############################
# Repeat Measure-Process ####
#############################
# times: times variable repeats the whole measurement process 'times' times
# and asks to press the eyeone button before every new time.
# recalibrate: if times > 1, you can set 'recalibrate' to true, to recalibrate
# for every measurement process
times = 1               ####
recalibrate = True       ####
#############################
# Measuring Information  ####
#############################
# prefix: file prefix (in the filename)
prefix = "gdata"
#############################

EyeOne = eyeone.EyeOne(dummy=False) # EyeOne Object

# set EyeOne Pro variables
if(EyeOne.I1_SetOption(constants.I1_MEASUREMENT_MODE,
    constants.I1_SINGLE_EMISSION) ==
        constants.eNoError):
    print("Measurement mode set to single emission.")
else:
    print("Failed to set measurement mode.")
if(EyeOne.I1_SetOption(constants.COLOR_SPACE_KEY,
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

mywin = visual.Window([1024,1536], monitor="mymon", color=(100,100,0),
        screen=1, colorSpace="rgb255", allowGUI=False, units="pix")
color=400
    # teststim=SquareStim(mywin,color=500, size=1024)

    #background = eizoGS320.decode_color((mywin.color[0], mywin.color[1], mywin.color[2]))
    #if not(background[0] == background[1]):
    #print("WARNING: There is something wrong with the background color")
teststim=visual.PatchStim(mywin, tex=None, units='norm', pos=(0, 0), size=2, colorSpace=mywin.colorSpace, color=eizoGS320.encode_color(400, 400))
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

with closing(printing.CalibDataFile(prefix=prefix)) as test:
    for n in range(times):
        #Put color changing code here, swap measurements dependence for some color dependence, and set times to number of recalibrations (perhaps batches of small numbers)
        #Then recalibrate, repeat for all colours
        if (recalibrate or (EyeOne.I1_TriggerMeasurement() ==
            constants.eDeviceNotCalibrated)):
            # Calibration of EyeOne
            print("\nPlease put EyeOne Pro on calibration plate and press \n key to start calibration.")
            while(EyeOne.I1_KeyPressed() != constants.eNoError):
                time.sleep(0.1)
            if (EyeOne.I1_Calibrate() == constants.eNoError):
                print("Calibration done.")
            else:
                print("Calibration failed.")

        print("\nPlease put EyeOne Pro in measurement position and press \n key to start measurement.")

        while(EyeOne.I1_KeyPressed() != constants.eNoError):
            time.sleep(0.1)
        print("Starting measurement...")
        while color>0: #for i in measurements: - swap measurements for colorr dependence
            # Trigger measurement
            if(EyeOne.I1_TriggerMeasurement() != constants.eNoError):
                print("Measurement failed.")
            # retrieve Color Space
            if(EyeOne.I1_GetTriStimulus(colorspace, 0) != constants.eNoError):
                print("Failed to get color space.")
            else:
                print("Color Space " + str(colorspace[:]) + "\n")
                color_list.append(colorspace[:])
                        # Write justmeasure color file containing the data
                        # f2.write(str(colorspace[:])[1:-1])
                        #f2.write("\n")
                # retrieve spectrum
            if(EyeOne.I1_GetSpectrum(spectrum, 0) != constants.eNoError):
                print("Failed to get spectrum.")
            else:
                print("Spectrum: " + str(spectrum[:]) + "\n")
                spec_list.append(spectrum[:])
                        # Write justmeasure spectrum file containing the data
                        # f1.write(str(spectrum[:])[1:-1] + "\n")
                        #f1.write("\n")

                        #is colorspace RGB values or xyY values, must test
                test.writeDataTXT(grayvals=[color, color], rgb=None, xyY=colorspace, voltage=None, spec_list=spectrum, delimiter="\t")
                color-=5
                print "Color:" + str(color)
                teststim.setColor(eizoGS320.encode_color(color, color))
                teststim.draw()
                mywin.flip()
                time.sleep(imi)
                #Write grey values, xyY values, measured RGB values, spectral values, no voltage values
                #Perhaps check the RGB values are decoded back in to roughly the same grey values



