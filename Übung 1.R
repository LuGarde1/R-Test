library (ggplot2)
library (sportsdata)
gymnastics
ggplot(gymnastics, aes(x = height, y = weight, colour = sex)) +
  geom_point() +
  labs(
    x = "height of gymnasts",
    y = "weights of gymnasts", 
    title = " height and weight datas of gymnasts") 




