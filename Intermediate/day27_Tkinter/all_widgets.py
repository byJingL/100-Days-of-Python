from tkinter import *
# Pake Function: pack sth in the screen
# a simple way to lay out the components that you're building

# Todo: 1.Creating a new window and configurations
# window: object; Tk(): class
window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

# Todo: 2.Label(): class, 3 Ways to modify it
my_label = Label(text="new text", font=("Arial", 24))
my_label["text"] = "new text"
my_label.config(text="new text")
my_label.pack()

# Todo: 3.Entry(): class
# "END" don't change
entry = Entry(width=30)

entry.insert(END, string="Email: ")
entry.pack()


# Todo: 4.Button(): class
def button_click():
    user_input = entry.get()
    my_label.config(text=user_input)


# command = just name of function
my_button = Button(text="Calculate", command=button_click)
my_button.pack()

# Todo: 5.Text(): class
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Todo: 6.Spinbox()
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Todo: 7.Scale()
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Todo: 8.Checkbutton()
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Todo: 9.Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Todo: 10.Listbox()
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()

