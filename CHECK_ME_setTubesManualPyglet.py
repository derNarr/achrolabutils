#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./setTubesManualPyglet.py
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
# created
# last mod 2011-10-17 KS

import pyglet

from psychopy import visual
from achrolab.devtubes import DevTubes

tub = DevTubes()

win = pyglet.window.Window()

voltages = list( (1200,1200,1200) )

# Variables are pre-defined to avoid Errors, can be changed in the program l8ter
colortube = ('red', 0)
step = 10

def getKey(symbol):
    """
    Returns key for certain symbol codes.
    """
    if symbol == 114:
        key = 'r'
    elif symbol == 103:
        key = 'g'
    elif symbol == 98:
        key = 'b'
    elif symbol == 49:
        key = '1'
    elif symbol == 50:
        key = '2'
    elif symbol == 51:
        key = '3'
    elif symbol == 52:
        key = '4'
    elif symbol == 53:
        key = '5'
    elif symbol == 65362:
        key = 'arrowup'
    elif symbol == 65364:
        key = 'arrowdown'
    else:
        key = 'ERROR'
    return key

def setColorTube(key):
    """
    Defines which color tubes should be changed.
    """
    if key == 'r':
        return ('red', 0)
    elif key == 'g':
        return ('green', 1)
    elif key == 'b':
        return ('blue', 2)
    else:
        pass

def setStepSize(key):
    """
    Defines step size of change.
    """
    if key == '1':
        return 1
    elif key == '2':
        return 10
    elif key == '3':
        return 50
    elif key == '4':
        return 200
    elif key == '5':
        return 500
    else:
        pass
    
def adjustTube(key, tubes, voltages, colortube, step):
    """
    Enables up and down arrow to adjust tubes' color step by step (lower if
    down and higher if up).
    """
    if key == 'arrowup':
        voltages[colortube[1]] = voltages[colortube[1]] + step
        tubes.setVoltages(voltages)
        print('Adjusted ' + colortube[0] + ' colortube voltage higher by ' + str(step))
    elif key == 'arrowdown':
        voltages[colortube[1]] = voltages[colortube[1]] - step
        tubes.setVoltages(voltages)
        print('Adjusted ' + colortube[0] + ' colortube voltage lower by ' + str(step))
    else:
        pass

def setTubesManual(startvoltages):
    """
    Starts program to set tubes by hand.
    """
    print('Manual adjustment of tubes` color\n\n' +
          'Press [arrowup] for higher intensity ' +
          'or press [arrowdown] for lower intensity.\n' +
          'To set tube color and step size press the following buttons:\n' +
          'Stepsize:\n [1] - 1\n [2] - 10\n [3] - 50\n [4] - 200\n [5] - 500' +
          'Colortube:\n [R] - Red\n [G] - Green\n [B] - Blue')
    tub.setVoltages(startvoltages)
    pyglet.app.run()

@win.event
def on_key_press(symbol, modifiers):
    
    # print(symbol)
    global step
    global colortube
    key = getKey(symbol)
    print(key)
    if key == 'r' or key == 'g' or key == 'b':
        colortube = setColorTube(key)
        print('Colortube ' + colortube[0] + ' ready for adjustment.')
    elif key == '1' or key == '2' or key == '3' or key == '4' or key == '5':
        step = setStepSize(key)
        print('Step size set to ' + str(step))
    else:
        adjustTube(key, tub, voltages, colortube, step)
            
if __name__ == "__main__":

    setTubesManual(voltages)
    
