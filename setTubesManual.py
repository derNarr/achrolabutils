#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./achrolabutils/iterativColorTubes.py
#
# (c) 2010-2011 Konstantin Sering <konstantin.sering [aet] gmail.com>
#     and Dominik Wabersich <wabersich [aet] gmx.net>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2012-02-16 KS

import matplotlib.pyplot as plt
import numpy as np

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


def tellme(s, plot):
    print s
    plot.set_title(s,fontsize=16)
    plt.draw()

def setColorTube(key):
    """
    Defines which color tubes should be changed.
    """
    if key == 'r':
        return ('red', 0)
    elif key == 'g':
        return ('green', 1)
    elif key == 'b':
        return ('blue', 2)
    elif key == 'a':
        return ('all', None) #second element is out of range, should not be used!
    else:
        pass

def setStepSize(key):
    """
    Defines step size of change.
    """
    if key == '1':
        return 1
    elif key == '2':
        return 5
    elif key == '3':
        return 10
    elif key == '4':
        return 50
    elif key == '5':
        return 100
    else:
        pass

class SetTubesManual(object):
    def __init__(self, voltages=(1224, 1726, 1680), 
            target_xyY=(0.2982336, 0.3200846, 20.62395)):
        self.voltages = list(voltages)
        self.target_xyY = target_xyY
        self.tub = DevTubes()
        self.eyeone = EyeOne()#dummy=True)
        self.imi = 0.5
        self.each = 5 #number of measurements per voltage
        self.colortube = ('red', 0)
        self.step = 10
        self.i = 0 # number of measurement
        self.fig = None
 
        # set EyeOne Pro variables
        if(self.eyeone.I1_SetOption(I1_MEASUREMENT_MODE, I1_SINGLE_EMISSION) ==
                eNoError):
            print("Measurement mode set to single emission.")
        else:
            print("Failed to set measurement mode.")
            return
    
        if(self.eyeone.I1_SetOption(COLOR_SPACE_KEY, COLOR_SPACE_CIExyY) ==
                eNoError):
            print("Color space set to CIExyY.")
        else:
            print("Failed to set color space.")
            return
    
        # calibrate EyeOne Pro
        print("\nPlease put EyeOne-Pro on calibration plate and "
        + "press key to start calibration.")
        while(self.eyeone.I1_KeyPressed() != eNoError):
            time.sleep(0.01)
        if (self.eyeone.I1_Calibrate() == eNoError):
            print("Calibration of EyeOne Pro done.")
        else:
            print("Calibration of EyeOne Pro failed. Please RESTART.")
            return
    
        self.tri_stim = (c_float * TRISTIMULUS_SIZE)() # memory where EyeOne Pro
                                                          # saves tristim.
        self.spectrum = (c_float * SPECTRUM_SIZE)()    # memory where EyeOne Pro
                                                  # saves spectrum.
        # prompt for click on button of EyeOne Pro
        print("\nPlease put EyeOne-Pro in measurement position and hit"
        + " button to start measurement.")
        while(self.eyeone.I1_KeyPressed() != eNoError):
            time.sleep(0.01)
    
        print('\nInitializing search mode complete.')
    
    
    def adjustTube(self):
        """
        Enables up and down arrow to adjust tubes' color step by step (lower if
        down and higher if up).
        """
        key = self.key
        step = self.step
        colortube = self.colortube
        if colortube[0] == "all" and key == "up":
            self.voltages[0] = self.voltages[0] + step
            self.voltages[1] = self.voltages[1] + step
            self.voltages[2] = self.voltages[2] + step
        elif colortube[0] == "all" and key == "down":
            self.voltages[0] = self.voltages[0] - step
            self.voltages[1] = self.voltages[1] - step
            self.voltages[2] = self.voltages[2] - step
        elif not colortube[0] == "all" and key == "up":
            self.voltages[colortube[1]] = self.voltages[colortube[1]] + step
        elif not colortube[0] == "all" and key == "down":
            self.voltages[colortube[1]] = self.voltages[colortube[1]] - step
        else:
            pass
        self.tub.setVoltages(self.voltages)
        tellme(str(self.voltages), self.plot_xy)
        self.measureVoltage()


    def run(self):
        """
        Starts program to set tubes by hand.
        """
        self.tub.setVoltages(self.voltages)
        # open file to write data while manual search
        with open('./calibdata/measurements/measure_tubes_manual_' +
                time.strftime("%Y%m%d_%H%M") + '.txt', 'w') as self.calibfile:
            self.calibfile.write("volR, volG, volB, x, y, Y," +
                    ", ".join(["l" + str(x) for x in range(1,37)]) + "\n")
        
            #set figures
            print('\n\nWait until first measurement is done.')
            self.newFigure()
            print('\n\nManual adjustment of tubes` color\n\n' +
                  'Press [up] for higher intensity ' +
                  'or press [down] for lower intensity.\n' +
                  'To set tube color and step size press the following buttons:\n' +
                  'Stepsize:\n' + 
                  ' [1] - 1\n [2] - 5\n [3] - 10\n [4] - 50\n [5] - 100\n' +
                  'Colortube:\n [r] - Red\n [g] - Green\n [b] - Blue\n [a] - all'
                  + '\nPress "c" to redraw figure.'
                  + '\nPress escape to quit')
            self.stop=False
            while not self.stop:
                plt.waitforbuttonpress()
    
    def newFigure(self):
        if self.fig:
            plt.close(self.fig)
        self.fig = plt.figure(1)
        plt.clf()
        self.plot_xy = plt.subplot(1,2,1)
        self.plot_xy.axis([0.29, 0.31, 0.29, 0.31])
        self.plot_xy.plot(self.target_xyY[0], self.target_xyY[1], "rx")
        self.plot_xy.set_aspect(1)
        self.plot_Y = plt.subplot(1,2,2)
        self.plot_Y.axis([0, 10, 19, 23])
        self.plot_Y.axhline(y=self.target_xyY[2], color="r", xmin=0,
                xmax=1000)
        tellme('Get to the red cross', self.plot_xy)
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        # reset self.i
        self.i = 0
        # measure once to draw current point
        self.measureVoltage()
       
    
    def measureVoltage(self):
        xyY_list = list()
        self.i += 1
        for i in range(self.each):
            self.tub.setVoltages(self.voltages)
            #print(self.voltages)
            time.sleep(self.imi) # to give the EyeOne Pro time to adapt and to
                            # reduce carry-over effects
            if(self.eyeone.I1_TriggerMeasurement() != eNoError):
                print("Measurement failed for voltage %s ."
                        %str(self.voltages))
            if(self.eyeone.I1_GetTriStimulus(self.tri_stim, 0) != eNoError):
                print("Failed to get tristim for voltage %s ."
                        %str(self.voltages))
            if(self.eyeone.I1_GetSpectrum(self.spectrum, 0) != eNoError):
                print("Failed to get spectrum for voltage %s ."
                        %str(self.voltages))
    
            #write data
            self.calibfile.write(", ".join([str(x) for x in self.voltages]) +
                            ", " + ", ".join([str(x) for x in self.tri_stim]) +
                            ", " + ", ".join([str(x) for x in self.spectrum]) + 
                            "\n")
            self.calibfile.flush()
            xyY_list.append( self.tri_stim )
        x_mean = np.mean([x[0] for x in xyY_list])
        y_mean = np.mean([x[1] for x in xyY_list])
        Y_mean = np.mean([x[2] for x in xyY_list])
        print("xyY: " + str(x_mean) + "," + str(y_mean) + "," + str(Y_mean))
        self.plot_xy.plot(x_mean, y_mean, "bx")
        self.plot_Y.plot(self.i, Y_mean, "bx")
        plt.draw()
            
    
    def on_key_press(self, event):
        key = event.key
        self.key = key
        #print(key)
        if key == 'r' or key == 'g' or key == 'b' or key == 'a':
            self.colortube = setColorTube(key)
            tellme('Now change ' + self.colortube[0] + ' tubes.', self.plot_xy)
        elif key == '1' or key == '2' or key == '3' or key == '4' or key == '5':
            self.step = setStepSize(key)
            tellme('Step size set to ' + str(self.step), self.plot_xy)
        elif key == 'up' or key == 'down':
            self.adjustTube()
        elif key == 'c':
            # close and reprint figure
            self.newFigure()
        elif key == 'escape':
            self.stop = True


if __name__ == "__main__":
    man = SetTubesManual(voltages=(1162, 1755, 1614))
    man.run()
    
