

# read data
dat0 <- read.table("depth_monitor20120217_1438.txt", sep=",")
names(dat0) <- c("R","G","B","x","y","Y",paste("l", 1:36, sep=""))
dat <- aggregate(as.matrix(dat0) ~ R + G + B, dat0, mean)
for (i in 1:3) dat[,4] <- NULL
names(dat) <- c("R","G","B","x","y","Y",paste("l", 1:36, sep=""))
dat <- dat[order(dat$R, dat$G, dat$B),]

plot(dat$Y)
rownames(dat) <- NULL

