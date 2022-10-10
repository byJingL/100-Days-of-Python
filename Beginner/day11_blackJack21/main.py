
from art import logo
import random
import os



def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    score = sum(cards)
    if score == 21 and len(cards) == 2: # do not forget just 2 cards
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score

def compare(user, computer):
    if user == computer:
        return "Draw 😢"
    elif computer == 0:
        return "Lose, opponent has Blackjack! 😱"
    elif user == 0:
        return "You win with Blackjack! 😎"
    elif user >21:
        return "You went over. You lose 😭"
    elif computer > 21:
        return "opponent went over. You win 😊"
    elif user > computer:
        return "You win 😊"
    else:
        return "You lose 😭"

def play_game():

    os.system("clear")
    print(logo)

    user_cards = []
    computer_cards = []

    for i in range(0,2): # for _ in random(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())    


    game_over = False

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")   


        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True

        else:
            ask = input("Type 'y' to another card, type 'n' to pass: ")

            if ask == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
