from turtle import Turtle, Screen

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
        while count <=side:
            timmy.right(360/side)
            timmy.forward(num)
            count+=1
    
        

count = 3        
while count < 8:
    shape(count, 100)
    count+=1

screen = Screen()
screen.exitonclick()