from tkinter import *
# todo: 1.Pake() Function: pack sth in the screen
# a simple way to lay out the components that you're building
# todo: 2.Place() Function: precise positioning 精准定位
# todo: 3.Grid() Function: grid(rows, columns)
# ☠️Can't mix up grid and pack in the same program,
# these two are incompatible with each other.


def button_click():
    user_input = entry.get()
    my_label.config(text=user_input)


# window: object; Tk(): class
window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label(): class, 3 Ways to modify it
my_label = Label(text="new text", font=("Arial", 24))
my_label["text"] = "new text"
my_label.config(text="new text")
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

# Button(): class; command = just name of function
my_button = Button(text="Calculate", command=button_click)
my_button.grid(row=1, column=1)

# Button(): class; command = just name of function
new_button = Button(text="Click")
new_button.grid(row=0, column=2)

# Entry(): class; "END" don't change
entry = Entry(width=10)
entry.insert(END, string="hint: ")
entry.grid(row=3, column=2)

window.mainloop()
