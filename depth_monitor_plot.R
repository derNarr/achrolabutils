
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

# One Spectrum
plot(as.numeric(dat[1000,7:42]) ~ I(1:36), type="l")



