# find_color.R
#
# Find voltages that adjust tubes so that xyY for tubes has a minimum
# distance from monitor xyY.
#
# content: (1) read data for tubes and monitor
#          (2) find best fit
#          (3) diagnostic plots
#
# input: measure_tubes_20120210_2151.txt
#        depth_monitor20120210_1949.txt
# output: --
#
# last mod: Feb/16/2012, NU

###### (1) read data for tubes and monitor ######

tub0 <- read.table("measure_tubes_20120210_2151.txt", header=T, sep=",")
# Careful! This thing is huge!

tub <- aggregate(as.matrix(tub0) ~ volR + volG + volB, tub0, mean)
for (i in 1:3) tub[,4] <- NULL
names(tub) <- c("volR","volG","volB","x","y","Y",paste("l", 1:36, sep=""))

mon0 <- read.table("depth_monitor20120210_1949.txt", sep=",")
names(mon0) <- c("R","G","B","x","y","Y",paste("l", 1:36, sep=""))
mon <- aggregate(as.matrix(mon0) ~ R + G + B, mon0, mean)
for (i in 1:3) mon[,4] <- NULL
names(mon) <- c("R","G","B","x","y","Y",paste("l", 1:36, sep=""))

###### (2) find best fit ######

res_x <- NULL
for (i in 1:10){
    x <- tub[which.min(abs(tub$x - mon$x[i])),]
    res_x <- rbind(res_x, x)
    gc() # free all memory R doesn't need anymore
}

res_y <- NULL
for (i in 1:10){
    y <- tub[which.min(abs(tub$y - mon$y[i])),]
    res_y <- rbind(res_y, y)
    gc() # free all memory R doesn't need anymore
}

res_Y <- NULL
for (i in 1:10){
    Y <- tub[which.min(abs(tub$Y - mon$Y[i])),]
    res_Y <- rbind(res_Y, Y)
    gc() # free all memory R doesn't need anymore
}


## first for x and y coosrdinates

for (i in 1:10){
    tub[paste("r", i, sep="")] <- sqrt((tub$x - mon$x[i])^2  + (tub$y -
        mon$y[i])^2)
}

epsilon <- 0.0035

## then for Y

reslist <- NULL
for (i in 1:10){
    tmp <- tub[tub[paste("r", i, sep="")] < epsilon,]
    print(paste("tmp dim for grey", i, "is", dim(tmp)))
    reslist <- rbind(reslist, tmp[which.min(abs(tmp$Y - mon$Y[i])),])
}

###### (3) diagnostic plots ######

# Did we measure the correct area?
par(mfrow=c(1,2))
# diagnostic plot xy
plot(tub$x, tub$y, pch=".", xlim=c(0.296, 0.306))
points(mon$x, mon$y, pch="x", col="red")
# and Y
plot(jitter(rep(1, length(tub$Y))), tub$Y, pch=".", ylim=c(19,21.5))
abline(h=mon$Y, col="red")

# How does the color influence direction?
par(mfrow=c(1,3))
# red
plot(tub$x, tub$y, type="n", xlim=c(0.296, 0.306))
points(mon$x, mon$y, pch="x", col="red")
lcolor <- colorRampPalette(c("black","red"))(length(unique(tub$volR)))
for (i in 1:length(unique(tub$volR))) {
    tmp <- tub[tub$volR==unique(tub$volR)[i],]
    points(tmp$x, tmp$y, col=lcolor[i], pch=".")
    }
# green
plot(tub$x, tub$y, type="n", xlim=c(0.296, 0.306))
points(mon$x, mon$y, pch="x", col="red")
lcolor <- colorRampPalette(c("black","green"))(length(unique(tub$volG)))
for (i in 1:length(unique(tub$volG))) {
    tmp <- tub[tub$volG==unique(tub$volG)[i],]
    points(tmp$x, tmp$y, col=lcolor[i], pch=".")
    }
# blue
plot(tub$x, tub$y, type="n", xlim=c(0.296, 0.306))
points(mon$x, mon$y, pch="x", col="red")
lcolor <- colorRampPalette(c("black","blue"))(length(unique(tub$volB)))
for (i in 1:length(unique(tub$volB))) {
    tmp <- tub[tub$volB==unique(tub$volB)[i],]
    points(tmp$x, tmp$y, col=lcolor[i], pch=".")
    }

# Look at deviance of our measurements:
# ellipse function
ell <- function(t, xc=0, yc=0, a=1, b=1/5, phi=0){
  phi <- ifelse(phi < pi/2, phi, pi - phi)
  cbind(x = xc + a*cos(t)*cos(phi) - b*sin(t)*sin(phi),
        y = yc + a*cos(t)*sin(phi) + b*sin(t)*cos(phi))
}

steps <- 1
tub.tmp <- tub
tub <- tub[tub$volR==1270 & tub$volG==1670,]
tub <- tub[order(tub$volB),]
print(dim(tub))
idx <- seq(1,46,steps)
plot(tub$x, tub$y, type="n")
lcolor <- colorRampPalette(c("green","red"))(length(idx))
for (j in 1:length(idx)) {
    i <- idx[j]
    points(y ~ x, data=tub[i,], pch="x", col=lcolor[j])
    volR <- tub$volR[i]
    volG <- tub$volG[i]
    volB <- tub$volB[i]
    tmp <- tub0[tub0$volR==volR & tub0$volG==volG & tub0$volB==volB,]
    points(y ~ x, data=tmp, col=lcolor[j])
    xsd <- sd(tmp$x)
    ysd <- sd(tmp$y)
    lines(ell(seq(0,2*pi,length.out=100), tub$x[i], tub$y[i], xsd, ysd),
    col=lcolor[j])
    }
lines(tub$x, tub$y)
tub <- tub.tmp
rm(tub.tmp)

