import turtle as t
from turtle import Turtle, Screen
import random

import colorgram
colors = colorgram.extract('image.jpg', 6)

print(colors)
def random_color():
    t.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

timmy = Turtle()
timmy.shape("turtle")
def square(num):
    side =0
    while side < 4:
        timmy.forward(num)
        timmy.right(90)
        side +=1
def straigh(num):
    timmy.left(45)
    count = 0
    while count < 20:
        timmy.forward(num)
        count+=1

def underline():
    timmy.left(45)
    count=0
    while count < 10:
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
        count +=1
def triagle(size):
    timmy.forward(size)
    count = 0
    while count < 3:
        timmy.right(360/3)
        timmy.forward(size)
        count+=1
def shape(side, num):
    count = 0 
    if side >= 3:
        while count < side:
            timmy.right(360/side)
            timmy.forward(num)
            count+=1
    
        

    
color = ["red", "black", "blue", "brown", "green", "pink", "orange", "yellow","violet", "cyan"]   

def drawoverlapshap():
    count = 3 
    while count < 13:
        timmy.pencolor(color[count%10])
        shape(count, 100) 
        count+=1
def drawrandomline():        
    directions =[0,90,180,270]
    timmy.pensize(15)
    timmy.speed("fastest")
    for _ in range(200):
        timmy.color(random_color())
        timmy.forward(30)
        timmy.setheading(random.choice(directions))
        
        
        
def draw_spiralgraph(sizeofgap):  
    timmy.speed("fastest")     
    for _ in range(int(360 / sizeofgap)):  
        timmy.color(random_color())        
        timmy.circle(100)
        timmy.setheading(timmy.heading() + sizeofgap)
    screen = Screen()
    screen.exitonclick()



