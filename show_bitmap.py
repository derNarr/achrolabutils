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
            color=(1,1,1), screen=1, colorSpace='rgb')

bitmap = visual.SimpleImageStim(mywin, "all_grey_eizo.bmp", units="pix")

bitmap.draw()
mywin.flip()

core.wait(30.0)


