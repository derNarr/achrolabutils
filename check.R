#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./check.R
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2010-12-09, KS


setwd("C:/Dokumente und Einstellungen/user1/Desktop/visionlabutils/visionlab/data/")

dat <- read.csv("color_table_20101209_1220.csv", na.strings="NA", colClasses=c("character", rep("numeric", 16)))
dat2 <- dat[171:180,]
datTuned <- read.csv("color_table_20101210_1402.csv", na.strings="NA", colClasses=c("character", rep("numeric", 16)))
datTuned2 <- datTuned[171:180,]

# Y uebersicht
with(dat, plot(monitor_xyY_Y))
with(dat, points(tubes_xyY_Y, col="blue"))
with(datTuned, points(tubes_xyY_Y, col="red"))
X11()
# x vs y uebersicht
with(dat, plot(monitor_xyY_x, monitor_xyY_y, xlim=c(0.20,0.40), ylim=c(0.20,0.40)))
with(dat, points(tubes_xyY_x, tubes_xyY_y, col="blue"))


# Y
with(dat2, plot(monitor_xyY_Y, ylim=c(16,26)))
with(dat2, points(tubes_xyY_Y, col="blue"))
with(datTuned2, points(tubes_xyY_Y, col="red"))
X11()
# x vs y
with(dat2, plot(monitor_xyY_x, monitor_xyY_y, xlim=c(0.29,0.31), ylim=c(0.31,0.33)))
with(dat2, points(tubes_xyY_x, tubes_xyY_y, col="blue"))
with(datTuned2, points(tubes_xyY_x, tubes_xyY_y, col="red"))

