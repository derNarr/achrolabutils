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

dat1 <- read.table("achrolabutils/calibdata/measurements/calibration_tubes_raw_20120208_1833.txt", sep=",", skip=1)

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
pdf("achrolabutils/calibdata/measurements/tubes_spectrum.pdf", width=5,
height=5)
#svg("tubes_spectrum.svg", width=5, height=5)
#png("tubes_spectrum.png", width=450, height=450)
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
plot(Y ~ vR, dat2[1:100,], ylim=c(0, 70), pch=16, col="red",
    xlab="voltage", ylab="luminance", type="l", lwd=2)
lines(Y ~ vG, dat2[101:200,], col="green", pch=16, lwd=2)
lines(Y ~ vB, dat2[201:300,], col="blue", pch=16, lwd=2)

# fit curves
nlsR <- nls(Y ~ p1 + (p2 - p1)*exp(-exp(p3)*vR), data=dat2[1:100,],
        start=c(p1=50, p2=-10, p3=-7))
nlsG <- nls(Y ~ p1 + (p2 - p1)*exp(-exp(p3)*vG), data=dat2[101:200,],
        start=c(p1=50, p2=-10, p3=-7))
nlsB <- nls(Y ~ p1 + (p2 - p1)*exp(-exp(p3)*vB), data=dat2[201:300,],
        start=c(p1=50, p2=-15, p3=-10))

# predicted values
preR <- predict(nlsR)
preG <- predict(nlsG)
preB <- predict(nlsB)

lines(preR ~ vR, dat2[1:100,])
lines(preG ~ vR, dat2[1:100,])
lines(preB ~ vR, dat2[1:100,])

## all three tubes together
dat3 <- read.table("achrolabutils/calibdata/measurements/calibration_tubes_raw20120210_1050.txt", sep=",", skip=1)
names(dat3) <- c("vR","vG","vB","x","y","Y",paste("l", 1:36, sep=""))

# five measurements per step
dat3 <- aggregate(as.matrix(dat3[,4:ncol(dat3)]) ~ vR + vG + vB, dat3, mean)

dat3 <- dat3[order(dat3$vR, dat3$vG, dat3$vB),]
names(dat3) <- c("vR","vG","vB","x","y","Y",paste("l", 1:36, sep=""))

lines(Y ~ vB, dat3, pch=16, lwd=2)

# are 3 channels additive?
Yadd <- dat2[1:100,6] + dat2[101:200,6] + dat2[201:300,6]

lines(Yadd ~ vR, dat3, pch=16, col="grey", lwd=2)

legend(1000, 70, c("measured","sum"), col=c("black","grey"), lty=1, lwd=2,
    bty="n")

