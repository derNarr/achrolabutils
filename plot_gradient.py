#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# plot_gradient.py
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content:
#
# input: --
# output: --
#
# created 2012-02-07 KS
# last mod 2012-02-07 KS

import numpy as np
import pylab


red = range(0, 256)
green = np.repeat(0, 256)
blue = np.repeat(0, 256)
alpha = np.repeat(255, 256)
colors = [(red[i], green[i], blue[i], alpha[i]) for i in range(len(red))]
image_red = np.repeat(np.array(colors, dtype=np.uint8, ndmin=3), 1034, 0)

red = np.repeat(0, 256)
green = range(0, 256)
blue = np.repeat(0, 256)
alpha = np.repeat(255, 256)
colors = [(red[i], green[i], blue[i], alpha[i]) for i in range(len(red))]
image_green = np.repeat(np.array(colors, dtype=np.uint8, ndmin=3), 1024, 0)

red = np.repeat(0, 256)
green = np.repeat(0, 256)
blue = range(0, 256)
alpha = np.repeat(255, 256)
colors = [(red[i], green[i], blue[i], alpha[i]) for i in range(len(red))]
image_blue = np.repeat(np.array(colors, dtype=np.uint8, ndmin=3), 1024, 0)

red = np.repeat(255, 256)
green = np.repeat(255, 256)
blue = np.repeat(255, 256)
alpha = range(0, 256)
colors = [(red[i], green[i], blue[i], alpha[i]) for i in range(len(red))]
image_alpha = np.repeat(np.array(colors, dtype=np.uint8, ndmin=3), 1024, 0)

pylab.figure(4, figsize=(10, 5))
pylab.clf()

pylab.subplot(1, 4, 1)
pylab.imshow(image_red)
pylab.subplot(1, 4, 2)
pylab.imshow(image_green)
pylab.subplot(1, 4, 3)
pylab.imshow(image_blue)
pylab.subplot(1, 4, 4, axisbg=(0, 0, 0))
pylab.imshow(image_alpha)
pylab.show()

