#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./showOneColor.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2010-12-02, KS

from visionlab.wasco.wasco import wasco, boardId
from visionlab.wasco.WascoConstants import DAOUT1_16, DAOUT2_16, DAOUT3_16
from psychopy import visual,event,core
from visionlab.monitor2 import Monitor
from visionlab.EyeOne import EyeOne

eye_one = EyeOne.EyeOne()#dummy=True)
mywin = visual.Window(size=(2048,1536), monitor='mymon',
                color=(0,0,0), screen=1)
mon = Monitor(eye_one, mywin)
mon.setPatchStimColor(0.380392156863)

wasco.wasco_outportW(boardId, DAOUT1_16, 3778)
wasco.wasco_outportW(boardId, DAOUT2_16, 2331)
wasco.wasco_outportW(boardId, DAOUT3_16, 3252)

mouse = event.Mouse(mywin)
show = True 
while show:
    core.wait(0.01)
    left, middle, right = mouse.getPressed()
    if left: 
        core.wait(0.2)
        show=False
