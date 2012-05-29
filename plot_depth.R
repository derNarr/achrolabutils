#!/usr/bin/env Rscript
# -*- encoding: utf-8 -*-
# ./plotDepth.R
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# plots for monitor depth
#
# input: depth_monitor*.txt
# output: depth_monitor.pdf
#
# content: (1) Plot most recent measurement
#          (2) Compare several measurements
#
# last mod 2012-05-21, NU

###### (1) Plot most recent measurement ######

setwd("Z:/AG_Heller/calibdata/measurements")

files <- dir(pattern="depth_monitor[0-9][0-9].*\\.txt")
file <- tail(files, 1)  # last measurement

dat0 <- read.table(file, sep=",")
names(dat0) <- c("R","G","B","x","y","Y", paste("l",1:36,sep=""))
#dat$R <- factor(dat$R)
#dat$G <- factor(dat$G)
#dat$B <- factor(dat$B)

dat <- aggregate(as.matrix(dat0) ~ R+ G + B, dat0, mean)[,-c(1:3)]
names(dat) <- c("R","G","B","x","y","Y", paste("l",1:36,sep=""))
dat <- dat[order(dat$Y),]
rownames(dat) <- NULL

plot(dat$Y)

# analytical plots
pdf(paste("../figures/depth_monitor_", substr(file, 14, 21), ".pdf",
    sep=""), width=7, height=3.75)
#png(paste("depth_monitor_", substr(file, 14, 21), ".pdf", sep=""))

par(mfrow=c(1,2), mai=c(.8,.8,.15,.15), mgp=c(2.7,1,0))
plot(dat$Y ~ I(0:1023), ylab="Luminance", xlab="Color")

id <- 100:110
plot(dat$Y[id] ~ I(id-1), ylab="Luminance", xlab="Color")

dev.off()

####### (2) Compare several measurements ######

dat1 <- read.table("depth_monitor20120210_1127.txt", sep=",")
dat2 <- read.table("depth_monitor20120217_1438.txt", sep=",")
dat3 <- read.table("depth_monitor20120515_1658.txt", sep=",")
dat4 <- read.table("depth_monitor20120516_1902.txt", sep=",")

names(dat1) <- c("R","G","B","x","y","Y", paste("l",1:36,sep=""))
names(dat2) <- c("R","G","B","x","y","Y", paste("l",1:36,sep=""))
names(dat3) <- c("R","G","B","x","y","Y", paste("l",1:36,sep=""))
names(dat4) <- c("R","G","B","x","y","Y", paste("l",1:36,sep=""))

dat1 <- aggregate(as.matrix(dat1) ~ R+ G + B, dat1, mean)[,-c(1:3)]
names(dat1) <- c("R","G","B","x","y","Y", paste("l",1:36,sep=""))
dat1 <- dat1[order(dat1$Y),]
rownames(dat1) <- NULL

dat2 <- aggregate(as.matrix(dat2) ~ R+ G + B, dat2, mean)[,-c(1:3)]
names(dat2) <- c("R","G","B","x","y","Y", paste("l",1:36,sep=""))
dat2 <- dat2[order(dat2$Y),]
rownames(dat2) <- NULL

dat3 <- aggregate(as.matrix(dat3) ~ R+ G + B, dat3, mean)[,-c(1:3)]
names(dat3) <- c("R","G","B","x","y","Y", paste("l",1:36,sep=""))
dat3 <- dat3[order(dat3$Y),]
rownames(dat3) <- NULL

dat4 <- aggregate(as.matrix(dat4) ~ R+ G + B, dat4, mean)[,-c(1:3)]
names(dat4) <- c("R","G","B","x","y","Y", paste("l",1:36,sep=""))
dat4 <- dat4[order(dat4$Y),]
rownames(dat4) <- NULL

# plot with different zooms
par(mfrow=c(2,2))

plot(dat1$Y ~ I(0:1023), ylab="Luminance", xlab="Color")
points(dat2$Y ~ I(0:1022), col="blue")
points(dat3$Y ~ I(0:1023), col="green")
points(dat4$Y ~ I(0:1023), col="purple")

id <- 100:110

plot(dat1$Y[id] ~ I(id-1), ylab="Luminance", xlab="Color", ylim=c(2.5, 5.5))
points(dat2$Y[id] ~ I(id-1), col="blue")
points(dat3$Y[id] ~ I(id-1), col="green")
points(dat4$Y[id] ~ I(id-1), col="purple")

id <- 500:510

plot(dat1$Y[id] ~ I(id-1), ylab="Luminance", xlab="Color", ylim=c(62.5, 77.5))
points(dat2$Y[id] ~ I(id-1), col="blue")
points(dat3$Y[id] ~ I(id-1), col="green")
points(dat4$Y[id] ~ I(id-1), col="purple")

id <- 800:810

plot(dat1$Y[id] ~ I(id-1), ylab="Luminance", xlab="Color", ylim=c(260,302))
points(dat2$Y[id] ~ I(id-1), col="blue")
points(dat3$Y[id] ~ I(id-1), col="green")
points(dat4$Y[id] ~ I(id-1), col="purple")

# --> offensichtlich gibt es ziemlich Unterschiede zwischen den einzelnen
# Messungen, aber das hat anscheinend nichts mit dem Zeitpunkt der Messung
# zu tun.

