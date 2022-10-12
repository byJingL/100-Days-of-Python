import random

from flask import Flask
IMG_HOME = 'https://media3.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif?' \
           'cid=ecf05e47fhoclrbrcl16ktthhqzgjkf01w5fv78i8r8vajnl&rid=giphy.gif&ct=g'
IMG_LOW = 'https://media3.giphy.com/media/wfS4vDyVsASQygl4mN/giphy.gif?' \
          'cid=ecf05e47jtiac5w4s49ti7z85ie5dgv1629eqnzvzsjml3ru&rid=giphy.gif&ct=g'
IMG_HIGH = 'https://media3.giphy.com/media/l4KibK3JwaVo0CjDO/giphy.gif?' \
           'cid=ecf05e47p212a8lh49ze7wytchlcmpeuw1tx9h8phaygocjr&rid=giphy.gif&ct=g'
IMG_RIGHT = 'https://media2.giphy.com/media/yrrEhlrF4Ek2k/giphy.gif?' \
            'cid=ecf05e47y67znfuo94x54lbeqpqbuonw6jok7hbnn9k2lr1z&rid=giphy.gif&ct=g'
app = Flask(__name__)
ran_number = random.randint(0, 9)
print(ran_number)


@app.route("/")
def homepage():
    return f'<h1>Guess a number between 0 and 9</h1>' \
           f'<img src={IMG_HOME}>'


@app.route("/<int:number>")
def result(number):
    if int(number) < ran_number:
        return f'<h1 style="color:HotPink">Too low, try again!</h1>' \
               f'<img src={IMG_LOW}>'
    elif int(number) > ran_number:
        return f'<h1 style="color:Purple">Too high, try again!</h1>' \
               f'<img src={IMG_HIGH}>'
    else:
        return f'<h1 style="color:SeaGreen">You found me!</h1>' \
               f'<img src={IMG_RIGHT}>'


if __name__ == "__main__":
    app.run(debug=True)