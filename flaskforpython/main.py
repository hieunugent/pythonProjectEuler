
from flask import Flask
import time
app = Flask(__name__)
def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper
def make_underline(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper
def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/sleep')
@make_bold 
@make_underline
@make_emphasis
def sleephour():
    time.sleep(1)
    return '<h1 style="text-align:center"> sleep hour at 10 pm </h1>'


if __name__ == '__main__':
    app.run()
