
def greet():
    print("Hello")
    print("How are you")
    print("You look so happy")

greet()

#function with inputs
def greet_with_people(people):
    print(f"Hello, {people}")
    print("How are you")
    print("You look so happy")

#Important: 
#Parameters: the name of variables, when define function, create parameters
#Argument: what's input, when call function, give arguments.
#Parameter gets assigned from Arguments; Argument assigned to Parameters
people = input("Who you want to greet? ") 
greet_with_people(people)
greet_with_people("Angela")

#function with muti-inputs

#parameters are positional
def greet(name,location):
    print(f"Hello, {name}.")
    print(f"What's like in {location}?")

#Position Arguments
#Keyword Arguments
greet(name = "Jenny", location = "London")


# Identify "Parameters" and "Arguments"
import math

#function just needs Parameters
def paint_calc (height, width, cover):
    num = math.ceil (height * width / cover)
    print(f"You'll need {num} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

#height, width, cover are "Parameters"
#test_h, test_h, coverage are "Arguments"
paint_calc(height=test_h, width=test_w, cover=coverage)

#prime number checker
def prime_checker(number):

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime  = False
            
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)