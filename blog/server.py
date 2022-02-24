from urllib import response
from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/blog')
def blog():
    response = requests.get('https://www.npoint.io/docs/3894d56cbf246dc4c5e2')
    all_post = response.json()
    return render_template('blog.html', posts=all_post)


if __name__ == '__main__':
    app.run()
