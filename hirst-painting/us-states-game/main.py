import turtle
import os
import csv
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
image = os.path.join(THIS_FOLDER, 'backgound.gif')
from PIL import Image
screen = turtle.Screen()
screen.title("U.S. State Game")
images = Image.open(image)

screen.addshape(images)
turtle.shape(images)
screen.exitonclick()