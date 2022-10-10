# Many class(bluepoint) in this module
from turtle import Turtle, Screen

# timmy: object; Turtle(): class
timmy = Turtle()
print(timmy)

# shape(), color(): Method
timmy.shape("turtle")
timmy.color("red", "coral")
timmy.circle(50)

# my_screen: object; Screen(): class
my_screen = Screen()

# canvheight: Attribute
print(my_screen.canvheight)
# exitonclick(): Method
my_screen.exitonclick()
