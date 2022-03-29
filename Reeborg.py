def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# number_of_hurdles = 6

# while number_of_hurdles > 0: 
#     if at_goal() == False:
#         jump()
#         number_of_hurdles -= 1

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

# Use a while loop when you don't care about what number in a sequence
# you're in, which is different from iterating through a list using a for loop. 
