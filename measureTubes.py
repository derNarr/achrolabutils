#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./calibrate.py
#
# (c) 2010-2011 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2012-02-08 KS

from achrolab.eyeone import EyeOne
from achrolab.tubes import CalibTubes

eyeone = EyeOne.EyeOne()
tub = CalibTubes(eyeone, calibfile="./calibdata/lastParameterTubes.pkl")

#tub.calibrateEyeOne()
#tub.startMeasurement()
#tub.measureVoltages()

tub.calibrate(n=100, each=5)

