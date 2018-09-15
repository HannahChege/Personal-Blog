from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,BooleanField
from wtforms.validators import Required

class BlogForm(FlaskForm):  # create a class that inherits from FlaskForm class
   title = StringField('Title', validators=[Required()])
   blog = TextAreaField('Blog', validators=[Required()])
   photo_url = StringField('Photo URL',validators=[Required()])
   post = SubmitField('Posted blog')

class CommentForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    comment_data = TextAreaField('WRITE COMMENT')
    post = SubmitField('Posted blog')

class EmailForm(FlaskForm):
    name = StringField('Name', validators=[Required()])
    email = StringField('Email', validators=[Required()])
    comment_data = TextAreaField('WRITE COMMENT')
    subscribe = SubmitField('Subscribe')

