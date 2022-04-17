import PIL.Image
import PIL.ImageTk
import PIL.ImageDraw
import PIL.ImageFont
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Watermark")
        self.geometry("1000x900")
        self.configure(background='grey')

        self.button = ttk.Button(self, text="Open Image", command=self.open_file)
        self.button.pack()
        self.button.place(x=0, y=0)
        self.watermark_content="Henrynugent.com"
        self.display_picture = ttk.Button(self, text="Show Photos", command="")
        self.display_picture.pack()
        self.display_picture.place(x=80, y=0)
        self.waterMark_button = ttk.Button(self, text="Watermark", command=self.watermaker_all_picture)
        self.waterMark_button.pack()
        self.waterMark_button.place(x=160, y=0)        
    def open_file(self):
        file_path = askopenfilename(multiple=True)
        for file in file_path:
            name = file.split('/')[-1]
            PIL.Image.open(file).save(
                f"pythonProjectEuler/watermarkapp/images/{name}")
            
    def watermaker_all_picture(self):
        import os
        imageData= []
        for x in os.listdir(f"pythonProjectEuler/watermarkapp/images/"):
            if x.endswith(".png"):
                self.add_watermark(f"pythonProjectEuler/watermarkapp/images/{x}", "Henrynugent.com")
                os.remove(f"pythonProjectEuler/watermarkapp/images/{x}")
            
    def add_watermark(self, image, watermark_content):
        open_image = PIL.Image.open(image)
        image_width, image_height = open_image.size
        draw = PIL.ImageDraw.Draw(open_image)
        font_size = int(image_width / 10)
        font = PIL.ImageFont.truetype("arial.ttf", font_size)
        text_width, text_height = draw.textsize(watermark_content, font=font)
        x = int(image_width/2)
        y = int(image_height/2)
        draw.text((x, y), watermark_content, font=font, fill=(255, 255, 255, 255), stroke_fill="grey", anchor="ms")
        name = image.split('/')[-1]
        open_image.save(f"pythonProjectEuler/watermarkapp/watermarked_photo/{name}")
         
                  
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
            img = PIL.Image.open(
                f"pythonProjectEuler/watermarkapp/images/{item[0]}")
            self.button1 = img.resize((100, 100), PIL.Image.ANTIALIAS)
            self.button1 = PIL.ImageTk.PhotoImage(self.button1)
            self.button = ttk.Button(self, image=self.button1,
                                command=self.open_file)
            self.button.pack()
            self.button.place(x=item[1], y=item[2])
            
        
if __name__ == "__main__":
    app = App()    
    app.mainloop()

