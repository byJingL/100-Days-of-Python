#List
states_of_US = ["Delaware", "Pennsylvania", "NewJesey"]

states_of_US[1] = "pencilvania"

states_of_US.append("JennyLand")
states_of_US.extend([])

print(states_of_US[2])
print(states_of_US[-1])

#Nested List

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ") #string

column = int(position[0])
row = int(position[1])
map[row - 1][column - 1] = "X" #same as matrix

print(f"{row1}\n{row2}\n{row3}")


#Random Pike Game
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") # Split string method

length = len(names)
choice = random.randint(0, length-1) #index = len - 1

print(f"{names[choice]} is going to buy the meal today!") 

#more simple random function
print(f"{random.choice(names)} is going to buy the meal today!")

#Nested List

fruit = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale,Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruit, vegetables]

print(dirty_dozen)
