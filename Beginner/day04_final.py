# Rock, Paper and Scissors 石头剪刀布

import random

rock = '''
 rock______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
 paper ____
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
 scissors__
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user > 2 or user < 0:
    print("You typed an invalid number, you lose")
else:
    computer = random.randint(0, 2)
    print(game[user])
    print(f"Computer chose:\n{game[computer]}")

    if user == computer:
        print("It's a draw")
    elif (user - computer == 1) or (user - computer == -2):
        print("You win")
    else:
        print("You lose") 
