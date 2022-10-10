# Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level

password1  = "" #use string: password += string

for num in range(1, nr_letters+1):
    letter = letters[random.randint(0, 25)]
    password1 += letter
for num in range(1, nr_symbols+1):
    password1 += random.choice(symbols) #use easier function
for num in range(1, nr_numbers+1):
    password1  += random.choice(numbers)

print(password1)

#Hard Level
#"How to change the order of item in a list"

password2  = [] #use list

for num in range(1, nr_letters+1):
    letter = letters[random.randint(0, 25)]
    password2.append(letter)
for num in range(1, nr_symbols+1):
    #use easier function
    password2.append(random.choice(symbols))
for num in range(1, nr_numbers+1):
    password2.append(random.choice(numbers))

# print(password2)
# print(*password2, sep = "")

random.shuffle(password2)
print(*password2, sep = "")

result = ""
for char in password2:
    result += char

print(f"Your password is: {result}")
