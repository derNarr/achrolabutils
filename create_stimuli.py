# create_stimuli.py
#
# This script creates infield/surround stimuli for same/different
# experiments as bitmap files that can be presented on EIZO GS320 with
# 10 bits.


from numpy import *
import eizoGS320

from psychopy import visual
import Image


bg = 850

# background that just fills whole monitor with a certain color
a_bg = repeat(bg, 2048*1536).reshape(1536, 2048)

cross = 700
inf1 = 200
sur1 = 650
inf2 = 300
sur2 = 550

size_inf = 80    # about 1deg, ca. 2cm
size_sur = 190   # about 8deg, ca. 5cm
size_diff = 40
size_bg = (2048 - 2*size_sur - size_diff)/2     # 824px

# infield/surround configurations
a_stim = array([repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),

    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff/2-1, 2, size_diff/2-1, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff/2-1, 2, size_diff/2-1, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff/2-1, 2, size_diff/2-1, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff/2-1, 2, size_diff/2-1, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff/2-5, 10, size_diff/2-5, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff/2-5, 10, size_diff/2-5, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff/2-1, 2, size_diff/2-1, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff/2-1, 2, size_diff/2-1, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff/2-1, 2, size_diff/2-1, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff/2-1, 2, size_diff/2-1, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),
    repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg], [size_bg, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2, size_bg]),

    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg]),
    repeat([bg, sur1, bg, sur2, bg],[size_bg, size_sur, size_diff, size_sur, size_bg])])


# check if stimuli have the correct size
print(a_bg.shape)       # should be (1536, 2048)
print(a_stim.shape)     # should be (size_sur, 2048)

# transform numpy array so EIZO GS320 can display it in packed pixel modus
np_bg = eizoGS320.encode_np_array(a_bg)
np_stim = eizoGS320.encode_np_array(a_stim)

# create image
pil_bg = Image.fromarray(np_bg)
pil_stim = Image.fromarray(np_stim)

# save image
pil_bg.save("background.bmp")
pil_stim.save("stim.bmp")

