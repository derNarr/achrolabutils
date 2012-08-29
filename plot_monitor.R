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
# last mod 2012-08-29, NU

#setwd("Z:/AG_Heller/calibdata/measurements/")

###### (1) Plot most recent measurement ######
i=1
files <- dir(pattern="^gdata[0-9][0-9].*\\.txt")

plot(x=1, y=1, xlim=c(0,400), ylim=c(0,40), type="n")
for (file in files){
dat <- read.table(file,header=TRUE)

#par(new=T, fig=c(0,1,0,1))
#x <- seq(1,length(dat[,1]),by=100)
points(y=dat$Y, x=dat$gray_1, xlab="gray color", ylab="Luminance", pch=4, col=colors()[(i+50)*5])
i=i+1
}

dev.print(device=postscript, "graph1.eps")
#pdf(paste("testpdf.pdf", sep=""), height=2.75, width=10)
#dev.off()

## Nora's solution

files <- dir(pattern="^gdata[0-9][0-9].*\\.txt")

dat1 <- NULL
for (file in files){
    dat1 <- rbind(dat1, read.table(file, T))
    }

dat2 <- dat1[,c(1,6,7,8)]
dat2$time <- factor(rep(1:10, e=80))

library(lattice)

xyplot(Y ~ gray_1 | time, dat2, type=c("l","g"))

s <- seq(400, 375, -5)
dat_tmp <- dat2[dat2$gray_1 %in% s,]

xyplot(Y ~ gray_1, dat_tmp, type=c("b","g"), groups=time)

xyplot(Y ~ gray_1, dat2, type=c("b","g"), groups=time)

## aggregate over different calibrations to get an estimate of "true curve"

files <- dir(pattern="calibrange.*\\.txt")

dat1 <- NULL
for (file in files){
    dat1 <- rbind(dat1, read.table(file, T))
    }

dat2 <- dat1[,c(1,6,7,8)]
dat2$time <- factor(rep(1:10, e=180))

dat3 <- aggregate(cbind(x,y,Y) ~ gray_1, dat2, mean)
dat3 <- dat3[1:176,]  ## Werte < 400 cd/m^2

plot(Y ~ gray_1, dat1[dat1$gray_1 %in% seq(875, 5, -5),], col="orange",
    xlab="Color #", ylab=expression("Luminance in cd/m",^2))
points(Y ~ gray_1, dat3, pch=16)

abline(v=620, h=dat3$Y[dat3$gray_1==620], lty=2, col="grey")

plot(Y ~ gray_1, dat1[dat1$gray_1 %in% seq(875, 5, -5),], col="lightgrey")

# 3 calibration colors:
390
600
850

