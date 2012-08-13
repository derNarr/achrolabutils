# (c) 2010 James McMurray, Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)

""" singrating.py :
Produces a sin-wave based stimuli across the screen, which is then shifted to anti-phase and re-presented rapidly.

TUB notes:
 Two stimuli, superimposed mean luminance is equal to background. At high enough frequencies, the stimuli should be invisible. The photometer will probably be fine with this, but if one's eyes are moving too much, it will look terrible. Look through a tube and the effect will probably go away. Anyway, the point is, is that this is a great test for frame dropping.
"""
if __name__=='__main__':
    #Oft-changed constants here:
    usingeizo=False
    measuring=False #Measuring unimplemented here, spectrometer too slow
    patchsize=0.5 #Size relative to window - i.e. whole monitor
    waittime=0.01 #Perhaps change this to more accurate frame-basis
    calibrate = True
    prefix="cdata"
    centralstimgray=511
    highgray=1023
    lowgray=0

    import numpy as np
    import pylab
    import math
    import matplotlib.pyplot as ppl
    import time
    import eizoGS320

    from ctypes import c_float

    from contextlib import closing
    from psychopy import visual
    from psychopy import core
    from psychopy import event
    #Program sin grating array
    # sarray=np.ones((1536,2048), dtype=np.uint16)
    # sarray*=512
    # i=0
    # while i<2048:
    #     sarray[748:788, i]=(512*math.sin((((2*math.pi)/(2048.))*i) +0.00001)) +512
    #     i+=1
    #ppl.imshow(sarray)

    #imageiron=self.axis5.imshow(self.ironconcmatrixindgen, cmap=self.cmap, vmin=self.ironmin, vmax=self.ironmax)

    #np.savetxt('myfile.txt', sarray, fmt="%12.6G")


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

    # import Image
    # #newarray=eizoGS320.encode_np_array(sarray)
    # # # ppl.imshow(newarray)
    # # # pylab.show()

    # pil_im = Image.fromarray(sarray)
    # pil_im.save("zerophasenc.png")

    # ###

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
    mywin = visual.Window(monitorsize, monitor="mymon", color=eizoGS320.encode_color(0,0), screen=monitornum, colorSpace="rgb255", allowGUI=False, units="pix")

    #bgstim=visual.PatchStim(mywin, tex=None, units='norm', pos=(0, 0), size=2, colorSpace=mywin.colorSpace, color=eizoGS320.encode_color(0, 0))
    #centralstim=visual.PatchStim(mywin, tex=None, units='norm', pos=(0, 0), size=patchsize, colorSpace=mywin.colorSpace, color=eizoGS320.encode_color(centralstimgray, centralstimgray))
    phase0=visual.SimpleImageStim(mywin, image='xsin0.png', units='norm', pos=(0.0, 0.0), contrast=1.0, opacity=1.0, flipHoriz=False, flipVert=False, name='phase0', autoLog=True)

    phase180=visual.SimpleImageStim(mywin, image='xsin180.png', units='norm', pos=(0.0, 0.0), contrast=1.0, opacity=1.0, flipHoriz=False, flipVert=False, name='phase180', autoLog=True)

    #Allow change stimulus size, etc. easily - use globals or arguments
    phase0.draw()
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

            if n%2 == 0:
                phase0.draw()
                print 'phase0'
            else:
                phase180.draw()
                print 'phase0'
            n+=1
            n = n % 2
            #print n
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
