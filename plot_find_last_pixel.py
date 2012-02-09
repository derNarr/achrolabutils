#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# plot_find_last_pixel.py
#
# (c) 2012 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# created 2012-02-07 KS
# last mod 2012-02-07 KS
#

import numpy as np
import pylab

red = range(0,256)
green = np.repeat(0, 256)
blue = np.repeat(0, 256)
alpha = np.repeat(255, 256)
colors = [(red[i], green[i], blue[i], alpha[i]) for i in range(len(red))]
image_red_top = np.repeat(np.array(colors, dtype=np.uint8, ndmin=3), 128, 0)

image_red = list()

for bit in (1,2,4,8,16,32,64,128):
    blue = np.repeat(bit, 256)
    colors = [(red[i], green[i], blue[i], alpha[i]) for i in range(len(red))]
    image_red_bot = np.repeat(np.array(colors, dtype=np.uint8, ndmin=3), 128, 0)
    
    image_red.append( np.concatenate( (image_red_top, image_red_bot) ) )


pylab.figure(len(image_red), figsize=(5*len(image_red),5))
pylab.clf()

for i in range(len(image_red)):
    pylab.subplot(1, 8, i)
    pylab.imshow(image_red[i])

pylab.show()

