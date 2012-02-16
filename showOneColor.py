#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./showOneColor.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2011-05-01, DW

from achrolab.devtubes import DevTubes
from psychopy import visual,event,core
from achrolab.monitor import Monitor
from achrolab.eyeone import EyeOne
from numpy import *
import eizoGS320
import Image

tub = DevTubes()
eye_one = EyeOne.EyeOne()#dummy=True)
mywin = visual.Window(size=(1024,1536), monitor='mymon',
            color=(1,0,0), screen=0, colorSpace='rgb')
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

#print("Create Images\nThis can take some time...\n")
#bg_list = range(620, 622)
#
#for i in range(len(bg_list)):
#
#    bg = bg_list[i]
#
#    # background that just fills whole monitor with a certain color
#    a_bg = repeat(bg, 2048*1536).reshape(1536, 2048)
#    
#    # transform numpy array so EIZO GS320 can display it in packed pixel modus
#    np_bg = eizoGS320.encode_np_array(a_bg)
#    # create image
#    pil_bg = Image.fromarray(np_bg)
#    # save image
#    pil_bg.save("background" + str(i) + ".bmp")
#    print(".")
#print("Finished.\n")

# which color
id = 5

# set tubes (see find_color.R for details)
vol = [(1224, 1726, 1680), 
       (1191, 1678, 1637),
       (1192, 1678, 1636),
       (1193, 1673, 1637),
       (1194, 1673, 1636),
       (1162, 1755, 1614)]

voltages = vol[id]

tub.setVoltages(voltages)

# show bitmaps
#bg = visual.SimpleImageStim(mywin, "background" + str(id) + ".bmp", units="pix")
print("load image to psychopy\n")
bg = visual.SimpleImageStim(mywin, "background1.bmp", units="pix")
print("done.\n\nDraw now!\n")
bg.draw()
mywin.flip()

core.wait(60)

# mouse = event.Mouse(mywin)
# show = True 
# while show:
#     core.wait(0.01)
#     left, middle, right = mouse.getPressed()
#     if left: 
#         core.wait(0.2)
#         show=False
