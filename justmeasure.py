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
measurements = 1000      ####
imi = 0.5                ####
#############################
#   File Information: Short information about what exactly you are measuring
info = "Measuring tubes after plugging in"               
#############################

# make measurements to a list for iterations
measurements = range(0,measurements)

EyeOne = EyeOne.EyeOne() # EyeOne Object

# Initialization of spectrum and colorspace
colorspace = (c_float * EyeOneConstants.TRISTIMULUS_SIZE)()
spectrum = (c_float * EyeOneConstants.SPECTRUM_SIZE)()
spec_list = []

# Calibration of EyeOne
print("\nPlease put EyeOne Pro on calibration plate and press \
key to start calibration.")
while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
    time.sleep(0.1)
if (EyeOne.I1_Calibrate() == EyeOneConstants.eNoError):
    print("Calibration done.")
else:
    print("Calibration failed.")

# Trigger measurement and retrieve spectrum and color space.
print("\nPlease put EyeOne Pro in measurement position and press \
key to start measurement.")
while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
    time.sleep(0.1)
if(EyeOne.I1_TriggerMeasurement() != EyeOneConstants.eNoError):
    print("Measurement failed.")

# Color Space
if(EyeOne.I1_GetTriStimulus(colorspace, 0) != EyeOneConstants.eNoError):
    print("Failed to get color space.")
else:
    print("Color Space " + str(colorspace[:]) + "\n")

# Start measurement
print("Starting measurement...")
for i in measurements:
    if(EyeOne.I1_GetSpectrum(spectrum, 0) != EyeOneConstants.eNoError):
        print("Failed to get spectrum.")
    else:
        print("Spectrum: " + str(spectrum[:]) + "\n")
        spec_list.append(spectrum)
    time.sleep(imi)

# Write justmeasure file containing the data
with open("justmeasure_" + time.strftime("%Y%m%d_%H%M") + ".txt", "w") as f:
    f.write("Spectrum for " + measurements.pop() + " measurements with " + imi + " intervall\n")
    f.write("Information: " + info + "\n\n")
    for i in measurements:
        f.write(spec_list[i] + "\n")

