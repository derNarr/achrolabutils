# find_color.R
#
# Find voltages that adjust tubes so that xyY for tubes has a minimum
# distance from monitor xyY.

tub0 <- read.table("measure_tubes_20120210_2151.txt", header=T, sep=",")
# Careful! This thing is huge!

tub <- aggregate(as.matrix(tub0) ~ volR + volG + volB, tub0, mean)
for (i in 1:3) tub[,4] <- NULL
names(tub) <- c("volR","volG","volB","x","y","Y",paste("l", 1:36, sep=""))

mon0 <- read.table("depth_monitor20120210_1949.txt", sep=",")
names(mon0) <- c("R","G","B","x","y","Y",paste("l", 1:36, sep=""))
mon <- aggregate(as.matrix(mon0) ~ R + G + B, mon0, mean)
for (i in 1:3) tub[,4] <- NULL
names(mon) <- c("R","G","B","x","y","Y",paste("l", 1:36, sep=""))

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


reslist <- NULL
for (i in 1:10){
    reslist <- rbind(reslist, tub[which.min(sqrt((tub$x - mon$x[i])^2 + (tub$y -
    mon$y[i])^2 + (tub$Y - mon$Y[i])^2)),])
}

# > reslist
#
#        volR volG volB         x         y        Y 
# 49429  1271 1682 1666 0.3029619 0.3186396 20.62462 
# 58780  1272 1682 1673 0.3028470 0.3182797 20.76279 
# 587801 1272 1682 1673 0.3028470 0.3182797 20.76279 
# 54773  1271 1682 1670 0.3026479 0.3181430 20.66311 
# 587802 1272 1682 1673 0.3028470 0.3182797 20.76279 
# 587803 1272 1682 1673 0.3028470 0.3182797 20.76279 
# 587804 1272 1682 1673 0.3028470 0.3182797 20.76279 
# 587805 1272 1682 1673 0.3028470 0.3182797 20.76279 
# 587806 1272 1682 1673 0.3028470 0.3182797 20.76279 
# 587807 1272 1682 1673 0.3028470 0.3182797 20.76279 




