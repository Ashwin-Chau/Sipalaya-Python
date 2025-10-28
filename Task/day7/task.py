# Project: Sissor,Papper, Rock game

import random

print("Welcome to Sissor, Paper, Rock game!!!")
print('''
        Choose one the following
      S-Scissor | R- Rock | P-Paper

      Rule :
      S beats P
      P beats R
      R beats S
        ''')

user=input("Enter your valid choices['S','P','R']: ").strip().upper()
computer=random.choice(['S','P','R'])

print(f"Your choice is {user}")
print(f"Computer choice is {computer}")

if (user == 'S' and computer == 'P') or (user == 'P' and computer == 'R') or \
    (user == 'R' and computer == 'S'):
    print("You won the game !!!")

elif user == computer:
    print("Draw")

elif user not in ['S','P','R']:
    print("Invalid input, please try again")

else:
    print("Computer won !!!")

