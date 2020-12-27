import turtle
import os
import gif
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
background = os.path.join(THIS_FOLDER, 'backgound.gif')
screen = turtle.Screen()
screen.title("U.S. State Game")
images = background

screen.addshape(images)
turtle.shape(images)
answer_state = screen.textinput(title="Guess the State",prompt="What's another state's name?" )
screen.exitonclick()