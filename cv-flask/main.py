from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
@app.route('/projects.html')
def projects():
    return render_template('projects.html')

if   __name__ == '__main__':
    app.run()
