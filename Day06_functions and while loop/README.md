# Maze Solver - Reeborg's World

This project is a solution to the **Maze challenge** in [Reeborg's World](https://reeborg.ca/).  
It uses **while loops**, **functions**, and **conditional statements** to navigate the maze and reach the goal.

## How It Works
The logic follows the **right-hand rule** for maze solving:
1. If there is a path on the right, turn right and move forward.
2. If the path in front is clear, move forward.
3. Otherwise, turn left.

## Code Overview
```python
def turn_around():
    turn_left()
    turn_left()

def turn_rigth():
    turn_left()
    turn_left()
    turn_left()

while at_goal() != True:
    if right_is_clear():
        turn_rigth()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

## Skills Learned
- While loops
- Functions
- Conditional statements
- Problem-solving logic
