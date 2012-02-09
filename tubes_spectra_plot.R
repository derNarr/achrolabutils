# this script should be looked at together with depth_monitor_plot.R
#
# content: (1) spectra for tubes
#          (2) luminance curves
#
# input: calibration_tubes_raw20120206_1653.txt --> auskommentiert
#        calibration_tubes_raw_20120208_1833.txt
# output: tubes_spectrum.pdf
#
# last mod:

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

dat2 <- read.table("achrolabutils/calibdata/measurements/calibration_tubes_raw_20120208_1833.txt", sep=",", skip=1)

names(dat2) <- c("vR","vG","vB","x","y","Y",paste("l", 1:36, sep=""))

###### (1) spectra for tubes ######

plot(as.numeric(dat[1,7:42]), type="l")
## three separat plots
par(mfrow=c(1,3))
# red
startp <- 0
endp <- 500
lcolor <- colorRampPalette(c("black","red"))(endp)
plot(as.numeric(dat2[1,7:42]) ~ I(1:36), type="l", col=lcolor[startp],
    ylim=c(0,3))
for (i in startp:endp){
    points(as.numeric(dat2[i,7:42]) ~ I(1:36), type="l", col=lcolor[i])
}

# green
startp <- 501
endp <- 1000
lcolor <- colorRampPalette(c("black","green"))(500)
plot(as.numeric(dat2[501,7:42]) ~ I(1:36), type="l", col=lcolor[1],
    ylim=c(0,3))
for (i in startp:endp){
    points(as.numeric(dat2[i,7:42]) ~ I(1:36), type="l", col=lcolor[i-500])
}

# blue
startp <- 1001
endp <- 1505
lcolor <- colorRampPalette(c("black","blue"))(500)
plot(as.numeric(dat2[1001,7:42]) ~ I(1:36), type="l", col=lcolor[1],
    ylim=c(0,3))
for (i in startp:endp){
    points(as.numeric(dat2[i,7:42]) ~ I(1:36), type="l", col=lcolor[i-1000])
}

## together in one plot
pdf("achrolabutils/calibdata/measurements/tubes_spectrum.pdf", width=5,
height=5)
#svg("tubes_spectrum.svg", width=5, height=5)
#png("tubes_spectrum.png", width=450, height=450)
par(mai=c(.8,.8,.1,.1), mgp=c(2.7,1,0))

# red
startp <- 0
endp <- 500
lcolor <- colorRampPalette(c("black","red"))(endp)
plot(as.numeric(dat2[1,7:42]) ~ I(seq(390, 740, 10)), type="l",
    col=lcolor[startp], ylim=c(0,2.2), xlab=expression(paste(lambda, " in nm")), ylab="Intensity")
for (i in startp:endp){
    lines(as.numeric(dat2[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i])
}

# green
startp <- 501
endp <- 1000
lcolor <- colorRampPalette(c("black","green"))(500)
lines(as.numeric(dat2[501,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[1])
for (i in startp:endp){
    lines(as.numeric(dat2[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i-500])
}

# blue
startp <- 1001
endp <- 1500
lcolor <- colorRampPalette(c("black","blue"))(500)
lines(as.numeric(dat2[1001,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[1]) 
for (i in startp:endp){
    lines(as.numeric(dat2[i,7:42]) ~ I(seq(390, 740, 10)),
    col=lcolor[i-1000])
}

dev.off()


###### (2) luminance curves ######

dat3 <- read.table("achrolabutils/calibdata/measurements/calibration_tubes_raw_20120208_1833.txt", sep=",", skip=1)

names(dat3) <- c("vR","vG","vB","x","y","Y",paste("l", 1:36, sep=""))


## fitted with nls()
plot(Y ~ vR, dat3[1:500,], ylim=c(0, 40), pch=16, col="red",
    xlab="voltage", ylab="luminance")
points(Y ~ vG, dat3[501:1000,], col="green", pch=16)
points(Y ~ vB, dat3[1001:1500,], col="blue", pch=16)

# fit curves
nlsR <- nls(Y ~ p1 + (p2 - p1)*exp(-exp(p3)*vR), data=dat3[1:500,],
        start=c(p1=50, p2=-10, p3=-7))
nlsG <- nls(Y ~ p1 + (p2 - p1)*exp(-exp(p3)*vG), data=dat3[501:1000,],
        start=c(p1=50, p2=-10, p3=-7))
nlsB <- nls(Y ~ p1 + (p2 - p1)*exp(-exp(p3)*vB), data=dat3[1001:1500,],
        start=c(p1=50, p2=-15, p3=-10))

# predicted values
preR <- predict(nlsR)
preG <- predict(nlsG)
preB <- predict(nlsB)

lines(preR ~ vR, dat3[1:500,])
lines(preG ~ vR, dat3[1:500,])
lines(preB ~ vR, dat3[1:500,])

## fitted with lm() for medium values
plot(Y ~ vR, dat3[100:400,], ylim=c(0, 40), pch=16, col="red",
    xlab="voltage", ylab="luminance")
points(Y ~ vG, dat3[600:900,], col="green", pch=16)
points(Y ~ vB, dat3[1100:1400,], col="blue", pch=16)

lmR <- lm(Y ~ vR, dat3[100:400,])
lmG <- lm(Y ~ vG, dat3[600:900,])
lmB <- lm(Y ~ vB, dat3[1100:1400,])

abline(lmR)
abline(lmG)
abline(lmB)
# Hmm, don't know. Looks good for blue but that also looks good with
# nls()...


