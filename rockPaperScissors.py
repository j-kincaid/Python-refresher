from multiprocessing.dummy import RLock
import random

print("Welcome to the SHOWDOWN.\n")
print(" Rock wins against Scissors.\n Scissors wins against Paper.\n Paper wins against Rock.\n")
user_play = int(input(" What do you choose?\n Type 0 for Rock, 1 for Paper, or 2 for Scissors."))


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Paper
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Scissors
'''
plays = [rock, paper, scissors]

computer_play = random.choice(plays)

if user_play == 0:
    print(f"You chose {rock} \n We chose: {computer_play}")
    if computer_play == plays[2]:
        print(f"Rock beats Scissors. \n You win!")
    elif computer_play == plays[1]:
        print(f"Paper beats Rock.\n You lose!")
    else:
        print(f"Rock equals Rock.\n It's a tie!")

elif user_play == 1:
    print(f"You chose{paper}\n We chose: {computer_play}")
    if computer_play == plays[0]:
        print(f"Paper beats Rock.  \n You win!")
    elif computer_play == plays[2]:
        print(f"Scissors beats Paper. \n You lose!")
    else:
        print(f"Paper equals Paper.\n It's a tie!")
else:
    print(f"You chose{scissors} \n We chose:{computer_play}")
    if computer_play == plays[2]:
        print(f"Scissors equals Scissors. \n It's a tie!")
    elif computer_play == plays[1]:
        print(f"Scissors beats Paper. \n You win!")
    else:
        print(f"Rock beats Scissors. \n You lose!")