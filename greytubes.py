#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./colortable.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2010-12-02, KS

from visionlab.tubes2 import Tubes
from EyeOne import EyeOne

eyeone = EyeOne.EyeOne()
tubes = Tubes(eyeone)

xyY_list = []
voltages = []
tubes.startMeasurement()
for i in range(0,50):
    print("measure voltages: " + str(0x800+40*i))
    xyY_list.append( 
            tubes.measureVoltages( (0x800+40*i, 0x800+40*i, 0x800+40*i) ) )
    voltages.append( 0x800+40*1)

# flat xyY_list
xyY_list = [x[0] for x in xyY_list]

# save to file
f = open("greytubes.txt", "w")
for i in range(0,50):
    f.write(str(voltages[i]))
    for x in xyY_list[i]:
        f.write(", "+str(x))
    f.write("\n")
f.close()



