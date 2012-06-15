#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./just_measure.py
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
# last mod 2012-05-29, NU

import time
from ctypes import c_float
from achrolab.eyeone import EyeOne, EyeOneConstants

#############################
#   Measurement values   ####
#############################
# measurement: how many measurements should one measurement process include
# imi: inter measurement intervall
measurement = 150000      ####
imi = 0.5                ####
#############################
# Repeat Measure-Process ####
#############################
# times: times variable repeats the whole measurement process 'times' times
# and asks to press the eyeone button before every new time.
# recalibrate: if times > 1, you can set 'recalibrate' to true, to recalibrate
# for every measurement process 
times = 30               ####
recalibrate = True       ####
#############################
# Measuring Information  ####
#############################
# info: short information about what exactly you are measuring
# prefix: file prefix (in the filename)
info = "Measruring screen 30 times with different calibrations"
prefix = "30calib"
#############################

# make measurements to a list for iterations
measurements = range(measurement)

EyeOne = EyeOne.EyeOne() # EyeOne Object

# set EyeOne Pro variables
if(EyeOne.I1_SetOption(EyeOneConstants.I1_MEASUREMENT_MODE,
    EyeOneConstants.I1_SINGLE_EMISSION) ==
        EyeOneConstants.eNoError):
    print("Measurement mode set to single emission.")
else:
    print("Failed to set measurement mode.")
if(EyeOne.I1_SetOption(EyeOneConstants.COLOR_SPACE_KEY,
    EyeOneConstants.COLOR_SPACE_CIExyY) == EyeOneConstants.eNoError):
    print("Color space set to CIExyY.")
else:
    print("Failed to set color space.")

# Initialization of spectrum and colorspace
colorspace = (c_float * EyeOneConstants.TRISTIMULUS_SIZE)()
spectrum = (c_float * EyeOneConstants.SPECTRUM_SIZE)()
spec_list = []
color_list = []

    # Start measurement
with open("calibdata/measurements/justmeasure_" + str(prefix) + "_spec_" +
    time.strftime("%Y%m%d_%H%M") + ".txt", "w") as f1:
    f1.write("Spectrum for " + str(measurement) + " measurements with "
            + str(imi) + " intervall\n" + str(times) + " times with" +
            "recalibration set " + str(recalibrate) + "\n")
    f1.write("Information: " + str(info) + "\n\n")
    with open("calibdata/measurements/justmeasure_" + str(prefix) +
    "_color_" + time.strftime("%Y%m%d_%H%M") + ".txt", "w") as f2:
        f2.write("Spectrum for " + str(measurement) + " measurements with "
                + str(imi) + " intervall\n" + str(times) + " times with " + 
                "recalibration set " + str(recalibrate) + "\n")
        f2.write("Information: " + str(info) + "\n\n")
        for n in range(times):
            if (recalibrate or (EyeOne.I1_TriggerMeasurement() ==
                EyeOneConstants.eDeviceNotCalibrated)):
                # Calibration of EyeOne
                print("\nPlease put EyeOne Pro on calibration plate and
                press \n key to start calibration.")
                while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
                    time.sleep(0.1)
                if (EyeOne.I1_Calibrate() == EyeOneConstants.eNoError):
                    print("Calibration done.")
                else:
                    print("Calibration failed.")

            print("\nPlease put EyeOne Pro in measurement position and
            press \n key to start measurement.")
            while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
                time.sleep(0.1)

            print("Starting measurement...")
            for i in measurements:
            # Trigger measurement 
                if(EyeOne.I1_TriggerMeasurement() != EyeOneConstants.eNoError):
                    print("Measurement failed.")
            # retrieve Color Space
                if(EyeOne.I1_GetTriStimulus(colorspace, 0) !=
                    EyeOneConstants.eNoError):
                    print("Failed to get color space.")
                else:
                    print("Color Space " + str(colorspace[:]) + "\n")
                    color_list.append(colorspace[:])
                    # Write justmeasure color file containing the data
                    f2.write(str(colorspace[:])[1:-1])
                    f2.write("\n")
            # retrieve spectrum 
                if(EyeOne.I1_GetSpectrum(spectrum, 0) !=
                    EyeOneConstants.eNoError):
                    print("Failed to get spectrum.")
                else:
                    print("Spectrum: " + str(spectrum[:]) + "\n")
                    spec_list.append(spectrum[:])
                    # Write justmeasure spectrum file containing the data
                    f1.write(str(spectrum[:])[1:-1] + "\n")
                    f1.write("\n")
                time.sleep(imi)

