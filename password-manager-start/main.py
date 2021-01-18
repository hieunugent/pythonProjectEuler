from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(THIS_FOLDER, 'logo.png')
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

canvas = Canvas(height=200,width=200)
logo_img = ImageTk.PhotoImage(Image.open(path))
lbl = ttk.Label(window, image = logo_img)
lbl.pack()



window.mainloop()