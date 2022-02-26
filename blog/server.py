
from flask import Flask, render_template

from post import Post
import requests

posts = requests.get('https://api.npoint.io/3894d56cbf246dc4c5e2').json()
post_objects = []
for post in posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def get_all_posts():   
    return render_template('blog.html', posts=post_objects)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in post_objects:
        if post.id == index:
            requested_post = post
    return render_template('posts.html', post=requested_post)


if __name__ == '__main__':
    app.run()
