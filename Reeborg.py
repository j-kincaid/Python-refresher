def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Use a while loop when you don't care about what number in a sequence
# you're in, which is different from iterating through a list using a for loop. 
