from flask import Flask
from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user
from .forms import PitchForm
# from .. models import User,Pitch,Comment
from ..import db

@main.route('/')
def index():
    
    title = "Personal blog"
    return render_template('index.html', title = title)

@main.route('/new/blog', methods = ['GET','POST'])
@login_required
def new_blog():
    formblog = BlogForm()
    if formblog.validate_on_submit():
        blog = Blog(category = formblog.category.data, content = formblog.blog.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
     
    return render_template('blog.html',formblog = formblog)   

# @main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
# @login_required
# def new_comment(pitch_id):  
#     '''
#     View the root page function
#     '''
#     pass



  