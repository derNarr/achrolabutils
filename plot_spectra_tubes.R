#!/usr/bin/env Rscript
# -*- encoding: utf-8 -*-
# ./plot_spectra_tubes.R
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# this script should be looked at together with plot_spectra_monitor.R
#
# content: (1) spectra for tubes
#          (2) luminance curves
#
# input: calibration_tubes_raw20120206_1653.txt --> auskommentiert
#        calibration_tubes_raw_20120208_1833.txt
# output: tubes_spectrum.pdf
#         luminance_curves.pdf
#         luminance_curves_zoom.pdf
#
# last mod 2012-02-16, NU

setwd("Z:/AG_Heller/calibdata/measurements/")

## first measurements, not very good
# datL <- readLines("calibration_tubes_raw20120206_1653.txt")
# 
# raw <- as.numeric(unlist(strsplit(unlist(strsplit(datL, ";")), ",")))
# 
# dat2 <- NULL
# for (i in seq(1, length(raw), 42)){
#     dat2 <- rbind(dat2, raw[i:(i+41)])
#     }
# dat2 <- as.data.frame(dat2)

dat1 <- read.table("calibration_tubes_raw_20120208_1833.txt", sep=",", skip=1)

names(dat1) <- c("vR","vG","vB","x","y","Y",paste("l", 1:36, sep=""))

# five measurements per step
dat2 <- aggregate(as.matrix(dat1[,4:ncol(dat1)]) ~ vR + vG + vB, dat1, mean)

dat2 <- dat2[order(dat2$vR, dat2$vG, dat2$vB),]
names(dat2) <- c("vR","vG","vB","x","y","Y",paste("l", 1:36, sep=""))

###### (1) spectra for tubes ######

## three separat plots
par(mfrow=c(1,3))
# red
startp <- 0
endp <- 100
lcolor <- colorRampPalette(c("black","red"))(endp)
plot(as.numeric(dat2[1,7:42]) ~ I(1:36), type="l", col=lcolor[startp],
    ylim=c(0,3))
for (i in startp:endp){
    points(as.numeric(dat2[i,7:42]) ~ I(1:36), type="l", col=lcolor[i])
}

# green
startp <- 101
endp <- 200
lcolor <- colorRampPalette(c("black","green"))(100)
plot(as.numeric(dat2[501,7:42]) ~ I(1:36), type="l", col=lcolor[1],
    ylim=c(0,3))
for (i in startp:endp){
    points(as.numeric(dat2[i,7:42]) ~ I(1:36), type="l", col=lcolor[i-100])
}

# blue
startp <- 201
endp <- 300
lcolor <- colorRampPalette(c("black","blue"))(100)
plot(as.numeric(dat2[1001,7:42]) ~ I(1:36), type="l", col=lcolor[1],
    ylim=c(0,3))
for (i in startp:endp){
    points(as.numeric(dat2[i,7:42]) ~ I(1:36), type="l", col=lcolor[i-200])
}

## together in one plot
#pdf("../figures/tubes_spectrum_20120208.pdf", width=5, height=5)
png("../figures/tubes_spectrum_20120208.png", width=600, height=600)
#svg("tubes_spectrum.svg", width=5, height=5)
par(mai=c(.8,.8,.1,.1), mgp=c(2.7,1,0))

# red
startp <- 0
endp <- 100
lcolor <- colorRampPalette(c("black","red"))(endp)
plot(as.numeric(dat2[1,7:42]) ~ I(seq(390, 740, 10)), type="l",
    col=lcolor[startp], ylim=c(0,2.2), xlab=expression(paste(lambda, " in nm")), ylab="Intensity")
for (i in startp:endp){
    lines(as.numeric(dat2[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i])
}

# green
startp <- 101
endp <- 200
lcolor <- colorRampPalette(c("black","green"))(100)
lines(as.numeric(dat2[501,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[1])
for (i in startp:endp){
    lines(as.numeric(dat2[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i-100])
}

# blue
startp <- 201
endp <- 300
lcolor <- colorRampPalette(c("black","blue"))(100)
lines(as.numeric(dat2[1001,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[1]) 
for (i in startp:endp){
    lines(as.numeric(dat2[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i-200])
}

dev.off()


###### (2) luminance curves ######

## fitted with nls()

# fit curves with non-linear model (Pinheiro and Bates)
nlsR <- nls(Y ~ p1 + (p2 - p1)*exp(-exp(p3)*vR), data=dat2[1:100,],
        start=c(p1=50, p2=-10, p3=-7))
nlsG <- nls(Y ~ p1 + (p2 - p1)*exp(-exp(p3)*vG), data=dat2[101:200,],
        start=c(p1=50, p2=-10, p3=-7))
nlsB <- nls(Y ~ p1 + (p2 - p1)*exp(-exp(p3)*vB), data=dat2[201:300,],
        start=c(p1=50, p2=-15, p3=-10))

# fit polynomial regression
lmR <- lm(Y ~ vR + I(vR^3), dat2[1:100,])
lmG <- lm(Y ~ vG + I(vG^3), dat2[101:200,])
lmB <- lm(Y ~ vB + I(vB^3), dat2[201:300,])

preR <- predict(lmR)
preG <- predict(lmG)
preB <- predict(lmB)

# predicted values
preR <- predict(nlsR)
preG <- predict(nlsG)
preB <- predict(nlsB)


## all three tubes together
dat3 <- read.table("calibration_tubes_raw_20120210_1050.txt", sep=",", skip=1)
names(dat3) <- c("vR","vG","vB","x","y","Y",paste("l", 1:36, sep=""))

# five measurements per step
dat3 <- aggregate(as.matrix(dat3[,4:ncol(dat3)]) ~ vR + vG + vB, dat3, mean)

dat3 <- dat3[order(dat3$vR, dat3$vG, dat3$vB),]
names(dat3) <- c("vR","vG","vB","x","y","Y",paste("l", 1:36, sep=""))

# are 3 channels additive?
Yadd <- dat2[1:100,6] + dat2[101:200,6] + dat2[201:300,6]
w <- c(1592, 2316, 2234)

guessVoltages <- function(Y) {
    Yred <- 6.173447/(6.173447+22.92364+4.036948)*Y
    Ygreen <- 22.92364/(6.173447+22.92364+4.036948)*Y
    Yblue <- 4.036948/(6.173447+22.92364+4.036948)*Y

    inv <- function(y, p) {-log((y - p[1])/(p[2]-p[1]))/exp(p[3])}

    pR <- summary(nlsR)$par[,1]
    pG <- summary(nlsG)$par[,1]
    pB <- summary(nlsB)$par[,1]
    
    volR <- inv(Yred,   pR)
    volG <- inv(Ygreen, pG)
    volB <- inv(Yblue,  pB)
    
    voltages <- data.frame(Y=Y, volR=volR, volG=volG, volB=volB)
    voltages
}

Yratio <- dat2[1:100,6] + dat2[101:200,6] + dat2[201:300,6]

predict(nlsR, data.frame(vR=1592))
# [1] 6.173447
predict(nlsG, data.frame(vG=2316))
# [1] 22.92364
predict(nlsB, data.frame(vB=2234))
# [1] 4.036948

inv <- function(y, p) {-log((y - p[1])/(p[2]-p[1]))/exp(p[3])}

pR <- summary(nlsR)$par[,1]
pG <- summary(nlsG)$par[,1]
pB <- summary(nlsB)$par[,1]

#inv(, pR)

## plot
#pdf("../figures/luminance_curves_20120210.pdf", width=4, height=4)
png("../figures/luminance_curves_20120210.png", width=600, height=600)

par(mai=c(.8,.8,.1,.1), mgp=c(2.6,1,0))
plot(Y ~ vR, dat2[1:100,], ylim=c(0, 70), pch=16, col="red",
    xlab="voltage", ylab="luminance", type="l", lwd=2)
lines(Y ~ vG, dat2[101:200,], col="green", pch=16, lwd=2)
lines(Y ~ vB, dat2[201:300,], col="blue", pch=16, lwd=2)

lines(preR ~ vR, dat2[1:100,], lty=2, col="grey")
lines(preG ~ vR, dat2[1:100,], lty=2, col="grey")
lines(preB ~ vR, dat2[1:100,], lty=2, col="grey")

lines(Y ~ vB, dat3, pch=16, lwd=2)
lines(Yadd ~ vR, dat3, pch=16, col="grey", lwd=2)

legend(1000, 70, c("measured","sum"), col=c("black","grey"), lty=1, lwd=2,
    bty="n")

dev.off()

# zoomed in
#pdf("../figures/luminance_curves_zoom_20120210.pdf", width=4, height=4)
png("../figures/luminance_curves_zoom_20120210.png", width=600, height=600)

par(mai=c(.8,.8,.1,.1), mgp=c(2.6,1,0))
plot(Y ~ vR, dat2[1:40,], ylim=c(0, 35), pch=16, col="red",
    xlab="voltage", ylab="luminance", type="l", lwd=2)
lines(Y ~ vG, dat2[101:140,], col="green", pch=16, lwd=2)
lines(Y ~ vB, dat2[201:240,], col="blue", pch=16, lwd=2)

lines(preR[1:40] ~ vR, dat2[1:40,], lty=2)
lines(preG[1:40] ~ vR, dat2[1:40,], lty=2)
lines(preB[1:40] ~ vR, dat2[1:40,], lty=2)

lines(Y[1:40] ~ vB[1:40], dat3, pch=16, lwd=2)
lines(Yadd[1:40] ~ vR[1:40], dat3, pch=16, col="grey", lwd=2)

legend(1000, 35, c("measured","sum"), col=c("black","grey"), lty=1, lwd=2,
    bty="n")

dev.off()

