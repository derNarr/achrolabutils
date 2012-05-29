#!/usr/bin/env Rscript
# -*- encoding: utf-8 -*-
# ./create_stimuli.py
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: This script creates infield/surround stimuli for same/different
# experiments as bitmap files that can be presented on EIZO GS320 with 10 bits.
#
# input: --
# output: --
#
# created
# last mod 2010-12-09, KS

from numpy import repeat
import eizoGS320

import Image


bg = 621
 
# # background that just fills whole monitor with a certain color
# a_bg = repeat(bg, 2048*1536).reshape(1536, 2048)
# 
# # transform numpy array so EIZO GS320 can display it in packed pixel modus
# np_bg = eizoGS320.encode_np_array(a_bg)
# # create image
# pil_bg = Image.fromarray(np_bg)
# # save image
# #pil_bg.save("background.bmp")
# pil_bg.save("background.png")


## --> colors between 360 and 445 rgb(90:110, 90:100, xx)

cross = 600
stim_inf1  = (374, 380, 386, 392, 398, 404, 410, 416, 422, 428)
stim_sur1  = 621
stim_inf2  = (374, 380, 386, 392, 398, 404, 410, 416, 422, 428)
stim_sur2  = 621

size_inf  = 80    # about 1deg, ca. 2cm
size_sur  = 190   # about 8deg, ca. 5cm
size_diff = 40
size_bg   = (2048 - 2*size_sur - size_diff)/2     # 824px

for i in range(len(stim_inf1)):
    for j in range(len(stim_inf2)):

        inf1 = stim_inf1[i]
        inf2 = stim_inf2[j]
        sur1 = stim_sur1
        sur2 = stim_sur2

        # infield/surround configurations
        line1 = repeat([bg, sur1, bg, sur2, bg], [size_bg, size_sur,
                size_diff, size_sur, size_bg])
        line2 = repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg],
                [size_bg, (size_sur-size_inf)/2, size_inf,
                (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2,
                size_inf, (size_sur-size_inf)/2, size_bg])
        line3 = repeat([bg, sur1, inf1, sur1, bg, cross, bg, sur2, inf2, sur2,
                bg], [size_bg, (size_sur-size_inf)/2, size_inf,
                (size_sur-size_inf)/2, size_diff/2-1, 2, size_diff/2-1,
                (size_sur-size_inf)/2, size_inf, (size_sur-size_inf)/2,
                size_bg])
        line4 = repeat([bg, sur1, inf1, sur1, bg, sur2, inf2, sur2, bg],
                [size_bg, (size_sur-size_inf)/2, size_inf,
                (size_sur-size_inf)/2, size_diff, (size_sur-size_inf)/2,
                size_inf, (size_sur-size_inf)/2, size_bg])
        line5 = repeat([bg, sur1, bg, sur2, bg], [size_bg, size_sur,
                size_diff, size_sur, size_bg])

        # create image array out of the 5 "image-lines"
        a_stim = repeat([line1, line2, line3, line4, line5], [55, 35, 10,
                 35, 55], axis=0)
        
        # check if stimuli have the correct size
        # print(a_bg.shape)       # should be (1536, 2048)
        print(a_stim.shape)     # should be (size_sur, 2048)

        # transform numpy array so EIZO GS320 can display it in packed
        # pixel modus
        np_stim = eizoGS320.encode_np_array(a_stim)
        
        # create image
        pil_stim = Image.fromarray(np_stim)
        
        # save image
        #pil_stim.save("stim" + str(i) + ".bmp")
        pil_stim.save("stim" + str(i) + str(j) + ".png")
        
