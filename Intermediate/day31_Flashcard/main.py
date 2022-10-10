from tkinter import *
import pandas
import random

GREEN = "#B1DDC6"
TITLE = "Ariel", 40, "italic"
WORD = "Ariel", 60, "bold"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/english_words.csv")
finally:
    to_learn = data.to_dict(orient="records")


def next_card():

    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=card_front_image)
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=current_card["English"], fil="black")

    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="Explain", fill="white")
    canvas.itemconfig(word_text, text=current_card["Explain"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()
    words = pandas.DataFrame(to_learn)
    words.to_csv("data/words_to_learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=GREEN)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=GREEN, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_back_image = PhotoImage(file="images/card_back.png")
# ❣️canvas Text
title_text = canvas.create_text(400, 150, text="", font=TITLE)
word_text = canvas.create_text(400, 263, text="", font=WORD)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
known_button = Button(image=right_image, highlightbackground=GREEN, command=is_known)
known_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=wrong_image, highlightbackground=GREEN, command=next_card)
unknown_button.grid(column=0, row=1)

next_card()

window.mainloop()

