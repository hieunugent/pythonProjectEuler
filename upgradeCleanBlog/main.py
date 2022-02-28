
from email import message
from flask import Flask, render_template, request
import requests

posts = requests.get('https://api.npoint.io/3894d56cbf246dc4c5e2').json()
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', all_posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method =="POST":
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        return "<h1>Thanks for contacting me. I will get back to you soon.</h1>"  
    return render_template('contact.html')
    
    
@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in posts:
        if post['id'] == index:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__=="__main__":
    app.run()  
