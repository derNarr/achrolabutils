#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# stim_midgrey.py
#
# (c) 2012 Dominik Wabersich <dominik.wabersich [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# created 2012-05-21
# last mod 2012-11-13 11:18 KS

"""This module contains a class to create and present an infield surround
stimulus with psychopy."""

from psychopy import visual
import eizoGS320

class SquareStim(object):
    def __init__(self, win, color, size, pos=(0,0)):
        """
        :Paramters:

            win: psychopy.Window instance
            color: 0..1023
                grey value for left infield
            size: 0...1024
                size of the grey square
            pos: (-512...512, -512...512)
                x and y position of the square

        """
        self.win = win
        background = eizoGS320.decode_color((win.color[0],
            win.color[1], win.color[2]))
        if not(background[0] == background[1]):
            print("WARNING: There is something wrong with the background color")
        background = background[0]

        width_mon_half = 512
        x_pos_left = width_mon_half  + pos[0]
        x_pos_right = -width_mon_half + pos[0]
        y_pos = 0 + pos[1]

        self.stim_l = visual.PatchStim(self.win, tex=None, units=win.units,
                pos=(x_pos_left, y_pos), size=size, colorSpace=win.colorSpace,
                color=eizoGS320.encode_color(color, background))
        self.stim_r = visual.PatchStim(self.win, tex=None, units=win.units,
                pos=(x_pos_right, y_pos), size=size, colorSpace=win.colorSpace,
                color=eizoGS320.encode_color(color, background))

    def draw(self, win=None):
        """Draw the stimulus in its relevant window. You must call this
        method after every win.flip().
        """
        if win==None: win=self.win
        self.stim_l.draw(win)
        self.stim_r.draw(win)


if __name__ == '__main__':
    # small example, change screen to eizoGS320 to get the real stimuli
    from psychopy import event
    mywin = visual.Window([1024, 500], monitor="testMonitor",
                          color=(155, 155, 17), screen=0, colorSpace="rgb255",
                          allowGUI=False, units="pix")
    teststim = SquareStim(mywin,color=500, size=80)
    teststim.draw()
    mywin.flip()
    event.waitKeys(keyList='escape')

