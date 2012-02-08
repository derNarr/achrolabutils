

grey <- 0:1023/1023
col <- 0:255/255

dat.col <- expand.grid(R=col, G=col, B=col)

# YUV way of caculating luminance (http://en.wikipedia.org/wiki/YUV)
dat.col$grey <- with(dat.col, 0.299*R+0.114*B+0.587*G)


#dat.col <- dat.col[order(dat.col$grey),]

# take all values, which are near (around 10%) to target value
digits = 4
dat.col.small <- dat.col[round(dat.col$grey, digits) %in% round(grey, digits),]
# take only the first one and dismiss all other
dat.col.small.unique <- dat.col.small[!duplicated(round(dat.col.small$grey, digits)),]

# missing six values
grey[!round(grey, digits) %in% round(dat.col.small.unique$grey, digits)]


# calculate the corresponding integer values (0,255) for RGB
dat.col.small.unique$Rint <- dat.col.small.unique$R*255
dat.col.small.unique$Gint <- dat.col.small.unique$G*255
dat.col.small.unique$Bint <- dat.col.small.unique$B*255
dat.col.small.unique$GREYint <- round(dat.col.small.unique$grey*1023, 0)

# write python code to file
f <- file("grey_dict.py")
writeLines( paste("grey_dict = {\n", with(dat.col.small.unique,
paste(GREYint, ": (", Rint, ",", Gint, ",", Bint, ")", sep="",
collapse=",\n")), "}\n", sep=""), f)
close(f)

