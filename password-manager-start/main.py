from tkinter import *

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(THIS_FOLDER, 'logo.png')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100,100,image =logo_img)
canvas.pack()


window.mainloop()