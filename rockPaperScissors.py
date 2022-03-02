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
import random
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
computer_play = random.choice(0, 1, 2)

if user_play == 0:
    print(f"You chose{rock}")

elif user_play == 1:
    print(f"You chose{paper}")

else:
    print(f"You chose{scissors}")

if computer_play == 0:
    print(f"{rock} beats {scissors}")
elif computer_play == 1:
    print(f"{paper} beats {rock}")
else:
    print("It'\s a tie.")