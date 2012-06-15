#!/usr/bin/env Rscript
# -*- encoding: utf-8 -*-
# ./stimulus_size.R
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: (1) visual angle to cm
#          (2) cm to pixel
#          (3) compute stimulus sizes
#
# input: --
# output: --
#
# created
#
# last mod 2012-02-22, NU

###### (1) visual angle to cm ######
vis2cm <- function(alpha, r=120){
    cm <- 2*r*tan(alpha/2 * pi/180)
    cm
    }

cm2vis <- function(cm, r=120){
    vis <- 2*atan(0.5*cm/r) * 180/pi
    vis
    }

###### (2) cm to pixel ######

# one pixel of EIZO GS320 has the size: 0.2115mm (see Manual)
cm2pix <- function(cm){
    pix <- cm/0.02115
    pix
    }

pix2cm <- function(pix){
    cm <- 0.02115*pix
    cm
    }

###### (3) compute stimulus sizes ######

cm2pix(vis2cm(1))       # 99.02829
cm2pix(vis2cm(8))       # 793.4957

# current setting
cm2vis(pix2cm(80))      # 0.8078571
cm2vis(pix2cm(190))     # 1.918513

# table for looking it up
dat <- data.frame(visual = round(seq(.5, 20, .5),1), cm =
    round(vis2cm(seq(.5, 20, .5)),2), pixel = round(cm2pix(vis2cm(seq(0.5,
    20, .5))),0))


