print("Hello World!\nNow!")
print('My name is "Jenny"')

#input function
#cursor a line and Command+/ can highlight the line
print('Hello ' + input("What is your name?" ) + "!")

#calculate the length of the string
#You can put functions inside other functions
print( len( input("What is your name?" ) ) )

#Variables
name = input("What is your name")
length = len(name)
print(length)

#Final Project: Band Name Generator

print("Welcome to the Band Name Generator.")
name1 = input("What's name of the city you grew up in?\n")
name2 = input("What's your pet's name?\n")
print("Your band name could be " + name1 +" "+ name2)
