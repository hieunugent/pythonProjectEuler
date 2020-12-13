import turtle as t
from turtle import Turtle, Screen
import random


def random_color():
    t.colormode(255)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)


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



# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     newcolor = (r,g,b)
#     rgb_colors.append((newcolor))
# print

import turtle as turtle_module

def draw_dot(num):
    turtle_module.colormode(255)
    timmy = turtle_module.Turtle()
    timmy.speed("fastest")
    color_list = [(248, 150, 92), (210, 65, 118), (45, 82, 182), (253, 246, 249), (240, 130, 154), (231, 223, 73), (35, 215, 192), (238, 245, 251), (149, 54, 40), (37, 47, 158), (112, 214, 251), (86, 24, 32), (59, 210, 188), (253, 218, 0), (248, 140, 148), (175, 59, 92), (123, 177, 208), (138, 30, 38), (223, 62, 56), (240, 156, 151), (138, 218, 207), (106, 113, 169), (137, 39, 29), (63, 24, 21), (177, 185, 222), (15, 21, 93), (74, 128, 74), (39, 208, 213)]
    timmy.penup()
    timmy.hideturtle()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)

    number_of_dots = num*num
    for dot_count in range(1, number_of_dots +1):
        timmy.dot(20, random.choice(color_list))

        timmy.forward(50)

        if dot_count % 10 == 0:

            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)


draw_dot(10)
screen = turtle_module.Screen()
screen.exitonclick()