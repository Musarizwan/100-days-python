def turn_around():
    turn_left()
    turn_left()
def turn_rigth():
    turn_left()
    turn_left()
    turn_left()
while at_goal()!=True:
    if right_is_clear():
        turn_rigth()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()