# TODO completely
# get python objects into R -- maybe there is a better way TODO
xyY_x = robjects.FloatVector([x[0] for x in xyY_list])
xyY_y = robjects.FloatVector([x[1] for x in xyY_list])
xyY_Y = robjects.FloatVector([x[2] for x in xyY_list])
input = robjects.FloatVector(colorlist)
R("xyY_x <- " + xyY_x.r_repr())
R("xyY_y <- " + xyY_y.r_repr())
R("xyY_Y <- " + xyY_Y.r_repr())
R("input <- " + input.r_repr())
R('''
lum_tab <- data.frame(color=paste("color", seq(50,169,1),
    sep=""),input, xyY_Y) 
''')

# save all created R objects to file resolution_device.RData
R('save(list=ls(), file="spot_resolution_' + 
        time.strftime("%Y%m%d_%H%M") + '.RData")')
        
print("Data read into R")
 
# analytical plots
R(' pdf("spot_resolution_' + time.strftime("%Y%m%d_%H%M")
    +'.pdf", width=6, height=5)')
R('''
id <- seq(length(input)/2, length(input) + 50, 1)
par(mfrow=c(1,2))
plot(xyY_Y ~ input, xlab="Input", ylab="Luminance")
plot(xyY_Y[id] * 72 ~ input[id], xlab="Input", ylab="Luminance")

dev.off()
'''
