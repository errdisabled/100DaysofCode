# import the random module
import random

# ascii art for each choice
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# this will map to computer_choice easily
all_choices = [rock, paper, scissors]

# gather the users choice input
user_choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# print the user input
if user_choice >= 3 or user_choice < 0:
    print("You have chosen an invalid number. You lose!")
else:
    print(all_choices[user_choice])

# gather the computer choice and print it
    computer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{all_choices[computer_choice]}")

# set up the scoring
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
