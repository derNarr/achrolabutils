# this script only works with some data from tubes_spectra_plot.R

dat <- read.table("calibdata/measurements/depth_monitor20120208_1918.txt", sep=",")

names(dat) <- c("R","G","B","x","y","Y",paste("l", 1:36, sep=""))

dat$grey <- factor(round(1023*with(dat, 0.299*R/255 + 0.587*G/255 + 0.114*B/255)))

Ymean <- with(dat, tapply(Y, grey, mean))

# Luminance steps
plot(Ymean)
plot(dat$Y)

<<<<<<< HEAD
## monitor
startp <- 0
endp <- 2700
lcolor <- colorRampPalette(c("black","lightgrey"))(endp)
plot(as.numeric(dat[1,7:42]) ~ I(seq(390, 740, 10)), type="l",
    col=lcolor[startp], ylim=c(0,3.5), xlab=expression(paste(lambda, " in nm")), ylab="Intensity")
for (i in startp:endp){
    lines(as.numeric(dat[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i])
}
=======
# One Spectrum
plot(as.numeric(dat[1,7:42]) ~ I(1:36), type="l")
>>>>>>> f18dc06c6aa4fe6de97d840a48688529fc6c2351

## tubes
# red
startp <- 0
endp <- 50
lcolor <- colorRampPalette(c("black","red"))(endp)
lines(as.numeric(dat2[1,7:42]) ~ I(seq(390, 740, 10)), type="l",
    col=lcolor[startp], ylim=c(0,2.2), xlab=expression(paste(lambda, " in
    nm")), ylab="Intensity")
for (i in startp:endp){
    lines(as.numeric(dat2[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i])
}

# green
startp <- 50
endp <- 100
lcolor <- colorRampPalette(c("black","green"))(50)
lines(as.numeric(dat2[51,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[1])
for (i in startp:endp){
    lines(as.numeric(dat2[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i-50])
}

# blue
startp <- 100
endp <- 150
lcolor <- colorRampPalette(c("black","blue"))(50)
lines(as.numeric(dat2[101,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[1]) 
for (i in startp:endp){
    lines(as.numeric(dat2[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i-100])
}


