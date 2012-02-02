# plotDepth2.R
# plot diagnostic plots for monitor depth
#
# input: depth_monitor*.txt
# output: depth_monitor.pdf
#
# content: (1) Read data
#
# last mod: 2011-11-18 KS

###### (1) Read data ######

path <- "/home/kfs-studium/Dokumente/arbeit/PI/achrolabutils"    # location of achrolabutils
path.data <- paste(path, "/achrolab/calibdata/measurements/monitor/", sep="")

setwd(path)
# dataset 1
files <- dir(path.data, pattern="depth_monitor[0-9][0-9].*\\.txt")
file <- tail(files, 1)  # last measurement
dat <- read.table(paste(path.data, file, sep=""), sep=",")
names(dat) <- c("R","G","B","x","y","Y")

#dataset 2
load(paste(path.data, "test_calibration_Monitor20101011_1413.RData",
    sep=""))


Y10 <- dat$Y
Y10 <- Y10[order(Y10)]
Y10 <- Y10[Y10 > 60 & Y10 < 70]

Y8 <- xyY_Y*72
Y8 <- Y8[order(Y8)]
Y8 <- Y8[Y8 > 60 & Y8 < 70]

pdf("depth_monitor.pdf", width=6, height=5)
plot(1:length(Y10)/length(Y10), Y10, xlab="Ordered Input",
    ylab="Luminance", pch=".")
points(1:length(Y8)/length(Y8), Y8, col="blue", pch=".")
dev.off()

Y10z <- Y10[Y10 > 60 & Y10 < 62]
Y8z <- Y8[Y8 > 60 & Y8 < 62]

pdf("depth_monitor_zoom.pdf", width=6, height=5)
plot(1:length(Y10z)/length(Y10z), Y10z, xlab="Ordered Input",
    ylab="Luminance", pch=".")
points(1:length(Y8z)/length(Y8z), Y8z, col="blue", pch=".")
dev.off()


