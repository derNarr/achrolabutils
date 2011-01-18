#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./check.R
#
# (c) 2010 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2010-12-09, KS


setwd("C:/Dokumente und Einstellungen/user1/Desktop/visionlabutils/visionlab/data/")
#setwd("/home/kfs-studium/Dokumente/arbeit/PI/visionlabutils/visionlab/data/")

dat <- read.csv("color_table_20101209_1220.csv", na.strings="NA", colClasses=c("character", rep("numeric", 16)))
dat2 <- dat[175:177,]
datTuned <- read.csv("color_table_20110115_1306.csv", na.strings="NA", colClasses=c("character", rep("numeric", 16)))
datTuned2 <- datTuned[175:177,]


setwd("C:/Dokumente und Einstellungen/user1/Desktop/visionlabutils/visionlab/tune/")

files <- dir()

it <- NULL

for (file in files) {
    tmp <- unlist(strsplit(file, "_"))
    tmp2 <- read.csv(file, header=T)
    tmp2$target <- tmp[2]
    tmp2$iteration <- unlist(strsplit(tmp[3], "n"))[2]
    tmp2$channel <- substr(tmp[4], 3, 3)
    it <- rbind(it, tmp2)
    }
it$target <- as.factor(it$target)
it$iteration <- as.factor(it$iteration)
it$channel <- as.factor(it$channel)

# x vs y
X11()
plot(dat$monitor_xyY_x[171], dat$monitor_xyY_y[171], pch="x",
xlim=c(0.26,0.31), ylim=c(0.25,0.33))

for (iter in levels(it$iteration)) {
    for (ch in levels(it$channel)) {
        rgb <- NULL
        if( ch == "R" ) {rgb="red"}
        if( ch == "G" ) {rgb="green"}
        if( ch == "B" ) {rgb="blue"}
        with(it[it$iteration==iter & it$channel==ch,],
            points(xyY_x, xyY_y, type="l", col=rgb))
    }
    text(it[it$iteration==iter,]$xyY_x[1],
    it[it$iteration==iter,]$xyY_y[1], iter)
}


# x vs Y
X11()
plot(dat$monitor_xyY_x[171], dat$monitor_xyY_Y[171], pch="x",
xlim=c(0.26,0.31), ylim=c(10,20))

for (iter in levels(it$iteration)) {
    for (ch in levels(it$channel)) {
        rgb <- NULL
        if( ch == "R" ) {rgb="red"}
        if( ch == "G" ) {rgb="green"}
        if( ch == "B" ) {rgb="blue"}
        with(it[it$iteration==iter & it$channel==ch,],
            points(xyY_x, xyY_Y, type="l", col=rgb))
    }
    text(it[it$iteration==iter,]$xyY_x[1],
    it[it$iteration==iter,]$xyY_Y[1], iter)
}

##########################################################################
### VOLTAGES #############################################################
##########################################################################

# r vs g
X11()
plot(dat$voltages_r[171], dat$voltages_g[171], pch="s",
xlim=c(0x400,0xFFF), ylim=c(0x400,0xFFF))

for (iter in levels(it$iteration)) {
    for (ch in levels(it$channel)) {
        rgb <- NULL
        if( ch == "R" ) {rgb="red"}
        if( ch == "G" ) {rgb="green"}
        if( ch == "B" ) {rgb="blue"}
        with(it[it$iteration==iter & it$channel==ch,],
            points(voltage_r, voltage_g, type="l", col=rgb))
    }
    text(it[it$iteration==iter,]$voltage_r[1],
    it[it$iteration==iter,]$voltage_g[1], iter)
}


# r vs b
X11()
plot(dat$voltages_r[171], dat$voltages_b[171], pch="s",
xlim=c(1000,3000), ylim=c(2000,5000))

for (iter in levels(it$iteration)) {
    for (ch in levels(it$channel)) {
        rgb <- NULL
        if( ch == "R" ) {rgb="red"}
        if( ch == "G" ) {rgb="green"}
        if( ch == "B" ) {rgb="blue"}
        with(it[it$iteration==iter & it$channel==ch,],
            points(voltage_r, voltage_b, type="l", col=rgb))
    }
    text(it[it$iteration==iter,]$voltage_r[1],
    it[it$iteration==iter,]$voltage_b[1], iter)
}

