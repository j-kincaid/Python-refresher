def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif right_is_clear():
        move()
    else:
        turn_left()
        

# Use a while loop when you don't care about what number in a sequence
# you're in, which is different from iterating through a list using a for loop. 
