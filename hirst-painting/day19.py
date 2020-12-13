from turtle import Turtle, Screen
def program():
    tim = Turtle()
    screen = Screen()
    def move_forwards():
        tim.forward(10)   
        
    def move_backwards():
        tim.backward(10)
        
    def turn_left():
        new_heading = tim.heading() +10
        tim.setheading(new_heading)
        
    def turn_right():
        new_heading = tim.heading() -10
        tim.setheading(new_heading)
    def clear():
        tim.clear()
        tim.penup()
        tim.home()
        tim.pendown()  
    screen.listen()
    screen.onkey(move_forwards, "w")
    screen.onkey(move_backwards, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear, "c")
    screen.exitonclick()
import random   
screen = Screen()
screen.setup(width=500, height=400)
is_race_on=False
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet", "cyan"]
y_pos=[-150, -100, -50, 0, 50 , 100, 150]
all_turtle = []
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y= y_pos[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on= False
            wincorlor = turtle.pencolor()
            if wincorlor == user_bet:
                print(f"you're won ! the {wincorlor} turtle  is winner")
            else:
               print(f"you're lose ! the {wincorlor} turtle  is winner")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()