from flask import Flask
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from .forms import BlogForm,UpdateProfile
from .. models import User,Blog,Comment
from ..import db,photos

@main.route('/')
def index():
    blogs = Blog.query.all()
    title = "blog"
    return render_template('index.html',blogs=blogs, title = title)

@main.route('/new/blog', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(category = form.category.data, content = form.blog.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
     
    return render_template('blog.html',form = form ,blog=blog) 

@main.route('/new/Beauty', methods = ['GET','POST'])
@login_required
def new_Beauty():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(category = form.category.data, content = form.content.data)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('beauty.html',form =form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user =User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(admin)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/admin/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        admin.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    
# @main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
# @login_required
# def new_comment(pitch_id):  
#     '''
#     View the root page function
#     '''
#     pass



  