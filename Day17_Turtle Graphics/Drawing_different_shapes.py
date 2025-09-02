import turtle as t
import random
tim=t.Turtle()
tim.shape("turtle")

colors=["red","blue","green","yellow","pink","black","purple"]
def draw_shapes(num_sides):
    for _ in range(num_sides):
        angle=360/num_sides
        tim.forward(100)
        tim.right(angle)
for i in range(3,11):
    tim.color(random.choice(colors))
    draw_shapes(i)


screen=t.Screen()
screen.exitonclick