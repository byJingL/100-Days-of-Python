
from art import logo
import random
import os

# global scop
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL_TURNS
    if level == "hard":
        return HARD_LEVEL_TURNS


def compare(user, computer, attemps):
    if user == computer and attemps  != 0:
        return 0
    elif user > computer and attemps != 1:
        return "Too high.\nGuess again"
    elif user < computer and attemps != 1:
        return "Too low.\nGuess again"
    elif user > computer and attemps == 1:
        return "Too high.\nYou've run out of guesses, you lose!"
    elif user < computer and attemps == 1:
        return "Too low.\nYou've run out of guesses, you lose!"

    
def game():

    os.system("clear")
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_num = random.choice(range(1,101))
    print(f"Pssst, the correct answer is {computer_num}")

    attemps = set_difficulty()

    game_over = False

    while not game_over:

        print(f"You have {attemps} attempts remaining to guess the number.")
        user_number = int(input("Make a guess: "))

        compare_result = compare(user_number, computer_num, attemps)

        attemps -= 1 # dont have block scope
        
        if  compare_result == 0:
            game_over = True
            print(f"You got it! The answer was {user_number}.")
        else:
            print(compare_result)

        if attemps == 0:
            game_over = True
            # print("You've run out of guesses, you lose!")

