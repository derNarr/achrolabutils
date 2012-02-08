
dat <- read.table("calibdata/measurements/depth_monitor20120208_1918.txt", sep=",")

names(dat) <- c("R","G","B","x","y","Y",paste("l", 1:36, sep=""))

dat$grey <- factor(round(1023*with(dat, 0.299*R/255 + 0.587*G/255 + 0.114*B/255)))

Ymean <- with(dat, tapply(Y, grey, mean))

# Luminance steps
plot(Ymean)
plot(dat$Y)

# One Spectrum
plot(as.numeric(dat[1,7:42]) ~ I(1:36), type="l")



