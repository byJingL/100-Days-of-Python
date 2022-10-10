# FileNotFound, KeyError, IndexError, TypeError......

# Error is eventually
# Todo: 1. Catch Exceptions
# Todo: 2. Handle Exceptions :
#          1.try: Something that might cause an exception
#          2.Except: Do this if there was an exception
#          3.else: Do this if there were no exceptions
#          4.finally: Do this no matter what happens (not usually used)
#          5. raise: raise errors whatever you want
# Be careful: Catch Exception should be putted in function
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


fruits = ["Apple", "Pear", "Orange"]
make_pie(20)

try:
    file = open("file.text")
    my_dict = {
        "key": "value",
    }
    print(my_dict["apple"])
except FileNotFoundError:
    file = open("file.text", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does nor exist")
else:
    # just when try to have no one error, can be executed
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")


# Using "raise"
height = float(input("Height: "))
weight = int(input("Weight: "))
if height > 3:
    raise ValueError()
elif weight > 500:
    raise ValueError()
else:
    BMI = weight/height**2
    print(BMI)
