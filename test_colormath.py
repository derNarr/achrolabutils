#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./test_colormath.py
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2010-12-02, KS

from achrolab.colormath.color_objects import SpectralColor, xyYColor,RGBColor

xyY = xyYColor(0.32, 0.32, 3.2)
print(xyY.convert_to("rgb", targetRGB="sRGB", clip=False))


