from tkinter import *


def calculate():
    user_input = float(mile_entry.get())
    result = round(user_input*1.609, 2)
    output_label.config(text=f"{result}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile_entry = Entry(width=8)
mile_entry.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)

mile_label = Label(text="Miles")
mile_label.grid(column=3, row=1)

Km_label = Label(text="Km")
Km_label.grid(column=3, row=2)

equal_label = Label(text="is equal to")
equal_label.grid(column=1, row=2)

output_label = Label(text="0")
output_label.grid(column=2, row=2)

window.mainloop()
