from tkinter import *
from tkinter import ttk, messagebox
from  random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("Welcome to the PyPassword Generator!")



    password_letters=[choice(letters) for _ in  range(randint(8,10))]
    password_symbols=[choice(symbols) for _ in  range(randint(2,4))]
    password_numbers=[choice(numbers) for _ in  range(randint(2,4))]
    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)
    password ="".join(password_list)
    password_generated.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_generated.get()
    new_data = {website:{
        "email":email,
        "password":password
    }}
    if len(website)==0  or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please dont let any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("./password/data.json", "a") as data_file:
                json.dump(new_data, data_file)
                
                
                # data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_generated.delete(0, END)
                
# ---------------------------- UI SETUP ------------------------------- #
from PIL import ImageTk, Image
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)
canvas = Canvas(window, height=200,width=200 , bg="white")
canvas.grid(row= 0, column=1)
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
logo = os.path.join(THIS_FOLDER, 'logo.png')
# logo_img = PhotoImage(file=logo)
logo_img = ImageTk.PhotoImage(Image.open(logo))
canvas.create_image(100, 100, image=logo_img)


lable1 = Label(text="Website:")
lable1.grid(row=1,column=0)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
lable2 = Label(text="Email/Username:")
lable2.grid(row=2, column=0)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "hieu@gmail.com")
lable3 = Label(text="Password:")
lable3.grid(row=3, column=0)
password_generated = Entry(width=35)
password_generated.grid(column=1, row=3, columnspan=2)
btngeneratePw= ttk.Button(text="Generate Password", command=generate_password)
btngeneratePw.grid(column= 3, row= 3)
btnAdd = ttk.Button(text="Add", width=36, command= save)
btnAdd.grid(column=1, row =4, columnspan=2)



window.mainloop()