from textwrap import fill
from tkinter import *
from PIL import ImageTk, Image
import pandas
import random

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
card_front = os.path.join(THIS_FOLDER, 'images/card_front.png')
card_back = os.path.join(THIS_FOLDER, 'images/card_back.png')
BACKGROUND_COLOR = "#B1DDC6"

# data = pandas.read_csv(os.path.join(THIS_FOLDER, 'data/french_words.csv'))  
current_card = {}
to_learn ={}




try:
    data = pandas.read_csv("flash-card-project/data/words_to_learn.csv")  
except FileNotFoundError:
    original_data = pandas.read_csv("flash-card-project/data/french_words.csv")
    to_learn = original_data.to_dict('records') 
else:
    to_learn = data.to_dict(orient='records')
       

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)   
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_image)
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("flash-card-project/data/words_to_learn.csv", index=False)
    next_card()
    
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526)
card_front_image = ImageTk.PhotoImage(Image.open(card_front))
card_back_image = ImageTk.PhotoImage(Image.open(card_back))
card_background = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400,150,text="", font=("arial",20,"italic"))
card_word = canvas.create_text(400,250,text="", font=("arial",40,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = ImageTk.PhotoImage(Image.open(os.path.join(THIS_FOLDER, 'images/wrong.png')))
unknown_button = Button(image=cross_image, command=next_card)
unknown_button.grid(row=1, column=0)
unknown_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)

check_image = ImageTk.PhotoImage(Image.open(os.path.join(THIS_FOLDER, 'images/right.png')))
known_button = Button(image=check_image, command=is_known)
known_button.grid(row=1, column=1)
known_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)

next_card()
window.mainloop()
