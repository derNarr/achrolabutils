#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./justmeasure.py
#
# (c) 2011 Dominik Wabersich <dominik.wabersich [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# created 2011-10-14
# last mod 2011-10-14 DW
#
import time
from ctypes import c_float
from achrolab.eyeone import EyeOne, EyeOneConstants

#############################
#   Measurement values   ####
#############################
measurement = 5000      ####
imi = 0.5                ####
#############################
#   File Information: Short information about what exactly you are measuring
info = "Measuring tubes after turning off and immediately on again"               
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
if(EyeOne.I1_SetOption(EyeOneConstants.COLOR_SPACE_KEY, EyeOneConstants.COLOR_SPACE_CIExyY) ==
        EyeOneConstants.eNoError):
    print("Color space set to CIExyY.")
else:
    print("Failed to set color space.")

# Initialization of spectrum and colorspace
colorspace = (c_float * EyeOneConstants.TRISTIMULUS_SIZE)()
spectrum = (c_float * EyeOneConstants.SPECTRUM_SIZE)()
spec_list = []
color_list = []

# Calibration of EyeOne
print("\nPlease put EyeOne Pro on calibration plate and press \
key to start calibration.")
#TODO: Why does it want 2 keypresses??
while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
    time.sleep(0.1)
if (EyeOne.I1_Calibrate() == EyeOneConstants.eNoError):
    print("Calibration done.")
else:
    print("Calibration failed.")

print("\nPlease put EyeOne Pro in measurement position and press \
key to start measurement.")
while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
    time.sleep(0.1)

# Start measurement
print("Starting measurement...")
for i in measurements:
# Trigger measurement 
    if(EyeOne.I1_TriggerMeasurement() != EyeOneConstants.eNoError):
        print("Measurement failed.")
# retrieve Color Space
    if(EyeOne.I1_GetTriStimulus(colorspace, 0) != EyeOneConstants.eNoError):
        print("Failed to get color space.")
    else:
        print("Color Space " + str(colorspace[:]) + "\n")
        color_list.append(colorspace[:])
# retrieve spectrum 
    if(EyeOne.I1_GetSpectrum(spectrum, 0) != EyeOneConstants.eNoError):
        print("Failed to get spectrum.")
    else:
        print("Spectrum: " + str(spectrum[:]) + "\n")
        spec_list.append(spectrum[:])
    time.sleep(imi)

# Write justmeasure files containing the data
with open("calibdata/measurements/justmeasure_spec_" + time.strftime("%Y%m%d_%H%M") + ".txt", "w") as f:
    f.write("Spectrum for " + str(measurement) + " measurements with "
            + str(imi) + " intervall\n")
    f.write("Information: " + str(info) + "\n\n")
    for i in measurements:
        f.write(str(spec_list[i]))
        f.write("\n")
with open("calibdata/measurements/justmeasure_color_" + time.strftime("%Y%m%d_%H%M") + ".txt", "w") as f:
    f.write("Spectrum for " + str(measurement) + " measurements with "
            + str(imi) + " intervall\n")
    f.write("Information: " + str(info) + "\n\n")
    for i in measurements:
        f.write(str(color_list[i]))
        f.write("\n")
