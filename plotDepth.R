# plotDepth.R
# plot diagnostic plots for monitor depth
#
# input: depth_monitor*.txt
# output: depth_monitor.pdf
#
# content: (1) Read data
#
# last mod: 2011-11-16, NU

###### (1) Read data ######

path <- "U:/phd/visionlab/achrolabutils"    # location of achrolabutils
setwd(paste(path, "/achrolab/calibdata/measurements/", sep=""))
files <- dir(pattern="depth_monitor[0-9][0-9].*\\.txt")
file <- tail(files, 1)  # last measurement

dat <- read.table(file, sep=",")
names(dat) <- c("R","G","B","x","y","Y")
#dat$R <- factor(dat$R)
#dat$G <- factor(dat$G)
#dat$B <- factor(dat$B)

plot(dat$Y)

dat3 <- dat[dat$R == dat$G & dat$G == dat$B,]
plot(dat3$Y)

dat2 <- dat[order(dat$Y),]

plot(dat2$Y)
plot(round(dat2$Y[22000:22700], 2))

# TODO 
# analytical plots
pdf("depth_monitor.pdf", width=6, height=5)
id <- seq(length(input)/2, length(input) + 50, 1)
par(mfrow=c(1,2))
plot(xyY_Y ~ input, xlab="Input", ylab="Luminance")
plot(xyY_Y[id] * 72 ~ input[id], xlab="Input", ylab="Luminance")

dev.off()

