
#Charactors of Strings
print("Hello"[4])
print("123"+"456")

#number data type
#Integer
print(123 + 456)
123_456_789 #123456789
#Float
3.1415

#Type Checking / Type Conversion

name = input("What is your name?")
num_char = len(name)
print(type(num_char))

print("Your name has " + str(num_char) + " characters")

#Mathematical Operations sign
print(1 + 2)
print(1 - 2)
print(2 * 3)
print(2 / 3)
print(4 ** 2)

#Round numbers

print(8 / 3)
print(8 // 3)
print(round(8 / 3, 2))

#F-string
score = 0
height = 1.6
iswing = True

message = f"Your score is {score}, your height is {height}, your winning is {iswing}"
print(message)


#Final Project: 

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("Hoe many people to split the bill? "))

each_bill = bill * (1 + tip / 100) / people
#r_each_bill = round(each_bill,2)
r_each_bill = "{:.2f}".format(each_bill)

print(type(r_each_bill)) #string

message = f"Each person should pay: ${r_each_bill}"
print(message)