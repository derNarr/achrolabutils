#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# demo_control_knobs.py
#
# (c) 2013 Konstantin Sering <konstantin.sering [aet] gmail.com>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content:
#
# input: --
# output: --
#
# created 2013-01-08 KS
# last mod 2013-01-08 14:47 KS

"""
Demo for the control knobs.

"""

import time
from ctypes import c_ulong, byref

from achrolab import wasco

wasco_card = wasco.Wasco()
boardId = wasco_card.boardId

all_ = c_ulong(0)
red = c_ulong(0)
green = c_ulong(0)
blue = c_ulong(0)

while True:
    wasco_card.wasco_readAnalogInp(boardId, None, 63, byref(all_), 0)
    wasco_card.wasco_readAnalogInp(boardId, None, 62, byref(red), 0)
    wasco_card.wasco_readAnalogInp(boardId, None, 61, byref(green), 0)
    wasco_card.wasco_readAnalogInp(boardId, None, 60, byref(blue), 0)
    print("all: %i" % all_)
    print("red: %i" % red)
    print("green: %i" % green)
    print("blue: %i" % blue)
    time.sleep(0.2)

