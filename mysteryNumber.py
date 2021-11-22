import random


#  """
#  Feedback: The first printed statement should clue the user 
#  in to what the program is doing. If they choose 1 in the beginning
#  then the random number will be picked between 1 and 1, it
#  will always be 1. It should say something more like
# A random number will be picked between 1 and the number you input 
# or something along those lines.
#  """  
top_of_range = input("Thank you for playing the Mystery number game! Type a number between 1 and 100: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

rNum = random.randint(1, top_of_range)
guesses = 0
print('You just chose a number. That is the greatest of the numbers that will be randomized. Try to guess the random number in 7 guesses or fewer.')
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    if user_guess == rNum:
        print("Good Job! You guessed the number!")
        break
    elif user_guess > rNum:
        print("You were above the number!")
    else:
        print("That's below the number!")
print("You guessed it in", guesses, "guesses")


