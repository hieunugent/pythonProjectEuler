from flask import Flask, render_template, request
import requests
import smtplib
import os
MY_EMAIL= os.environ.get('TEST_EMAIL')
PASSWORD=''
if os.environ.get('TEST_PASSWORD'):
    PASSWORD= os.environ.get('TEST_PASSWORD')
elif os.environ.get('TEST_PASS'):
    PASSWORD= os.environ.get('TEST_PASS')

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
        print(data['name'])
        print(data['email'])
        print(data['phone'])
        print(data['message'])
        send_email(data['name'], data['email'], data['phone'], data['message'])
        return render_template('contact.html', msg_sent=True) 
    return render_template('contact.html', msg_sent=False)
    
def send_email(name, email, phone, message):
    message_send= f"Subject:New Message \n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with  smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(MY_EMAIL, PASSWORD)
        server.sendmail(from_addr=MY_EMAIL, to_addrs="henrynugent009@gmail.com",
                        msg=message_send)
    
    
    
    
@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in posts:
        if post['id'] == index:
            requested_post = post
    return render_template('post.html', post=requested_post)


if __name__=="__main__":
    app.run()  
