# xyyToRgb.R

# Funktion to transform xyY values into RGB

# cf. http://brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html

#

# last mod: Jun/16/2011



# xyY to XYZ

conv <- function(x, y, Y){

    X <- x*Y/y

    Y <- Y

    Z <- (1-x-y)*Y/y

    output <- as.data.frame(cbind(X=X, Y=Y, Z=Z))

    output

    }



# xyY tp RGB

xyyToRgb <- function(dat){

    dat <- conv(dat[,1], dat[,2], dat[,3])

    mat <- matrix(c( 3.1338561, -1.6168667, -0.4906146, 

                    -0.9787684,  1.9161415,  0.0334540,

                     0.0719453, -0.2289914,  1.4052427), 3, 3, byrow=T)

    output <- NULL

    for (i in 1:nrow(dat)){

        output <- rbind(output, t(mat %*% as.numeric(dat[i,])))

    colnames(output) <- c("R","G","B")

    }

    output

}



