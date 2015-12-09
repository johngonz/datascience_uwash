# Run this code periodically

#T
if(!require(installr)) {install.packages("installr"); require(installr)} #load / install+load installr
updateR()


# This code updates all R packages
x <- packageStatus(repositories="http://cran.r-project.org/src/contrib")
st <- x$avai["Status"]
install.packages(rownames(st)[which(st$Status=="not installed")]) 