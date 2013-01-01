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
# last mod 2013-01-01 12:37 KS

from psychopy import visual, core, event

from achrolab.devtubes import DevTubes
from achrolab.monitor import Monitor
from achrolab.eyeone.eyeone import EyeOne
from numpy import repeat
from stimuli import eizoGS320
import Image

tub = DevTubes()
eye_one = EyeOne()#dummy=True)
mywin = visual.Window(size=(1024, 1536), monitor='mymon',
            color=(1, 0, 0), screen=1, colorSpace='rgb')
mon = Monitor(mywin)

# ## background from Exp I (old lab, old graphics card)
# bg = 0.301960784314
# voltages = (1592, 2316, 2234)
# mon.setPatchStimColor(bg)
#
# wasco.wasco_outportW(boardId, DAOUT3_16, voltages[0])
# wasco.wasco_outportW(boardId, DAOUT1_16, voltages[1])
# wasco.wasco_outportW(boardId, DAOUT2_16, voltages[2])

## create bitmaps

print("Create Images\nThis can take some time...\n")
color = bg = 600

# background that just fills whole monitor with a certain color
a_bg = repeat(bg, 2048*1536).reshape(1536, 2048)

# transform numpy array so EIZO GS320 can display it in packed pixel modus
np_bg = eizoGS320.encode_np_array(a_bg)
# create image
pil_bg = Image.fromarray(np_bg)
# save image
pil_bg.save("same.bmp")
print(".")
print("Finished.\n")

# set tubes (see find_color.R for details)
voltages = (1060, 1512, 1496)
#voltages = (1060/2+0x7FF, 1512/2+0x7FF, 1496/2+0x7FF)
#voltages = (4000, 0x800, 0x800)

tub.setVoltages(voltages)

# show bitmaps
# bg = visual.SimpleImageStim(mywin, "background" + str(id) + ".bmp",
# units="pix")
#print("load image to psychopy\n")
#bg = visual.SimpleImageStim(mywin, "same.bmp", units="pix")
#print("done.\n\nDraw now!\n")

bg = visual.GratingStim(mywin, tex=None, mask=None, units="norm", pos=(0, 0),
                        size=(2, 2), color=eizoGS320.encode_color(color),
                        colorSpace="rgb255")
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

