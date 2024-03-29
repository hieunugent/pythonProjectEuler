import email
from unicodedata import name
from urllib import response
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in= current_user.is_authenticated)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method=="POST":
        if User.query.filter_by(email=request.form.get('email')).first():
            flash("Email already exists")
            return redirect(url_for('login'))
        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            email = request.form.get('email'),
            password = hash_and_salted_password,
            name = request.form.get('name')
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template("secrets.html", name=new_user.name)
    return render_template("register.html", logged_in= current_user.is_authenticated)


@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method=="POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("User does not exist, please register or login again with different credentials")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash("Incorrect password, please try again")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))    
        
    return render_template("login.html", logged_in= current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in= True) , 200


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    # depend on where the lib is install the directory will be set differently, for now path is replace for filename
    return send_from_directory(directory="../flask-auth/static/files/", path="cheat_sheet.pdf")
     


if __name__ == "__main__":
    app.run(debug=True)
