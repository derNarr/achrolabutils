#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./check.R
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2010-12-02, KS


setwd("C:\\Dokumente und Einstellungen\\user1\\Desktop\\visionlab_neu_20101122")

dat <- read.csv("color_table_20101123_2024.csv")

# Y
plot(dat$monitor_xyY_Y)
points(dat$tubes_xyY_Y, col="blue")

# x vs y
plot(dat$tubes_xyY_x, dat$tubes_xyY_y, col="blue")
points(dat$monitor_xyY_x, dat$monitor_xyY_y)

