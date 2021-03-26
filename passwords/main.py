from tkinter import *
from tkinter import messagebox,ttk
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
from PIL import Image, ImageTk

# window = Tk()
# window.title("Password Manager")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(height=200, width=200)
#
# logo_img = ImageTk.PhotoImage("logo.png")
# canvas.create_image(100, 100, image=logo_img)
# canvas.grid(row=0, column=1)
#
# #Labels
# website_label = Label(text="Website:")
# website_label.grid(row=1, column=0)
# email_label = Label(text="Email/Username:")
# email_label.grid(row=2, column=0)
# password_label = Label(text="Password:")
# password_label.grid(row=3, column=0)
#
# #Entries
# website_entry = Entry(width=35)
# website_entry.grid(row=1, column=1, columnspan=2)
# website_entry.focus()
# email_entry = Entry(width=35)
# email_entry.grid(row=2, column=1, columnspan=2)
# email_entry.insert(0, "angela@gmail.com")
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)
#
# # Buttons
# generate_password_button = Button(text="Generate Password", command=generate_password)
# generate_password_button.grid(row=3, column=2)
# add_button = Button(text="Add", width=36, command=save)
# add_button.grid(row=4, column=1, columnspan=2)
#
# window.mainloop()

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(window, height=100, width=100, bg="white")
canvas.grid(row=0, column=1)
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
logo = os.path.join(THIS_FOLDER, 'logo.png')
# logo_img = PhotoImage(file=logo)
logo_img = ImageTk.PhotoImage(Image.open(logo))
canvas.create_image(100, 100, image=logo_img)

lable1 = Label(text="Website:")
lable1.grid(row=1, column=0)
input1 = Entry(width=35)
input1.grid(column=1, row=1, columnspan=2)
lable2 = Label(text="Email/Username:")
lable2.grid(row=2, column=0)
input2 = Entry(width=35)
input2.grid(column=1, row=2, columnspan=2)
input2.insert(0, "hieu@gmail.com")
lable3 = Label(text="Password:")
lable3.grid(row=3, column=0)
input3 = Entry(width=21)
input3.grid(column=1, row=3)
btngeneratePw = ttk.Button(text="Generate Password", command=generate_password)
btngeneratePw.grid(column=2, row=3)
btnAdd = ttk.Button(text="Add", width=36, command=save)
btnAdd.grid(column=1, row=4, columnspan=2)

window.mainloop()