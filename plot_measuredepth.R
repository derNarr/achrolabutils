#!/usr/bin/env Rscript (python)
# -*- encoding: utf-8 -*-
# ./plot_just_measure.R
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# plots for behavior of luminance of tubes over time
#
# content: (1) Plot most recent measurement
#
# input: justmeasure_color_20120519_1121.txt
# output: /figures/tubes_over_time.pdf
#
# last mod 2012-05-21, NU

#setwd("Z:/AG_Heller/calibdata/measurements")

###### (1) Plot most recent measurement ######
i=1
files <- dir(pattern="gdata[0-9][0-9].*\\.txt")

plot(x=1, y=1, xlim=c(0,400), ylim=c(0,40), type="n")
for (file in files){
dat <- read.table(file,header=TRUE)

#par(new=T, fig=c(0,1,0,1))
#x <- seq(1,length(dat[,1]),by=100)
points(y=dat$Y, x=dat$gray_1, xlab="gray color", ylab="Luminance", pch=4, col=colors()[(i+50)*5])
i=i+1
}

dev.print(device=postscript, "graph1.eps")
#pdf(paste("testpdf.pdf", sep=""), height=2.75, width=10)
#dev.off()


