from flask import Flask
app = Flask(__name__)


def bold_decorator(function):
    def wrapper_function():
        return f'<strong>{function()}</strong>'
    return wrapper_function


def em_decorator(function):
    def wrapper_function():
        return f'<em>{function()}</en>'
    return wrapper_function


def under_decorator(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function


@app.route('/')  # homepage
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="http://www.reddit.com/r/gifs/comments/3l0i36/can_i_sit_in_your_lap_now/">'\
           '<p><h2 style="text-align: left">Cute dog</h2></p>'


@app.route('/bye')  # homepage
@bold_decorator
@em_decorator
@under_decorator
def hello_world():
    return 'Bye!'


if __name__ == "__main__":
    # Run the app in debug mode: Auto-reload
    app.run(debug=True)
