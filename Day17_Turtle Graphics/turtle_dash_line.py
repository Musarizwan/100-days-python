import turtle as t
import random
tim=t.Turtle()
tim.shape("turtle")
for _ in range(5):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



screen=t.Screen()
screen.exitonclick