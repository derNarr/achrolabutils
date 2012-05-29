#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./getDepth_pyglet.py
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content:
#
# input: --
# output: --
#
# created
# last mod 2012-02-08 KS

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

import pyglet
from pyglet import gl

eye_one = EyeOne() #dummy=True)
 
def drawRect(grey, win):
    gl.glBegin(gl.GL_QUADS)
    gl.glColor3ub( grey[0], grey[1], grey[2] )
    gl.glVertex2f(0,0)
    gl.glVertex2f(win.width, 0)
    gl.glVertex2f(win.width, win.height)
    gl.glVertex2f(0, win.height)
    gl.glEnd()

def getDepth_pyglet(colorlist, imi=0.5, n=1):
        """get the depth of monitor with colors in colorlist.
        EyeOne Pro should be connected to the computer. 
        * colorlist -- a color list
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
        XSize = 1280
        YSize = 1024
        win = pyglet.window.Window(XSize,YSize)
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(0, XSize, YSize, 0, 0, 1)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        drawRect([255, 0, 0], win)
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
                    print(color)
                    gl.glLoadIdentity()
                    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
                    drawRect(color, win)
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
    from grey_dict import grey_dict
    
    greylist = grey_dict.values()
    greylist = greylist[720:730]

    getDepth_pyglet(greylist, imi=1, n=5)

