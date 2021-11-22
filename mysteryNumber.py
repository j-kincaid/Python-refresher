import random

top_of_range = input("Type a number between 1 and 10: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

rNum = random.randint(1, top_of_range)
guesses = 0
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

