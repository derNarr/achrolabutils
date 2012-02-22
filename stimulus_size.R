# stimulus_size.R
#
# content: (1) visual angle to cm
#          (2) cm to pixel
#          (3) compute stimulus sizes
#
# last mod: Feb/22/2012

###### (1) visual angle to cm ######
vis2cm <- function(alpha, r=120){
    cm <- 2*r*tan(alpha/2 * pi/180)
    cm
    }

cm2vis <- function(cm, r=120){
    vis <- 2*atan(0.5*cm/r) * 180/pi
    vis
    }

###### (2) cm to pixel ######

# one pixel of EIZO GS320 has the size: 0.2115mm (see Manual)
cm2pix <- function(cm){
    pix <- cm/0.02115
    pix
    }

pix2cm <- function(pix){
    cm <- 0.02115*pix
    cm
    }

###### (3) compute stimulus sizes ######

cm2pix(vis2cm(1))       # 99.02829
cm2pix(vis2cm(8))       # 793.4957

# current setting
cm2vis(pix2cm(80))      # 0.8078571
cm2vis(pix2cm(190))     # 1.918513



