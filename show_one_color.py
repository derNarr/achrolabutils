#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./show_one_color.py
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: Show one calibrated color using bitmaps
#
# input: --
# output: --
#
# created
# last mod 2013-01-08 12:47 KS

import sys
sys.path.append("D:\\software\\achrolabutils")
sys.path.append("D:\\software")

from psychopy import visual, core, event

from achrolab.devtubes import DevTubes
from achrolab.monitor import Monitor
from achrolab.eyeone.eyeone import EyeOne
from numpy import repeat
from stimuli import eizoGS320
import Image

color = bg = 621
voltages = (1067, 1590, 1514)
# set tubes (see find_color.R for details)

tub = DevTubes()
eye_one = EyeOne()#dummy=True)
mywin = visual.Window(size=(1024, 1536), monitor='mymon',
            color=(1, 0, 0), screen=1, colorSpace='rgb')
mon = Monitor(mywin)

tub.setVoltages(voltages)

bg = visual.GratingStim(mywin, tex=None, mask=None, units="norm", pos=(0, 0),
                        size=(2, 2), color=eizoGS320.encode_color(color,
                            color), colorSpace="rgb255")
bg.draw()
mywin.flip()

mouse = event.Mouse(mywin)
show = True
while show:
    core.wait(0.01)
    left, middle, right = mouse.getPressed()
    if left:
        core.wait(0.2)
        show=False

