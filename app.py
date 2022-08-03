
from flask import Flask, request, render_template, redirect
from peewee import *
from models import Post


app = Flask(__name__)

@app.route('/')
def sdf():
    all_posts = Post.select()
    return render_template("index.html", posts=all_posts)


@app.route('/create', methods = ('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form ['title']
        description = request.form ['description']

        Post.create(
            title = title,
            description = description
        )
        return redirect('/')
    return render_template ('create.html')





@app.route ('/bye')
def nurai():
    return 'bye, Nurai'


if __name__ == "__main__":
    app.run(debug=True)