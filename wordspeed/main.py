from distutils.fancy_getopt import wrap_text
import tkinter as tk
from tkinter import Canvas, ttk

from sqlalchemy import true
from text import array_text
import random
class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Word Speed")
        self.master.geometry("800x800")
        self.master.maxsize(800, 800) 
        self.typing_content()
        self.typing_speed()
        self.pack()
    def typing_content(self):
        canvas = Canvas(self.master, width=800, height=350, bg="lightgrey")  
        my_text = array_text[random.randint(0,1)]
        count = 0
        for i in range(len(my_text)):
            if count >= 103:
                if my_text[i] ==" ":
                   my_text = my_text[:i] + "\n" + my_text[i:]
                   count = 0
                else:
                   continue
            count += 1 
        canvas.create_text(400,180, text=my_text,  font=("Helvetica", "12"))
        canvas.pack()
    def typing_speed(self):
        canvas = Canvas(self.master, width=800, height=350, bg="grey")
        textbox = tk.Entry(canvas, textvariable=tk.StringVar(), width=100)
        textbox.grid(row=0, sticky="N"+"S")
        canvas.pack()
        textbox.pack()  


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()


