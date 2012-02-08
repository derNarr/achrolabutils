

datL <- readLines("calibration_tubes_raw20120206_1653.txt")

raw <- as.numeric(unlist(strsplit(unlist(strsplit(datL, ";")), ",")))

dat2 <- NULL
for (i in seq(1, length(raw), 42)){
    dat2 <- rbind(dat2, raw[i:(i+41)])
    }
dat2 <- as.data.frame(dat2)

plot(as.numeric(dat[1,7:42]), type="l")
## three separat plots
par(mfrow=c(1,3))
# red
startp <- 0
endp <- 50
lcolor <- colorRampPalette(c("black","red"))(endp)
plot(as.numeric(dat2[1,7:42]) ~ I(1:36), type="l", col=lcolor[startp],
    ylim=c(0,3))
for (i in startp:endp){
    points(as.numeric(dat2[i,7:42]) ~ I(1:36), type="l", col=lcolor[i])
}

# green
startp <- 50
endp <- 100
lcolor <- colorRampPalette(c("black","green"))(50)
plot(as.numeric(dat2[51,7:42]) ~ I(1:36), type="l", col=lcolor[1],
    ylim=c(0,3))
for (i in startp:endp){
    points(as.numeric(dat2[i,7:42]) ~ I(1:36), type="l", col=lcolor[i-50])
}

# blue
startp <- 100
endp <- 150
lcolor <- colorRampPalette(c("black","blue"))(50)
plot(as.numeric(dat2[101,7:42]) ~ I(1:36), type="l", col=lcolor[1],
    ylim=c(0,3))
for (i in startp:endp){
    points(as.numeric(dat2[i,7:42]) ~ I(1:36), type="l", col=lcolor[i-100])
}

## together in one plot
pdf("tubes_spectrum.pdf", width=5, height=5)
#svg("tubes_spectrum.svg", width=5, height=5)
#png("tubes_spectrum.png", width=450, height=450)
par(mai=c(.8,.8,.1,.1), mgp=c(2.7,1,0))

# red
startp <- 0
endp <- 50
lcolor <- colorRampPalette(c("black","red"))(endp)
plot(as.numeric(dat2[1,7:42]) ~ I(seq(390, 740, 10)), type="l",
    col=lcolor[startp], ylim=c(0,2.2), xlab=expression(paste(lambda, " in nm")), ylab="Intensity")
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

dev.off()

