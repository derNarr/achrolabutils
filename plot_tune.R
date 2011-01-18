#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./plot_tune.R
#
# (c) 2011 Konstantin Sering <konstantin.sering [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# last mod 2011-01-18, KS

##########################################################################
### READ DATA ############################################################
##########################################################################

#path="C:/Dokumente und Einstellungen/user1/Desktop/visionlabutils/"
path="/home/kfs-studium/Dokumente/arbeit/PI/visionlabutils/"

setwd(paste(path, "visionlab/data/", sep=""))

dat <- read.csv("color_table_20101209_1220.csv", na.strings="NA", colClasses=c("character", rep("numeric", 16)))
dat2 <- dat[175:177,]
datTuned <- read.csv("color_table_20110115_1306.csv", na.strings="NA", colClasses=c("character", rep("numeric", 16)))
datTuned2 <- datTuned[175:177,]


setwd(paste(path, "visionlab/tune/", sep=""))

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

setwd(path)

source("xyyToRgb.R")
it <- cbind(it, xyyToRgb(it[,4:6]))

rm(tmp, tmp2, files, file)

##########################################################################
### select COLOR #########################################################
##########################################################################
color_num = 171
it2 <- it[it$target=="r770g908b1069",]

##########################################################################
### xyY ##################################################################
##########################################################################

# x vs y
X11()
plot(dat$monitor_xyY_x[color_num], dat$monitor_xyY_y[color_num], pch="x",
xlim=c(0.26,0.31), ylim=c(0.25,0.33))

for (iter in levels(it2$iteration)) {
    for (ch in levels(it2$channel)) {
        rgb <- NULL
        if( ch == "R" ) {rgb="red"}
        if( ch == "G" ) {rgb="green"}
        if( ch == "B" ) {rgb="blue"}
        with(it2[it2$iteration==iter & it2$channel==ch,],
            points(xyY_x, xyY_y, type="l", col=rgb))
    }
    text(it2[it2$iteration==iter,]$xyY_x[1],
    it2[it2$iteration==iter,]$xyY_y[1], iter)
}


# x vs Y
X11()
plot(dat$monitor_xyY_x[color_num], dat$monitor_xyY_Y[color_num], pch="x",
xlim=c(0.26,0.31), ylim=c(10,20))

for (iter in levels(it2$iteration)) {
    for (ch in levels(it2$channel)) {
        rgb <- NULL
        if( ch == "R" ) {rgb="red"}
        if( ch == "G" ) {rgb="green"}
        if( ch == "B" ) {rgb="blue"}
        with(it2[it2$iteration==iter & it2$channel==ch,],
            points(xyY_x, xyY_Y, type="l", col=rgb))
    }
    text(it2[it2$iteration==iter,]$xyY_x[1],
    it2[it2$iteration==iter,]$xyY_Y[1], iter)
}

##########################################################################
### VOLTAGES #############################################################
##########################################################################

# r vs g
X11()
plot(dat$voltages_r[color_num], dat$voltages_g[color_num], pch="s",
xlim=c(0x400,0xFFF), ylim=c(0x400,0xFFF))

for (iter in levels(it2$iteration)) {
    for (ch in levels(it2$channel)) {
        rgb <- NULL
        if( ch == "R" ) {rgb="red"}
        if( ch == "G" ) {rgb="green"}
        if( ch == "B" ) {rgb="blue"}
        with(it2[it2$iteration==iter & it2$channel==ch,],
            points(voltage_r, voltage_g, type="l", col=rgb))
    }
    text(it2[it2$iteration==iter,]$voltage_r[1],
    it2[it2$iteration==iter,]$voltage_g[1], iter)
}


# r vs b
X11()
plot(dat$voltages_r[color_num], dat$voltages_b[color_num], pch="s",
xlim=c(1000,3000), ylim=c(2000,5000))

for (iter in levels(it2$iteration)) {
    for (ch in levels(it2$channel)) {
        rgb <- NULL
        if( ch == "R" ) {rgb="red"}
        if( ch == "G" ) {rgb="green"}
        if( ch == "B" ) {rgb="blue"}
        with(it2[it2$iteration==iter & it2$channel==ch,],
            points(voltage_r, voltage_b, type="l", col=rgb))
    }
    text(it2[it2$iteration==iter,]$voltage_r[1],
    it2[it2$iteration==iter,]$voltage_b[1], iter)
}

##########################################################################
### RGB ##################################################################
##########################################################################

# r vs g
X11()
tmp <- xyyToRgb(dat[color_num, 12:14])
plot(tmp[1], tmp[2], pch="x", xlim=c(7,14), ylim=c(10,20), xlab="red",
ylab="green")

for (iter in levels(it2$iteration)) {
    for (ch in levels(it2$channel)) {
        rgb <- NULL
        if( ch == "R" ) {rgb="red"}
        if( ch == "G" ) {rgb="green"}
        if( ch == "B" ) {rgb="blue"}
        with(it2[it2$iteration==iter & it2$channel==ch,],
            points(R, G, type="l", col=rgb))
    }
    text(it2[it2$iteration==iter,]$R[1],
    it2[it2$iteration==iter,]$G[1], iter)
}


# r vs b
X11()
tmp <- xyyToRgb(dat[color_num, 12:14])
plot(tmp[1], tmp[3], pch="x", xlim=c(7,14), ylim=c(15,28), xlab="red",
ylab="blue")

for (iter in levels(it2$iteration)) {
    for (ch in levels(it2$channel)) {
        rgb <- NULL
        if( ch == "R" ) {rgb="red"}
        if( ch == "G" ) {rgb="green"}
        if( ch == "B" ) {rgb="blue"}
        with(it2[it2$iteration==iter & it2$channel==ch,],
            points(R, B, type="l", col=rgb))
    }
    text(it2[it2$iteration==iter,]$R[1],
    it2[it2$iteration==iter,]$B[1], iter)
}

