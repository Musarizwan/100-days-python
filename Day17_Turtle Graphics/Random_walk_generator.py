import turtle as t
import random
tim=t.Turtle()
tim.shape("turtle")

t.colormode(255)
def color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

directions=[0,90,180,270]
tim.speed("fastest")
for _ in range(100):
    tim.width(10)
    tim.forward(30)
    tim.color(color())
    tim.setheading(random.choice(directions))















screen=t.Screen()
screen.exitonclick()