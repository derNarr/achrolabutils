#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./showOneColor.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2011-05-01, DW

from achrolab.wasco.wasco import wasco, boardId
from achrolab.wasco.WascoConstants import DAOUT1_16, DAOUT2_16, DAOUT3_16
from psychopy import visual,event,core
from achrolab.monitor import Monitor
from achrolab.eyeone import EyeOne

eye_one = EyeOne.EyeOne()#dummy=True)
mywin = visual.Window(size=(1024,1536), monitor='mymon',
            color=(1,1,1), screen=0, colorSpace='rgb')
mon = Monitor(eye_one, mywin)

# ## background from Exp I (old lab, old graphics card)
# bg = 0.301960784314
# voltages = (1592, 2316, 2234)
# mon.setPatchStimColor(bg)
# 
# wasco.wasco_outportW(boardId, DAOUT3_16, voltages[0])
# wasco.wasco_outportW(boardId, DAOUT1_16, voltages[1])
# wasco.wasco_outportW(boardId, DAOUT2_16, voltages[2])
 
## create bitmaps
bg_list = range(720, 730)

for i in range(len(bg_list)):

    bg = bg_list[i]

    # background that just fills whole monitor with a certain color
    a_bg = repeat(bg, 2048*1536).reshape(1536, 2048)
    
    # transform numpy array so EIZO GS320 can display it in packed pixel modus
    np_bg = eizoGS320.encode_np_array(a_bg)
    # create image
    pil_bg = Image.fromarray(np_bg)
    # save image
    pil_bg.save("background" + str(i) + ".bmp")


# which color
id = 0

# set tubes (see find_color.R for details)
vol = [(1271, 1682, 1666),
       (1272, 1682, 1673),
       (1272, 1682, 1673),
       (1271, 1682, 1670),
       (1272, 1682, 1673),
       (1272, 1682, 1673),
       (1272, 1682, 1673),
       (1272, 1682, 1673),
       (1272, 1682, 1673),
       (1272, 1682, 1673)]

voltages = vol[id]

wasco.wasco_outportW(boardId, DAOUT3_16, voltages[0])
wasco.wasco_outportW(boardId, DAOUT1_16, voltages[1])
wasco.wasco_outportW(boardId, DAOUT2_16, voltages[2])

# show bitmaps
bg = visual.SimpleImageStim(mywin, "background" + str(id) + ".bmp", units="pix")
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
