# this script only works with some data from tubes_spectra_plot.R

dat <- read.table("depth_monitor20120207_2249.txt", sep=",")

s1 <- dat[,6]
# v1 <- as.numeric(substr(s1, 1, 10))

v1 <- as.numeric(gsub("([ .0-9]*)-?[0-9]\\..*$", "\\1", cs1))
v2 <- as.numeric(gsub("[ .0-9]*(-?[0-9]\\..*$)", "\\1", cs1))

dat$V6 <- NULL

dat$v1 <- v1
dat$v2 <- v2

names(dat) <- c("R","G","B","x","y",paste("l", 2:36, sep=""),"Y","l1")

# Sort variables
dat <- cbind(dat[1:5], dat[41:42], dat[6:40])
dat$grey <- factor(round(1023*with(dat, 0.299*R/255 + 0.587*G/255 + 0.114*B/255)))

Ymean <- with(dat, tapply(Y, grey, mean))

# Luminance steps
plot(Ymean[0:100])
plot(dat$Y[0:100])
plot(Ymean[600:700])
plot(dat$Y[600:700])

## monitor
startp <- 0
endp <- 2700
lcolor <- colorRampPalette(c("black","lightgrey"))(endp)
plot(as.numeric(dat[1,7:42]) ~ I(seq(390, 740, 10)), type="l",
    col=lcolor[startp], ylim=c(0,3.5), xlab=expression(paste(lambda, " in nm")), ylab="Intensity")
for (i in startp:endp){
    lines(as.numeric(dat[i,7:42]) ~ I(seq(390, 740, 10)), col=lcolor[i])
}

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


