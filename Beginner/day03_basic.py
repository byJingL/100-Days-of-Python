number = int(input("Which number do you want to check? "))

test = number % 2
if test == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

#Nested Condition Statement
#multiple if
bill = 0
height = int(input("Please enter your height in cm: "))

if height < 120:
    print("Sorry, you can't ride")
else:
    print("You can ride.")
    age = int(input("Please enter your age: "))

    if age >= 45 and age <= 55:
        bill = 0
    elif age >18:
        bill += 12
    elif age <12:
        bill += 5
    else:
        bill += 7
    
    photo = input("Want a photo? Y or N. ")
    if photo == "Y":
        bill += 3
    
    print(f"Your ticket price is ${bill}")

#Love Calculator: Logic Operator, Lowercase function, Count function
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
n = (name1 + name2).lower()

score_true = n.count('t') + n.count('r') + n.count('u') + n.count('e')
score_love = n.count('l') + n.count('o') + n.count('v') + n.count('e') 
score = int(str(score_true)+str(score_love))

if (score < 10) or (score > 90):
    message = ", you go together like coke and mentos."
elif (score >= 40) and (score <= 50):
    message = ", you are alright together."
else:
    message = "."

print(f"Your score is {score}" + message)