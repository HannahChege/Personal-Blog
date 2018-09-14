from flask import Flask
from flask import render_template
from . import main
from flask_login import login_required



@main.route('/')
def index():
    '''
    View the root page function
    '''
    title = "Blog"
    return render_template('index.html', title = title)

