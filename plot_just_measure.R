#!/usr/bin/env Rscript (python)
# -*- encoding: utf-8 -*-
# ./plot_just_measure.R
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# plots for behavior of luminance of tubes over time
#
# content: (1) Plot most recent measurement
#
# input: justmeasure_color_20120519_1121.txt
# output: /figures/tubes_over_time.pdf
#
# last mod 2012-05-21, NU

setwd("Z:/AG_Heller/calibdata/measurements")

###### (1) Plot most recent measurement ######

files <- dir(pattern="justmeasure_color_[0-9][0-9].*\\.txt")
file <- tail(files, 1)  # last measurement

dat <- read.table(file, sep=",", skip=3)

names(dat) <- c("x","y","Y")

pdf(paste("../figures/tubes_over_time_", substr(file, 19, 26), ".pdf",
    sep=""), height=2.75, width=10)
par(mfrow=c(1,4), mai=c(.5,.5,.1,.1), mgp=c(2.7,1,0))
#png(paste("../figures/tubes_over_time_", substr(file, 19, 26), ".png",
#    sep=""), height=600, width=600)

#par(new=T, fig=c(0,1,0,1))
x <- seq(1,length(dat[,1]),by=100)
plot(dat$Y[x] ~ I(1.7*x/3600), xlab="time [hours]",
    ylab="Luminance", pch=4, ylim=c(16,25))

#par(new=T, fig=c(0.10,0.55,0.35,0.8))
id <- seq(20,2000,by=20)
plot(dat$Y[id] ~ I(1.7*id/3600), xlab="", ylab="", pch=4)
box()

#par(new=T, fig=c(0.50,0.95,0.35,0.8))
id <- seq(2000,8000,by=50)
plot(dat$Y[id] ~ I(1.7*id/3600), xlab="", ylab="", pch=4)

#par(new=T, fig=c(0.10,0.95,0.10,0.48))
id <- seq(8000,length(dat[,1]), by=100)
plot(dat$Y[id] ~ I(1.7*id/3600), xlab="", ylab="", pch=4)

dev.off()
