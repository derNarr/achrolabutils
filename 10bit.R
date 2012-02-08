

color <- 1:255/255
grey <- 1:1023/1023

# Create all combinations
dat <- expand.grid(r=color,g=color,b=color)
# Calculate grey results for all combinations
dat$grey <- with(dat, r*.299 + g*.587 + b*.114)

# oder data after grey
# (not really necessary)
dat <- dat[order(dat$grey),]

# Find elements next to grey in dat
reslist <- NULL
for (i in 1:1024){
    x <- dat[which.min(abs(dat$grey - grey[i])),]
    reslist <- rbind(reslist, x)
}

# save rdata
save(dat,reslist, file="10bit.rdata")
write.table(reslist, file="10bit_reslist.txt")
write.table(dat, file="10bit_dat.txt")

# calculate the corresponding integer values (0,255) for RGB
reslist$Rint <- reslist$r*255
reslist$Gint <- reslist$g*255
reslist$Bint <- reslist$b*255
reslist$GREYint <- round(reslist$grey*1023, 0)


# write python code to file
f <- file("10bit.py")
writeLines( paste("grey_dict = {\n", with(reslist,
paste(GREYint, ": (", Rint, ",", Gint, ",", Bint, ")", sep="",
collapse=",\n")), "}\n", sep=""), f)
close(f)

