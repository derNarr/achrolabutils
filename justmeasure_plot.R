
# Info colorpalette
plot(1:100, col=colorRampPalette(c("blue","green"))(100), type="p", pch=16)

#setwd("D:/Experimente/achrolabutils")

datL <- readLines("justmeasure_spec_20120208_1120.txt")

datL <- datL[-c(1:3)]

dat <- NULL
for (i in 1:5000){
    l <- substr(datL[i], 2, 738)
    dat <- rbind(dat, as.numeric(unlist(strsplit(l, ","))))
}

dat <- as.data.frame(dat)

# Plot
# Startpoint and Endpoint
startp <- 0
endp <- 100
lcolor <- colorRampPalette(c("blue","green"))(endp)
plot(as.numeric(dat[1,]) ~ I(1:36), type="l", col=lcolor[startp],
    ylim=c(0,3))
for (i in startp:endp){
    points(as.numeric(dat[i,]) ~ I(1:36), type="l", col=lcolor[i])
}

# Peaks in time
plot(as.numeric(dat[,18]), col="green", pch=16, ylim=c(.5,2.7))
points(as.numeric(dat[,24]), col="blue", pch=16)
points(as.numeric(dat[,7]), col="red", pch=16)

# TODO persp Plot (3D)
