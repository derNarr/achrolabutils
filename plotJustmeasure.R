# plotJustmeasure.R
# plots for behavior of luminance of tubes over time
#
# input: justmeasure_color_20120519_1121.txt
# output: /figures/tubes_over_time.pdf
#
# content: (1) Plot most recent measurement
#          (2) TODO -- what was it again?
#
# last mod 2012-05-21, NU

setwd("Z:/AG_Heller/calibdata/measurements")

###### (1) Plot most recent measurement ######

files <- dir(pattern="justmeasure_color_[0-9][0-9].*\\.txt")
file <- tail(files, 1)  # last measurement

dat <- read.table(file, sep=",", skip=3)

names(dat) <- c("x","y","Y")

pdf(paste("../figures/tubes_over_time_", substr(file, 19, 26), ".pdf",
    sep=""), height=2.75, width=10)
par(mfrow=c(1,4), mai=c(.5,.5,.1,.1), mgp=c(2.7,1,0))

plot(dat$Y ~ I(1:50000), xlab="# measurement", ylab="Luminance")

id <- 1:2000
plot(dat$Y[id] ~ id, xlab="# measurement", ylab="Luminance")
abline(h=22.2, col="red")

id <- 2000:8000
plot(dat$Y[id] ~ id, xlab="# measurement", ylab="Luminance")
abline(h=c(22.5, 23.5), col="red")

id <- 8000:50000
plot(dat$Y[id] ~ id, xlab="# measurement", ylab="Luminance")
abline(h=c(23.5, 23.7, 23.9), col="red")

dev.off()

###### (2) TODO -- what was it again? ######

# TODO --> what does it do, is it still useful?
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
