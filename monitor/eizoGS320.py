#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# eizoGS320.py
#
# (c) 2010-2011 Konstantin Sering <konstantin.sering [aet] gmail.com> and
# Dominik Wabersich <dominik.wabersich [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# created 2012-05-21
# last mod 2012-05-21 22:08 DW
#

from exceptions import ValueError
import numpy as np
import pylab
import Image

def encode_color(grey_left, grey_right):
    """
    encodes the two grey values from two corresponding pixels in
    one color value.

    grey_left, grey_right must be integer between 0 and 1023 or castable to it.

    returns tuple of r,g,b as integer between 0 and 255.

    >>> encode_color(0, 0)
        (0, 0, 0)
    >>> encode_color(1020, 0)
        (0, 255, 0)
    """
    # store most significant bits of grey_left in green
    green = np.uint16(grey_left/4)
    # store most significant bits of grey_right in red
    red = np.uint16(grey_right/4)

    # store least significant two bits in correct blue bits
    # for left it has to be in the 5th and 6th bit
    # for right it has to be in the 1st and 2nd bit
    blue = np.uint16((grey_left % 4)*16 + (grey_right % 4)*1)

    return( (green, red, blue) )


def decode_color(color):
    """
    decodes the one color value from corresponding pixels in
    two grey values.

    color must be tuple of r,g,b as integer between 0 and 255.

    returns tuple of 2 integers between 0 and 1023.

    >>> decode_color((255,255,51))
        (1023.0, 1023.0)
    """
    red, green, blue = color
    # get most significant bits of grey_left from green channel
    grey_left = np.uint(green*4)
    # get most significant bits of grey_right from red channel
    grey_right = np.uint(red*4)

    # store blue bit 5 and 6 in grey_left bit 1 and 2
    grey_left = grey_left + (blue%32 - blue%16)/16 + (blue%64 - blue%32)/16 
    # store blue bit 1 and 2 in grey_right bit 1 and 2
    grey_right = grey_right + (blue%4)*1

    return( (grey_left, grey_right) )


def encode_np_array(np_array):
    """
    encodes two dimensional numpy array to arbitrary packed pixel format of the
    eizo GS320.

    np_array must be of shape NxM with an even number N. All values in this
    array must be castable to int and must be between 0 and 1023.

    returns three dimensional numpy array with shape NxM/2x3 and dtype=uint8
    """
    (N, M) = np_array.shape
    if not M%2 == 0:
        raise(ValueError, "first dimension of np_array must be even")
    M_new = M/2
    left = np_array[:,M_new:M]
    right = np_array[:,0:M_new]
    array_new = np.zeros((N, M_new, 3), dtype=np.uint8)

    greys = encode_color(left, right)

    for n in range(N):
        for m in range(M_new):
            for i in range(3):
                array_new[n,m,i] = greys[i][n,m]

    return array_new

def convert_to_eizo_picture(filename, outname):
    """
    converts picture with filename to picture with outname. The outname
    file kann be used with the EIZO GS320.
    """
    image = pylab.imread(filename)

    # imread gives values between 0 and 1
    # TODO convert to grey value from all three rgb values.
    image_grey = image[:,:,1]*1023

    image_eizo = encode_np_array(image_grey)

    pil_im = Image.fromarray(image_eizo)
    pil_im.save(outname)

