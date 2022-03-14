#ül2

import turtle
import random

#akna seaded
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Harjutus02")
angle = 0
k1 = turtle.Turtle()

for i in range(5):
    k1.rt(angle)
    k1.forward(100)
    angle=144
    

angle = 0
k1 = turtle.Turtle()

for i in range(3):
    k1.rt(angle)
    k1.forward(100)
    angle=120
    
turtle.exitonclick()