import random
import turtle
#martin pettai
#it21
#turtlekt

aken=turtle.Screen()
aken.setup(1000,1000)


nurk=360/5
t=turtle.Turtle()
for x in range(5):
    t.left(nurk)   
    t.forward(50)
    t.left(90)
    for i in range(3):    
        t.forward(100)
        t.left(90)
    t.forward(50)




turtle.exitonclick()

