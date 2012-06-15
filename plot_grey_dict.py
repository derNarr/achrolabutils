#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# plot_grey_dict.py
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

from grey_dict import grey_dict

image = np.repeat(np.array(grey_dict.values(), ndmin=3), 1024, 0)

image = np.uint8(image)

pylab.imshow(image)
pylab.show()

