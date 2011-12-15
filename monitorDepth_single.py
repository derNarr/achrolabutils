#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# monitorDepth_single.py
#
# (c) 2011 Dominik Wabersich <dominik.wabersich [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# created 2011-11-21
# last mod 2011-11-21 DW
#
from monitorDepth import getDepth
from psychopy import visual

if(__name__=="__main__"):

    #patch_stim_value_list = [x/127.5 - 1 for x in range(120,130)]
    #patch_stim_rgb = (122,123,124)
    patch_stim_rgb = list()
    g=0
    b=0
    for r in range(100,150):
        patch_stim_rgb.append( (r,g,b) )
    r=0
    b=0
    for g in range(100,150):
        patch_stim_rgb.append( (r,g,b) )
    r=0
    g=0
    for b in range(100,150):
        patch_stim_rgb.append( (r,g,b) )

    mywin = visual.Window(size=(2048,1536), monitor='mymon',
                color=(1,1,1), screen=1, colorSpace='rgb')

    getDepth(patch_stim_rgb, imi=0.5, screen=1, colorSpace='rgb255')
    
