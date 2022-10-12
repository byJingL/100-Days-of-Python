# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(f"you called {function.__name__}"
              f"({args[0]}, {args[1]}, {args[2]})")
        print(f"It returned: {function(args[0], args[1], args[2])}")
    return wrapper


# Use the decorator 👇
@ logging_decorator
def calculate_function(a, b, c):
    return a+b+c


calculate_function(1, 2, 3)
