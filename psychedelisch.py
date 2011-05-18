#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./psychedelisch.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2011-05-01, DW

from achrolab.devtubes import Tubes
import time 
from random import randint 

tubes = Tubes()

for i in range(1,200):
    color = (randint(0, 0xFFF), randint(0, 0xFFF), randint(0, 0xFFF))
    print("Farbe (rgb): " + str(color) + 
            "Zeit: " + time.strftime("%M:%S"))
    tubes.setVoltage( color )
    time.sleep(0.3)
    
tubes.setVoltage( (0,0,0) )

