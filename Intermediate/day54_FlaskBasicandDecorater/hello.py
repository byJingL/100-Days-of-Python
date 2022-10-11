from flask import Flask
import random
# import os
# test = os.environ.get("FLASK_APP")
# print(test)

# only one required input
app = Flask(__name__)
print(app)
print(__name__)  # __main__
print(random.__name__)  # random


# If user go to homepage, trigger the function_speed.py
@app.route('/')  # homepage
def hello_world():
    return 'Hello, World!'


@app.route('/bye')  # homepage
def say_bye():
    return 'Bye'


if __name__ == "__main__":
    app.run()
