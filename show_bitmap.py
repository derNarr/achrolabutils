#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./show_bitmap.py
#
# (c) 2012 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2012-02-10, KS

from psychopy import visual, core



mywin = visual.Window(size=(1024,1536), monitor='mymon',
            color=(155,155,17), screen=1, colorSpace='rgb255')

#bitmap = visual.SimpleImageStim(mywin, "all_grey_eizo.bmp", units="pix")

#bitmap.draw()
#mywin.flip()

bg = visual.SimpleImageStim(mywin,
"Z:\\AG_Heller\\experiments\\same_different\\exp_II\\stimuli\\stim_0_7.png", units="pix")
#stim = visual.SimpleImageStim(mywin, "stim0.png", units="pix")

# build up a composite or large visual background (slow, do once):
bg.draw()
#stim.draw()

# capture everything (one time):
#screenshot = visual.BufferImageStim(mywin)

# render to screen (fast, do many times):
#screenshot.draw()  # fast; can change orientation (.ori) or x,y location (._position)
mywin.flip()

core.wait(30.0)


