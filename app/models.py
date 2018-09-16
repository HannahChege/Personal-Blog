from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


# #...
# @login_manager.admin_loader
# def load_admin(id):
#         return Admin.query.get(int(id))
       

class Admin(UserMixin,db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'
class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer,primary_key = True)
    admin_id = db.Column(db.Integer,db.ForeignKey('admin.id'))
    category= db.Column(db.String(255),index = True)
    content= db.Column(db.String(255)) 
    comments = db.relationship('Comment', backref = 'blog', lazy = 'dynamic')

    def __repr__(self):
        return f'blog {self.content}'          

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer,db.ForeignKey ('blog.id'))
    admin_id = db.Column(db.Integer,db.ForeignKey('admin.id'))
    content= db.Column(db.String(255)) 

    def __repr__(self):
        return f'Comment :content {self.content}' 

        