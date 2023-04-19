#CHECKING OUT MTCARS

library(database)
#load data
data(mtcars)
#view first 5 rows
?mtcars
#load ggplot package
library(ggplot2)
#create a scatterplot of displacement (disp) and miles per gallon (mpg)
ggplot(aes(x=disp, y=mpg),data=mtcars)+geom_point()
