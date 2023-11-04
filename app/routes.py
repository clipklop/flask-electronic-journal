from flask import render_template

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mischa'}
    posts = [
        {
            'author': {'username': 'Vasya'},
            'body': 'omg wtf'
        },
        {
            'author': {'username': 'Petya'},
            'body': 'The weather was so cool back in summer'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

