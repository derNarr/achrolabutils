# (c) 2010 James McMurray, Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)

""" gamma.py :
Compare luminance of big patch and small patch, on CRT big patch should always be less bright. Can use up and down arrow keys to modify the size of the patch whilst running.
"""
if __name__=='__main__':
    #Oft-changed constants here:
    usingeizo=False
    measuring=False
    patchsize=0.5 #Size relative to window - i.e. whole monitor
    waittime=0.001 #Perhaps change this to more accurate frame-b
    calibrate = True
    prefix="cdata"
    centralstimgray=511
    highgray=1023

    if usingeizo==False:
        #Testing stuff
        import sys
        sys.path.append("/home/jamesmcm/git/achrolabutils/")
        sys.path.append("/home/jamesmcm/git/achrolabutils/achrolab/")
        import os
        os.chdir("/home/jamesmcm/git/achrolabutils")
        #End testing
        monitorsize=[1024,768]
        monitornum=0
        from achrolab.printing import CalibDataFile
        from achrolab.eyeone import EyeOne, EyeOneConstants
        EyeOne = EyeOne.EyeOne(dummy=True) # EyeOne Object
    else:
        from printing import CalibDataFile
        monitorsize=[1024, 1536]
        monitornum=1
        from achrolab.eyeone import eyeone, EyeOneConstants
        EyeOne = eyeone.EyeOne(dummy=False) # EyeOne Object

    import time

    from ctypes import c_float

    from contextlib import closing
    from psychopy import visual
    from psychopy import core
    from psychopy import event
    import eizoGS320
    import math

    ###




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


    #set monitor color

    #For eizo: 1024x1536, screen 1
    mywin = visual.Window(monitorsize, monitor="mymon", color=eizoGS320.encode_color(centralstimgray,centralstimgray), winType="pygame", screen=monitornum, colorSpace="rgb255", allowGUI=False, units="pix")


    centralstim=visual.PatchStim(mywin, tex=None, units='norm', pos=(0, 0), size=patchsize, colorSpace=mywin.colorSpace, color=eizoGS320.encode_color(highgray, highgray))
    #Allow change stimulus size, etc. easily - use globals or arguments
    centralstim.draw()
    mywin.flip()

    if measuring==True:
        if (calibrate or (EyeOne.I1_TriggerMeasurement() ==  EyeOneConstants.eDeviceNotCalibrated)):
            # Calibration of EyeOne
            print("\nPlease put EyeOne Pro on calibration plate and press \n key to start calibration.")
            while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
                time.sleep(0.1)
            if (EyeOne.I1_Calibrate() == EyeOneConstants.eNoError):
                print("Calibration done.")
            else:
                print("Calibration failed.")
                print("\nPlease put EyeOne Pro in measurement position and press \n key to start measurement.")

            while(EyeOne.I1_KeyPressed() != EyeOneConstants.eNoError):
                time.sleep(0.1)

    running=True
    #freq=0.015 #This affects how big the steps are we sample in the sin function
    n=0

    with closing(CalibDataFile(prefix=prefix)) as datafile:
        while running:
            keys=event.getKeys()
            for thiskey in keys:
                if thiskey in ['q', 'escape']:
                    running=False
                    break
                if thiskey in ['up']:
                    patchsize+=0.1
                    centralstim.setSize(patchsize, units='norm')
                if thiskey in ['down']:
                    patchsize-=0.1
                    centralstim.setSize(patchsize, units='norm')

            #color = [x/128.-1 for x in color]
            #mywin.setColor(color, 'rgb255')
            centralstim.draw()
            mywin.flip()
            if measuring==True:
                if(EyeOne.I1_TriggerMeasurement() != EyeOneConstants.eNoError):
                    print("Measurement failed.")
                # retrieve Color Space
                if(EyeOne.I1_GetTriStimulus(colorspace, 0) != EyeOneConstants.eNoError):
                    print("Failed to get color space.")
                else:
                    print("Color Space " + str(colorspace[:]) + "\n")
                    color_list.append(colorspace[:])
                    #datafile.writeDataTXT(grayvals=[graystim, centralstimgray], rgb=None, xyY=colorspace, voltage=None, spec_list=None, delimiter="\t")
            time.sleep(waittime)
