from flask import Blueprint, render_template,request
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