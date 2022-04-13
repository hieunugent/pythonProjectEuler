
import PIL.Image
import PIL
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
from requests import request
window = Tk()
import os
# helper functions in the watermarkapp folder


def open_file(): 
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*.png *.jpg *.jpeg')])
    PIL.Image.open(file_path.name).save()   
def upload_file():
    pgbar = Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
    pgbar.grid(row=3, columnspan=3, pady=20)
    for i in range(100):
        pgbar['value'] = i
        window.update_idletasks()
        time.sleep(0.01)
    pgbar.destroy()
    return True
def display_image():
    pass

# UI/UX design for the watermark app
## ---------------------------- WATERMARK ------------------------------- #
# Introduce the user to the watermark app
window.config(padx=0, pady=0)
canvas = Canvas(width=800, height=700, bg="grey")
titleText = canvas.create_text(250, 450, text="", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, columnspan=12)
canvas.itemconfig(titleText, text="Welcome to the Watermark App!")
backBtn = Button(text="<Back", command=lambda: window.destroy())
backBtn.grid(row=1, column=0)
nextStepBtn = Button(text="Next >", command=lambda: window.destroy())
nextStepBtn.grid(row=1, column=11)
btnSelect = Button( text="Add Photo", command=lambda: open_file())
btnSelect.grid(row=1,column=5, padx=10, pady=10)
btnUpload = Button(text="Upload",command=lambda: upload_file())
btnUpload.grid(row=1,column=6, padx=10, pady=10)
waterMarkBtn = Button(text="Watermark Images",command=lambda: window.destroy())




# app run loop
window.mainloop()
