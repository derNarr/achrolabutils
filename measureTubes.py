#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./calibrate.py
#
# (c) 2010-2011 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2012-02-08 KS

from achrolab.devtubes import DevTubes
from achrolab.eyeone.EyeOne import EyeOne
from achrolab.eyeone.EyeOneConstants import  (I1_MEASUREMENT_MODE, 
                                    I1_SINGLE_EMISSION,
                                    eNoError,
                                    COLOR_SPACE_KEY, 
                                    COLOR_SPACE_CIExyY,
                                    SPECTRUM_SIZE,
                                    TRISTIMULUS_SIZE)
import time
from ctypes import c_float

tub = DevTubes()
eyeone = EyeOne() #dummy=True)

def measureTubes(voltages, imi=0.5, each=1):
    # set EyeOne Pro variables
    if(eyeone.I1_SetOption(I1_MEASUREMENT_MODE, I1_SINGLE_EMISSION) ==
            eNoError):
        print("Measurement mode set to single emission.")
    else:
        print("Failed to set measurement mode.")
        return

    if(eyeone.I1_SetOption(COLOR_SPACE_KEY, COLOR_SPACE_CIExyY) ==
            eNoError):
        print("Color space set to CIExyY.")
    else:
        print("Failed to set color space.")
        return

    # calibrate EyeOne Pro
    print("\nPlease put EyeOne-Pro on calibration plate and "
    + "press key to start calibration.")
    while(eyeone.I1_KeyPressed() != eNoError):
        time.sleep(0.01)
    if (eyeone.I1_Calibrate() == eNoError):
        print("Calibration of EyeOne Pro done.")
    else:
        print("Calibration of EyeOne Pro failed. Please RESTART.")
        return

    tri_stim = (c_float * TRISTIMULUS_SIZE)() # memory where EyeOne Pro
                                                      # saves tristim.
    spectrum = (c_float * SPECTRUM_SIZE)()    # memory where EyeOne Pro
                                              # saves spectrum.
    # prompt for click on button of EyeOne Pro
    print("\nPlease put EyeOne-Pro in measurement position and hit"
    + " button to start measurement.")
    while(eyeone.I1_KeyPressed() != eNoError):
        time.sleep(0.01)

    print("WAIT ONE HOUR TO HEAT TUBES, remove code, if tubes are warm.")
    time.sleep(60*60)

    with open('calibdata/measurements/measure_tubes_' +
            time.strftime("%Y%m%d_%H%M") + '.txt', 'w') as calibfile:
        calibfile.write("volR, volG, volB, x, y, Y," +
                ", ".join(["l" + str(x) for x in range(1,37)]) + "\n")

        print("Starting measurement...")

        for voltage in voltages:
            for i in range(each):
                tub.setVoltages(voltage)
                print(voltage)
                time.sleep(imi) # to give the EyeOne Pro time to adapt and to
                                # reduce carry-over effects
                if(eyeone.I1_TriggerMeasurement() != eNoError):
                    print("Measurement failed for voltage %s ." %str(voltage))
                if(eyeone.I1_GetTriStimulus(tri_stim, 0) != eNoError):
                    print("Failed to get tristim for voltage %s ."
                            %str(voltage))
                if(eyeone.I1_GetSpectrum(spectrum, 0) != eNoError):
                    print("Failed to get spectrum for voltage %s ."
                            %str(voltage))

                #write data
                calibfile.write(", ".join([str(x) for x in voltage]) +
                                ", " + ", ".join([str(x) for x in tri_stim]) +
                                ", " + ", ".join([str(x) for x in spectrum]) + 
                                "\n")
                calibfile.flush()

if __name__=="__main__":
    voltages = list()
    for r in range(1248,1276):
        for g in range(1634,1683):
            for b in range(1630,1676):
                voltages.append( (r,g,b) )
    print(len(voltages))

    #voltages = [ (1248, 1634, 1630), (1275, 1683, 1676) ]
    measureTubes( voltages, imi=0.5, each=5 )
