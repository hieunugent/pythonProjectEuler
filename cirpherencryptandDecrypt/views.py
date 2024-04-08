from flask import Blueprint, render_template,request, url_for
from markupsafe import escape
views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")
@views.route("/login", methods=['GET','POST'])
def login():
    if request.method =='POST':
        return  "DO LOGING STUFF"
    else:
        return "SHOW LOGGING Moving"
@views.route('/user/<username>')
def show_user_profile(username):
    return  f'User {escape(username)}'


    