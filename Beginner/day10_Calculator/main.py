from art import logo

#Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, #不用写parameters
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():

    print(logo)

    num1 = float(input("What's the first number? "))
    for key in operations:
        print(key)

    be_continue = True

    while be_continue:
        operate = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        function = operations[operate]
        result = function(num1, num2)
        print(f"{num1} {operate} {num2} = {result}")
        
        ask = input(f"Type 'yes' to continue calculating with {result}, Type 'new' to start a new calculation, or type 'no' to exit.: ")
        if ask == "yes":
            num1 = result
        elif ask == "new":
            be_continue = False
            calculator()
        else:
            be_continue = False
            print("Thank you for using this calculator")

calculator()







    
    