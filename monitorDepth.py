#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./achrolabutils/monitorDepth.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com> und Nora
# Umbach <nora.umbach@web.de>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2012-02-08 KS

from achrolab.eyeone.EyeOne import EyeOne
from achrolab.eyeone.EyeOneConstants import  (I1_MEASUREMENT_MODE, 
                                    I1_SINGLE_EMISSION,
                                    eNoError,
                                    COLOR_SPACE_KEY, 
                                    COLOR_SPACE_CIExyY,
                                    SPECTRUM_SIZE,
                                    TRISTIMULUS_SIZE)

from psychopy import visual, core
import time,pickle
from ctypes import c_float

eye_one = EyeOne() #dummy=True)

def getDepth(colorlist, win=None, imi=0.5, screen=1, colorSpace='rgb255', n=1):
        """get the depth of monitor with colors in colorlist.
        EyeOne Pro should be connected to the computer. 
        * colorlist -- a list of PatchStim values
        * win -- psychopy.visual.Window instance or None
        * imi -- inter measurement interval.
        * n is the number of samples per color"""

        # set EyeOne Pro variables
        if(eye_one.I1_SetOption(I1_MEASUREMENT_MODE, I1_SINGLE_EMISSION) ==
                eNoError):
            print("Measurement mode set to single emission.")
        else:
            print("Failed to set measurement mode.")
            return

        if(eye_one.I1_SetOption(COLOR_SPACE_KEY, COLOR_SPACE_CIExyY) ==
                eNoError):
            print("Color space set to CIExyY.")
        else:
            print("Failed to set color space.")
            return

        # calibrate EyeOne Pro
        print("\nPlease put EyeOne-Pro on calibration plate and "
        + "press key to start calibration.")
        while(eye_one.I1_KeyPressed() != eNoError):
            time.sleep(0.01)
        if (eye_one.I1_Calibrate() == eNoError):
            print("Calibration of EyeOne Pro done.")
        else:
            print("Calibration of EyeOne Pro failed. Please RESTART.")
            return

        ## measurement
        if not win:
            win = visual.Window(size=(800,600), color=0.4, monitor='mymon',
                    screen=screen, colorSpace=colorSpace)

        #pos = sizeSur/2 + 0.02
        patch_stim = visual.PatchStim(win, units='norm', size=(2,2),
                pos=[0,0], sf=0, color=-0.1450980, colorSpace=colorSpace)
        patch_stim.setColor(-0.5, colorSpace=colorSpace)
        patch_stim.draw()
        win.flip()

        # prompt for click on button of EyeOne Pro
        print("\nPlease put EyeOne-Pro in measurement position and hit"
        + " button to start measurement.")
        while(eye_one.I1_KeyPressed() != eNoError):
            time.sleep(0.01)

        with open('calibdata/measurements/depth_monitor' +
                time.strftime("%Y%m%d_%H%M") + '.txt', 'w') as calibfile:

            print("Starting measurement...")

            xyY_list = list() # saves the measured xyY value

            tristim = (c_float * TRISTIMULUS_SIZE)() # memory to where EyeOne
                                                     # Pro saves TriStim.
            spectrum = (c_float * SPECTRUM_SIZE)()   # memory to where EyeOne
                                                     # Pro saves spectrum.

            for color in colorlist:
                for i in range(n):
                    patch_stim.setColor(color, colorSpace=colorSpace)
                    print(color)
                    patch_stim.draw()
                    win.flip()

                    time.sleep(imi) # to give EyeOne Pro time to adapt and to
                                    # reduce carry-over effects

                    if(eye_one.I1_TriggerMeasurement() != eNoError):
                        print("Measurement failed for color %s ." %str(color))
                    if(eye_one.I1_GetTriStimulus(tristim, 0) != eNoError):
                        print("Failed to get TriStimulus for color %s ."
                                %str(color))
                    if(eye_one.I1_GetSpectrum(spectrum, 0) != eNoError):
                        print("Failed to get spectrum for color %s ."
                                %str(color))
                    xyY_list.append(list(tristim))

                    if isinstance(color, int):
                        calibfile.write(str(color) + ", " +
                                ", ".join([str(x) for x in tristim]) +
                                ", " + ", ".join([str(x) for x in spectrum]) +
                                "\n")
                    else:
                        calibfile.write(", ".join([str(x) for x in color]) +
                                ", " + ", ".join([str(x) for x in tristim]) +
                                ", " + ", ".join([str(x) for x in spectrum]) +
                                "\n")
        print("Measurement finished.")


if(__name__=="__main__"):

    #patch_stim_value_list = [x/127.5 - 1 for x in range(120,130)]
    #patch_stim_rgb = (122,123,124)
    #patch_stim_rgb = list()
    #for r in range(109,150):
    #    for g in range(100,150):
    #        for b in range(100,150):
    #            patch_stim_rgb.append( (r,g,b) )

    #from grey_dict import grey_dict
    #patch_stim_rgb = grey_dict.values()


    ## Code to check for significant bit on the left side of the EIZO
    ## GS320 monitor
    #patch_stim_rgb = list()
    #for b in (0,1,2,4,8,16,32,64,128):
    #    patch_stim_rgb.append( (0,180,b) )

    ## Code to check for significant bit on the right side of the EIZO
    ## GS320 monitor
    #patch_stim_rgb = list()
    #for b in (0,1,2,4,8,16,32,64,128):
    #    patch_stim_rgb.append( (180,0,b) )

    ## all greys on EIZO GS320
    import eizoGS320
    patch_stim_rgb = [eizoGS320.encode_color(x, x) for x in range(620,630)]

    mywin = visual.Window(size=(1024,1536), monitor='mymon',
                color=(1,1,1), screen=0, colorSpace='rgb')

    getDepth(patch_stim_rgb, win=mywin, imi=0.5, colorSpace='rgb255', n=5)

