from tkinter import *
# Not class, need a new import
from tkinter import messagebox
from password import Generator
import pyperclip
SAND = "#FFFFDE"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Generator(): Class
def create_password():
    generator = Generator()
    generator.create()
    pyperclip.copy(generator.password)
    pass_entry.insert(0, string=generator.password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    web = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(web) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered:\nEmail: {email}\n"
                                                  f"Password: {password}\nIs it OK to save? ")
        if is_ok:
            with open("data.text", "a") as data:
                data.write(f"{web} | {email} | {password}\n")

            web_entry.delete(0, END)
            pass_entry.delete(0, END)
            web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=30)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
# x, y 为相对定位 on the canvas
canvas.create_image(125, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
user_label = Label(text="Email/Username")
user_label.grid(column=0, row=2)
pass_label = Label(text="Password")
pass_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=38)
web_entry.grid(column=1, row=1, columnspan=2)
# curser already show up when open
web_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
# Starting value of email entry
email_entry.insert(END, string="emma@outlook.com")
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=create_password)
generate_button.grid(column=2, row=3)
add_button = Button(width=36, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
