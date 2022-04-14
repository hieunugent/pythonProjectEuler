
from sys import displayhook
import PIL.Image
import PIL
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import time
from requests import request

class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.title("Watermark")
        self.geometry("1000x900")
        self.configure(background='grey')
        # all the labels
      
        # all the buttons
        self.button = ttk.Button(self, text="Open Image", command=self.open_file)
        self.button.pack()
        self.button.place(x=0, y=0)
        self.display_picture = ttk.Button(self, text="Show Photos", command=self.create_widget)
        self.display_picture.pack()
        self.display_picture.place(x=80, y=0)
        self.waterMark_button = ttk.Button(
            self, text="Watermark", command=lambda:self.create_widget(0,100))
        self.waterMark_button.pack()
        self.waterMark_button.place(x=160, y=0)    
    def open_file(self):
        file_path = askopenfilename(multiple=True)
        for file in file_path:
            name = file.split('/')[-1]
            PIL.Image.open(file).save(
                f"pythonProjectEuler/watermarkapp/images/{name}")
            
    def create_widget(self):
        import os
        cdx = 0
        cdy = 100
        for x in os.listdir(f"pythonProjectEuler/watermarkapp/images"):
            if x.endswith(".jpg"):
               
               self.display_photo(cdx, cdy, x)
               cdy += 100
                # image = PIL.Image.open(f"pythonProjectEuler/watermarkapp/images/{x}")
                # image.show()
                # image.close()
                # time.sleep(1)
                # os.remove(f"pythonProjectEuler/watermarkapp/images/{x}")
                
                  
    def display_photo(self, x, y,imgName):   
        self.canvas = Canvas(self, width=100, height=100, bg="white")
        self.img = PhotoImage(file=f"pythonProjectEuler/watermarkapp/images/{imgName}")
        self.canvas.create_image(0, 0, image=self.img)
        self.canvas.pack()
        self.canvas.place(x=x, y=y)

    
if __name__ == "__main__":
    app = App()    
    app.mainloop()

# def upload_file():
#     pgbar = Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate')
#     pgbar.grid(row=3, columnspan=3, pady=20)
#     for i in range(100):
#         pgbar['value'] = i
#         window.update_idletasks()
#         time.sleep(0.01)
#     pgbar.destroy()
#     return True
# def display_image():
#     pass

# UI/UX design for the watermark app
## ---------------------------- WATERMARK ------------------------------- #
# Introduce the user to the watermark app
# window.config(padx=0, pady=0)
# canvas = Canvas(width=800, height=700, bg="grey")
# titleText = canvas.create_text(250, 450, text="", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, columnspan=12)
# canvas.itemconfig(titleText, text="Welcome to the Watermark App!")
# backBtn = Button(text="<Back", command=lambda: window.destroy())
# backBtn.grid(row=1, column=0)
# nextStepBtn = Button(text="Next >", command=lambda: window.destroy())
# nextStepBtn.grid(row=1, column=11)
# btnSelect = Button( text="Add Photo", command=lambda: open_file())
# btnSelect.grid(row=1,column=5, padx=10, pady=10)
# btnUpload = Button(text="Upload",command=lambda: upload_file())
# btnUpload.grid(row=1,column=6, padx=10, pady=10)
# waterMarkBtn = Button(text="Watermark Images",
#                       command=lambda: display_photo(window))
# waterMarkBtn.grid(row=1,column=7, padx=10, pady=10)



# app run loop
# window.mainloop()
