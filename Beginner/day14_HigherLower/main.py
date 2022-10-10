
import art
import random
from game_data import data
import os


def choose_data():
    return random.choice(data)

def check(a, b):
    if a == b:
        b = random.choice(data)

def data_display():
    print(f"Compare A: {compare_data['A']['name']}, a {compare_data['A']['description']}, from {compare_data['A']['country']}")
    print(art.vs)
    print(f"Compare B: {compare_data['B']['name']}, a {compare_data['B']['description']}, from {compare_data['B']['country']}")

def compare(data, choice):
    user_count = int((data[choice]["follower_count"]))
    biggest_count = 0
    for key in data:
        count = int(data[key]["follower_count"])
        if count > biggest_count:
            biggest_count = count

    if user_count == biggest_count:
        return 0
    else:
        return 1

def result_display(massage):
    os.system("clear")
    print (art.logo)
    print(message)


compare_data = {}
# compare_data["A"] = choose_data()
compare_data["B"] = choose_data()
# check(compare_data["A"], compare_data["B"])

score = 0
game_finish = False

os.system("clear")
print (art.logo)

while not game_finish:

    compare_data["A"] = compare_data["B"]
    compare_data["B"] = choose_data()
    check(compare_data["A"], compare_data["B"])

    data_display()
    
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    result = compare(compare_data, user_choice)

    if result == 0:
        score += 1
        message = f"You're right! Current score: {score}."

    if result == 1:
        game_finish = True
        message = f"Sorry, That's Wrong! Fianl score: {score}."

    result_display(message)
