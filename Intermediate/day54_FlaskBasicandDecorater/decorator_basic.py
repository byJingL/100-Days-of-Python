import time


# Required concepts
# Functions can have inputs/functionality/output
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
def calculator(call_calc, n1, n2):
    return call_calc(n1, n2)


result = calculator(add, 6, 8)
print(result)


# Functions can be Nested in other functions
def outer_func():
    print("I'm outer")

    def nested_func():
        print("I'm inner")

    nested_func()


outer_func()


# Functions can be returned from other functions
def outer_func():
    print("I'm outer")

    def nested_func():
        print("I'm inner")

    return nested_func


inner_func = outer_func()
inner_func()
print('=========================')


# Simple Python Decorator Functions
def delay_decorator(function):
    def wrapper_function():
        # Do sth before function
        time.sleep(2)
        function()
        # Do sth after function
        # or Modify function
    return wrapper_function


# With the @ syntactic sugar
@delay_decorator
def say_hello():
    print('hello')


# With the @ syntactic sugar
@delay_decorator
def say_bye():
    print('bye')


# Without the @ syntactic sugar
def say_greeting():
    print('How are you?')


decorated_func = delay_decorator(say_greeting)
decorated_func()
say_hello()  # will wait 2 seconds
say_bye()  # will wait 2 seconds

