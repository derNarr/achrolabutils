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

from __future__ import print_function

import time

from achrolab.wasco import wasco
from achrolab.wasco.constants import (AD_ADCONT, AD_ADDAT, AD_ADRANGE,
        AD_ADSTAT, AD_STARTCH, AD_SWTRIG, DAOUT1, RESETERRORFLAG,
        RESETFIFO)

wasco_card = wasco.Wasco()
boardId = wasco_card.boardId

wasco_card.wasco_outportW(boardId, AD_ADCONT, 0x91) # A/D-Modus:
                                                    # Softwareauslösung
wasco_card.wasco_outportW(boardId, AD_ADCONT, 0xB1) # PGA-Ansteuerung über
                                                    # Register AD_ADRANGE

# MUX-Ansteuerung über Register AD_ADSTARTCH
wasco_card.wasco_outportW(boardId, AD_ADRANGE, 0x1) # VPGA = 2, single ended
                                                    # vgl Seite 34 im
                                                    # Manual
wasco_card.wasco_outportW(boardId, RESETERRORFLAG, 0x0)
wasco_card.wasco_outportW(boardId, RESETFIFO, 0x0)
wasco_card.wasco_outportW(boardId, DAOUT1, 0x820)

while True:
    # break with <ctrl>-c
    for chnr in range(60, 64): # trigger channel 60-63
          wasco_card.wasco_outportW(boardId, AD_STARTCH, chnr)
          time.sleep(0.001)
          wasco_card.wasco_outportW(boardId, AD_SWTRIG, 0x0)
          time.sleep(0.001)

    for mwnr in range(60, 64):
        status = wasco_card.wasco_inportW(boardId, AD_ADSTAT) # check A/D-Status-Register
        if status:
            mw = wasco_card.wasco_inportW(boardId, AD_ADDAT) # read A/D-Wert
            print("Kanal: %02d  %4x Hex  %4.4f Volt\t" % (mwnr,mw,-10 + mw
                * 0.004882812), end="")
            time.sleep(0.005)
        else:
            print(("\nA/D-Statusregister: %x") % status)
    print("\n\n")
    time.sleep(0.200)

