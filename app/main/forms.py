from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    category=SelectField('category',
       choices=[('inspiration', 'inspiration'), ('pickuplines', 'pickuplines'), ('technoloy', 'technoloy'),
        ('411', '411')], validators = [Required()])
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




