import turtle
import os
import pandas
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
background = os.path.join(THIS_FOLDER, 'backgound.png')
screen = turtle.Screen()
screen.title("U.S. State Game")
images = background

screen.addshape(images)
turtle.shape(images)
fiftystate = os.path.join(THIS_FOLDER, '50_states.csv')
data = pandas.read_csv(fiftystate)
all_states = data.state.to_list()

answer_state = screen.textinput(title="Guess the State",prompt="What's another state's name?" )


if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state==answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)
    
print(answer_state)


screen.exitonclick()



