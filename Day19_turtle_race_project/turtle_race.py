from turtle import Turtle,Screen
import random

screen=Screen()
is_race_on=False
screen.setup(500,400)
user_bet=screen.textinput(title="Make your Bet",prompt="Which turtle will win the race? Write the color:red?blue?green?purple?black?orange? ")
colors=["red","blue","green","purple","black","orange"]
y=[-70,-40,-10,20,50,80]
all_turtles=[]
for turtle_index in range(0,6):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235,y=y[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>235:
            winning_color=turtle.pencolor()
            if user_bet==winning_color:
                print(f"You have won,the winner was {winning_color}")
            else:
                print(f"You have lost,the winner was {winning_color}")
            is_race_on=False
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)