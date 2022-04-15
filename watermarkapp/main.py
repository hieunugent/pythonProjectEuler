import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename



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
        self.waterMark_button = ttk.Button(self, text="Watermark", command=lambda:self.create_widget(0,100))
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
        imageData= []
        buttonWidgets=[]      
        for x in os.listdir(f"pythonProjectEuler/watermarkapp/images"):
            if x.endswith(".png"):
               imageData.append([x,cdx,cdy])
               cdx +=105 
        for item in imageData:
            self.Button_image(item, "Button"+str(item[0]).split('.')[0])
            
            
                  
    def display_photo(self,data):
            self.canvas = Canvas(self, width=99, height=99, bg="white")
            self.img = PIL.Image.open(
                f"pythonProjectEuler/watermarkapp/images/{data[0]}")
            self.img = self.img.resize((100,100), PIL.Image.ANTIALIAS)
            self.img = PIL.ImageTk.PhotoImage(self.img)
            self.canvas.create_image(0,0,anchor=NW, image=self.img)
            self.canvas.pack()
            self.canvas.place(x=10, y=40)
    def Button_image(self, item, button1):
            self.button1 = PIL.Image.open(
                f"pythonProjectEuler/watermarkapp/images/{item[0]}")
            self.button1 = self.button1.resize((100, 100), PIL.Image.ANTIALIAS)
            self.button1 = PIL.ImageTk.PhotoImage(self.button1)
            button = ttk.Button(self, image=self.button1,
                                command=self.open_file)
            button.pack()
            button.place(x=item[1], y=item[2])
        
        
if __name__ == "__main__":
    app = App()    
    app.mainloop()

