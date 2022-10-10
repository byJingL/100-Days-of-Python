# Todo: 1. Unlimited Position Arguments: *args
def add(*args):
    print(args[4])
    # args is a tuple
    sum_ = 0
    for item in args:
        sum_ += item
    return sum_


print(add(1, 2, 3, 4, 5, 6, 12, 14, 17))


# Todo: 2. Unlimited keyword Arguments: **kw
def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)


# Todo: 3. Use above to create a class
# use kw.get()
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self. color = kw.get("color")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.color)
