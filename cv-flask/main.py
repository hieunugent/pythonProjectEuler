from flask import Flask, redirect, render_template 
import datetime
app = Flask(__name__)
@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template('index.html', current_year=current_year)
# @app.route('/index.html')
# def index():
#     return redirect('/')
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
# @app.route('/projects.html')
# def projects():
#     return render_template('projects.html')
@app.route('/<string:subpath>')
def catch_all(subpath):
    return render_template(subpath)


if   __name__ == '__main__':
    app.run()
