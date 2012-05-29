#!/usr/bin/env Rscript
# -*- encoding: utf-8 -*-
# ./plot_calibration.R
#
# (c) 2010 Konstantin Sering, Nora Umbach, Dominik Wabersich
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: plots luminance curves for each channel (data and fitted
# curve).
#
# input: calibration_tubes*.txt
# output: --
#
# created
# last mod 2012-05-29 NU

# TODO
# load data
# ... I have to see what the file looks like first ... (Has to wait till
# laboratory is working again.)

# plot calibration curves and data points for each channel
pdf("calibdata/measurments/calibration_curves_rgb_tubes.pdf",
    width=9, height=8) 

par(mfrow=c(3,3))
len3 <- floor(length(voltage_r)/3)
# only red voltage
plot(voltage_r[1:len3], rgb_r[1:len3], col="red", ylim=c(0,256),
    pch=19,
    main="red channel vs. voltage\ndata points and
    calibration curve",
    xlab="voltage", ylab="red rgb-value")
points(voltage_r[1:len3], rgb_g[1:len3], pch=21, col="green")
points(voltage_r[1:len3], rgb_b[1:len3], pch=21, col="blue")
#curve(p_r[1] + p_r[2]*x, col="red", add=T, xlab="", ylab="")
curve(p_r[1] + (p_r[2] - p_r[1])*exp(-exp(p_r[3])*x), col="red",
    add=T, xlab="", ylab="")

# only green voltage
plot(voltage_g[(len3+1):(2*len3)], rgb_g[(len3+1):(2*len3)], 
    col="green", ylim=c(0,256), pch=19,
    main="green channel vs. voltage\ndata points and
    calibration curve",
    xlab="voltage", ylab="green rgb-value")
points(voltage_g[(len3+1):(2*len3)], rgb_r[(len3+1):(2*len3)], pch=21,
      col="red")
points(voltage_g[(len3+1):(2*len3)], rgb_b[(len3+1):(2*len3)], pch=21,
      col="blue")
#curve(p_g[1] + p_g[2]*x, col="green", add=T, xlab="", ylab="")
curve(p_g[1] + (p_g[2] - p_g[1])*exp(-exp(p_g[3])*x), col="green",
    add=T, xlab="", ylab="")

# only blue voltage
plot(voltage_b[(2*len3+1):(3*len3)], rgb_b[(2*len3+1):(3*len3)],
    col="blue", ylim=c(0,256), pch=19,
    main="blue channel vs. voltage\ndata points and
    calibration curve",
    xlab="voltage", ylab="blue rgb-value")
points(voltage_b[(2*len3+1):(3*len3)], rgb_g[(2*len3+1):(3*len3)], 
    pch=21, col="green")
points(voltage_b[(2*len3+1):(3*len3)], rgb_r[(2*len3+1):(3*len3)], 
    pch=21, col="red")
#curve(p_b[1] + p_b[2]*x, col="blue", add=T, xlab="", ylab="")
curve(p_b[1] + (p_b[2] - p_b[1])*exp(-exp(p_b[3])*x), col="blue",
    add=T, xlab="", ylab="")

# residual plots free y-scale
#pred_r <- p_r[1] + p_r[2]*voltage_r
#pred_g <- p_g[1] + p_g[2]*voltage_g
#pred_b <- p_b[1] + p_b[2]*voltage_b

pred_r <- p_r[1] + (p_r[2] - p_r[1])*exp(-exp(p_r[3])*voltage_r)
pred_g <- p_g[1] + (p_g[2] - p_g[1])*exp(-exp(p_g[3])*voltage_g)
pred_b <- p_b[1] + (p_b[2] - p_b[1])*exp(-exp(p_b[3])*voltage_b)

resid_r <- rgb_r - pred_r
resid_g <- rgb_g - pred_g
resid_b <- rgb_b - pred_b

plot(voltage_r[1:len3], resid_r[1:len3], pch=19, col="red",
    type="h",
    main="residuals (free y-axis)", xlab="voltage", ylab="resid")
abline(h=0)
plot(voltage_g[(len3+1):(2*len3)], resid_g[(len3+1):(2*len3)], 
    pch=19, col="green", type="h",
    main="residuals (free y-axis)", xlab="voltage", ylab="resid")
abline(h=0)
plot(voltage_b[(2*len3+1):(3*len3)], resid_b[(2*len3+1):(3*len3)], 
    pch=19, col="blue", type="h",
    main="residuals (free y-axis)", xlab="voltage", ylab="resid")
abline(h=0)

# residual plots fixed y-scale
plot(voltage_r[1:len3], resid_r[1:len3], pch=19, col="red",
    ylim=c(-10,10), type="h",
    main="residuals (fixed y-axis)", xlab="voltage", ylab="resid")
abline(h=0)
plot(voltage_g[(len3+1):(2*len3)], resid_g[(len3+1):(2*len3)], 
    pch=19, col="green", ylim=c(-10,10), type="h",
    main="residuals (fixed y-axis)", xlab="voltage", ylab="resid")
abline(h=0)
plot(voltage_b[(2*len3+1):(3*len3)], resid_b[(2*len3+1):(3*len3)], 
    pch=19, col="blue", ylim=c(-10,10), type="h",
    main="residuals (fixed y-axis)", xlab="voltage", ylab="resid")
abline(h=0)

dev.off()

