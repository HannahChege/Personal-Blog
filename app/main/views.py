from flask import Flask
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from .forms import BlogForm,UpdateProfile
from .. models import User,Blog
from ..import db,photos

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
@main.route('/admin/<uname>')
def profile(uname):
    admin = Admin.query.filter_by(username = uname).first()

    if admin is None:
        abort(404)

    return render_template("profile/profile.html", admin = admin)

@main.route('/admin/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    admin = Admin.query.filter_by(username = uname).first()
    if admin is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        admin.bio = form.bio.data

        db.session.add(admin)
        db.session.commit()

        return redirect(url_for('.profile',uname=admin.username))

    return render_template('profile/update.html',form =form)
@main.route('/admin/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    admin = Admin.query.filter_by(username = uname).first()
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



  