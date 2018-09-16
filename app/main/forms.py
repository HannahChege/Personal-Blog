from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    category=SelectField('category',
       choices=[('Beauty', 'Beauty'), ('Fashion', 'Fashion'), ('Lifestyle', 'Lifestyle')], validators = [Required()])
    blog = TextAreaField('Blog')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio= TextAreaField('Tell us about you.', validators=[Required()])
    submit= SubmitField('Submit')


# class ContentForm(FlaskForm):
#    content = TextAreaField('YOUR PITCH')
#    submit = SubmitField('SUBMIT')

# class CommentForm(FlaskForm):
#    comment_id = TextAreaField('WRITE COMMENT')
#    submit = SubmitField('SUBMIT')




