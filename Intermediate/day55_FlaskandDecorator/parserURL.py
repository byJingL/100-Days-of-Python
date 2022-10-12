from flask import Flask
import random

# only one required input
app = Flask(__name__)
# print(app)
# print(__name__)  # __main__
# print(random.__name__)  # random


# If user go to homepage, trigger the function_speed.py
@app.route('/')  # homepage
def hello_world():
    return 'Hello, World!'


@app.route('/bye')  # bye page
def say_bye():
    return 'Bye'


@app.route('/<name>')
def greet1(name):
    return f'Hi,there! {name}! How are you?'


# Anything after '/' will be assigned to 'name'
@app.route('/<path:name>')
def greet2(name):
    return f'Hi,there! {name}! How are you?'


@app.route('/<name>/<int:age>')
def greet3(name, age):
    return f'Hi, {name}! You are {age} years old!'


if __name__ == "__main__":
    # Run the app in debug mode: Auto-reload
    app.run(debug=True)

