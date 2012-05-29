#!/usr/bin/env Rscript
# -*- encoding: utf-8 -*-
# ./plot_spectra_monitor.R
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: (1) spectra for tubes
#          (2) luminance curves
#
# input: depth_monitor20120210_1127.txt
# output: monitor_spectrum.pdf
#
# last mod 2012-05-29, NU

setwd("Z:/AG_Heller/calibdata/measurements")

dat <- read.table("depth_monitor20120210_1127.txt", sep=",")

names(dat) <- c("R","G","B","x","y","Y",paste("l", 1:36, sep=""))

dat$grey <- factor(round(1023*with(dat, 0.299*R/255 + 0.587*G/255 + 0.114*B/255)))

Ymean <- with(dat, tapply(Y, grey, mean))

# Luminance steps
plot(Ymean)
plot(dat$Y)

## monitor
pdf("../figures/monitor_spectrum_20120210.pdf", width=5, height=5)
par(mai=c(.8,.8,.1,.1), mgp=c(2.7,1,0))

startp <- 0
endp <- 2700
lcolor <- colorRampPalette(c("black","lightgrey"))(endp)
plot(as.numeric(dat[1,7:42]) ~ I(seq(390, 740, 10)), type="l",
    col=lcolor[startp], ylim=c(0,3.5), xlab=expression(paste(lambda, " in nm")), ylab="Intensity")
for (i in startp:endp){
    lines(as.numeric(dat[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i])
}

dev.off()

# One Spectrum
plot(as.numeric(dat[1,7:42]) ~ I(1:36), type="l")

