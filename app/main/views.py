from flask import Flask
from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required
from .forms import BlogForm, CommentForm ,EmailForm
from .. models import User
from ..import db

# @main.route('/')
# def index():
#     form = EmailForm()
#     '''
#     View the root page function
#     '''
#     title = "Pitches"
#     return render_template('index.html', title = title,pitches=pitches)

@main.route('/', methods = ['GET','POST'])
def index():
    formemail = EmailForm()
    if formemail.validate_on_submit():
        pitch = Pitch(category = formpitch.category.data, content = formpitch.pitch.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
     
    return render_template('pitch.html',formpitch = formpitch)   

# @main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
# @login_required
# def new_comment(pitch_id):  
#     '''
#     View the root page function
#     '''
#     pass



  