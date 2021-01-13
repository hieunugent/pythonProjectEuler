import turtle
import os
# import gif
import pandas
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# background = os.path.join(THIS_FOLDER, 'backgound.gif')


screen = turtle.Screen()
screen.title("U.S. State Game")
images = "backgound.gif"

screen.addshape(images)
turtle.shape(images)
# fiftystate = os.path.join(THIS_FOLDER, '50_states.csv')
fiftystate = "50_states.csv"
data = pandas.read_csv(fiftystate)
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states)< 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct" , prompt="What's another state's name?" ).title()


    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state==answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


screen.exitonclick()



