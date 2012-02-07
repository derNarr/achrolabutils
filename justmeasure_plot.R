
# Info colorpalette
plot(1:100, col=colorRampPalette(c("blue","green"))(100), type="p", pch=16)

#setwd("D:/Experimente/achrolabutils")

datL <- readLines("justmeasure_20120207_1345.txt")

datL <- datL[-c(1:3)]

dat <- NULL
for (i in 1:5000){
    l <- substr(datL[i], 2, 738)
    dat <- rbind(dat, as.numeric(unlist(strsplit(l, ","))))
}

dat <- as.data.frame(dat)

# Plot
# Startpoint and Endpoint
startp <- 1
endp <- 100
lcolor <- colorRampPalette(c("blue","green"))(endp)
plot(as.numeric(dat[1,]) ~ I(1:36), type="l", col=lcolor[startp])
for (i in startp:endp){
    points(as.numeric(dat[i,]) ~ I(1:36), type="l", col=lcolor[i])
}

# TODO persp Plot (3D)
