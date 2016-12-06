from flask_wtf import FlaskForm as Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo
from ..models import User

class LoginForm(Form):
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(Form):
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    username = StringField('Username',validators=[DataRequired(),Length(1,64)])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password2',message='password not match')])
    password2 = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

