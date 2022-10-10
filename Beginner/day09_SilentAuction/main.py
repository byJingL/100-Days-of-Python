from art import logo
import os

def add_person(user_name, user_bid):
    auction[user_name] = user_bid

def find_highest_bidder(bidding_record):
    biggest_amount = 0
    for person in bidding_record:
        bid_amount = bidding_record[person]
        if bid_amount > biggest_amount:
             biggest_amount = bid_amount
             winner = person
    print(f"The winner is {winner} with a bid of ${biggest_amount}.")



print(logo)
print("Welcome to the secret auction program.")

auction = {}
any_other = True

while any_other:
    name = input("What's your name?: ")
    bid = float(input("What's your bid?: $"))
    add_person(user_name = name, user_bid = bid)

    ask = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if ask == "no":
        any_other = False

    os.system("clear")

print(auction)

#Solution 1
find_highest_bidder(auction)

#Solution 2
#🌹EasyFunction: Get the biggest value in dict
max_person = max(auction)

print(f"The winner is {max_person} with a bid of ${auction[max_person]}.")

