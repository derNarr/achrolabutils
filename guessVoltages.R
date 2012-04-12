# if anything misses check tubes_spectra_plot.R

guessVoltages <- function(Y) {
    Yred <- 6.173447/(6.173447+22.92364+4.036948)*Y
    Ygreen <- 22.92364/(6.173447+22.92364+4.036948)*Y
    Yblue <- 4.036948/(6.173447+22.92364+4.036948)*Y

    inv <- function(y, p) {-log((y - p[1])/(p[2]-p[1]))/exp(p[3])}

    pR <- summary(nlsR)$par[,1]
    pG <- summary(nlsG)$par[,1]
    pB <- summary(nlsB)$par[,1]
    
    volR <- inv(Yred,   pR)
    volG <- inv(Ygreen, pG)
    volB <- inv(Yblue,  pB)
    
    voltages <- data.frame(Y=Y, volR=volR, volG=volG, volB=volB)
    voltages
}

