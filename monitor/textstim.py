#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# stim_midgrey.py
#
# (c) 2012 Dominik Wabersich <dominik.wabersich [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# created 2012-05-21
# last mod 2012-11-13 12:05 KS

"""
This module contains a class to create and present a text sitmulus with
psychopy for the Eizo GS320.

"""

from psychopy import visual
import eizoGS320

class TextStim(object):
    """
    Create and present a text on the Eizo GS320.

    """
    def __init__(self, win, text, pos=(0, 0), color=1023, bg_color=None, wrapWidth=1):
        """
        Paramters
        ---------
            win : psychopy.Window instance
                window in which the text is drawn
            text : string
                text that will be presented
            pos: (-1..1, -1...1)
                x and y position of the center of the text in norm units
            color : 0..1023
                grey value of text
            bg_color : None or 0..1023
                grey value for the bg_color, if None the bg_color of the
                window will be used.
            wrapWidth : 0..2
                width of the text in norm units

        """
        self.win = win
        if bg_color is None:
            bg_color = eizoGS320.decode_color((win.color[0],
                    win.color[1], win.color[2]))
        if bg_color[0] != bg_color[1]:
            print("WARNING: There is something wrong with the bg_color color")
        bg_color = bg_color[0]

        width_mon_half = int(win.size[0]/2)
        x_pos_left = width_mon_half * (1 + pos[0])
        x_pos_right = width_mon_half * (-1 + pos[0])
        y_pos = 0 + pos[1] * int(win.size[1]/2)

        self.stim_left = visual.TextStim(self.win, text, units="pix",
                pos=(x_pos_left, y_pos), colorSpace="rgb255",
                color=eizoGS320.encode_color(color, bg_color))
        self.stim_right = visual.TextStim(self.win, text, units="pix",
                pos=(x_pos_right, y_pos), colorSpace="rgb255",
                color=eizoGS320.encode_color(color, bg_color))

    def draw(self, win=None):
        """Draw the stimulus in its relevant window. You must call this
        method after every win.flip().
        """
        if win==None: win=self.win
        self.stim_left.draw(win)
        self.stim_right.draw(win)


if __name__ == '__main__':
    # small example, change screen to eizoGS320 to get the real stimuli
    from psychopy import event
    mywin = visual.Window([1024, 500], monitor="testMonitor",
                          color=(155, 155, 17), screen=0, colorSpace="rgb255",
                          allowGUI=False, units="pix")
    textstim = TextStim(mywin, u"""Ein schöner langer Text, der hoffentlich über mehrere Zeilen gebrochen wird. Und noch ein bisschen mehr Text als Instruktion für irgendein komisches, blah, blah, blah Experiment.""")
    textstim.draw()
    mywin.flip()
    event.waitKeys(keyList='escape')

