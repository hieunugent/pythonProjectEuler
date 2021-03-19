from tkinter import *
from tkinter import ttk, messagebox
from  random import choice, randint, shuffle
import pyperclip
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
    input3.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input1.get()
    email = input2.get()
    password = input3.get()
    if len(website)==0  or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please dont let any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("./password/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
                input1.delete(0, END)
                # input2.delete(0, END)
                input3.delete(0, END)
                
# ---------------------------- UI SETUP ------------------------------- #
from PIL import ImageTk, Image
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(window, height=100,width=100 , bg="white")
canvas.grid(row= 0, column=1)
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
logo = os.path.join(THIS_FOLDER, 'logo.png')
# logo_img = PhotoImage(file=logo)
logo_img = ImageTk.PhotoImage(Image.open(logo))
canvas.create_image(100, 100, image=logo_img)


lable1 = Label(text="Website:")
lable1.grid(row=1,column=0)
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
btngeneratePw= ttk.Button(text="Generate Password", command=generate_password)
btngeneratePw.grid(column= 2, row= 3)
btnAdd = ttk.Button(text="Add", width=36, command= save)
btnAdd.grid(column=1, row =4, columnspan=2)



window.mainloop()