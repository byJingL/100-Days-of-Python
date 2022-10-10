###########DEBUGGING#####################

# Tip 1: Describe the problem, which of assumptions is false
# Describe Problem
def my_function():
    for i in range(1, 21): #Wrong: "range(1, 20)" [1,21)
        if i == 20:
            print("You got it")
my_function()

# Tip 2: Reproducing the bug
# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) #Wrong: "randint(1, 6)" [1, 6]
print(dice_num)
print(dice_imgs[dice_num])

# Tip 3: Play Computer and Evaluate Each Line
# Play Computer
year = int(input("What's your year of birth? "))
if year > 1980 and year <= 1994:# Wrong "year < 1994" 
    print("You are a millenial.")
elif year > 1994: 
    print("You are a Gen Z.")

# Tip 4: Fixing Errors and Watching for Red Underlines
# Fix the Errors One by One
# Copy the error-hit to the StackoverFlow
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

# Tip 5: Squash bugs with a print() Statement
# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page = int(input("Number of words per page: ")) #Wrong "=="
print(word_per_page)
total_words = pages * word_per_page
print(total_words)

# Tip 6: Use a Debugger
# Python step by Step web
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])


