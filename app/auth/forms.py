from flask_wtf import FlaskForm as Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo
from ..models import User

class LoginForm(Form):
    email = StringField('邮箱',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('密码',validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登陆')

class RegistrationForm(Form):
    email = StringField('邮箱',validators=[DataRequired(),Length(1,64),Email()])
    username = StringField('用户名',validators=[DataRequired(),Length(1,64)])
    password = PasswordField('密码',validators=[DataRequired(),EqualTo('password2',message='密码不匹配')])
    password2 = PasswordField('确认密码',validators=[DataRequired()])
    submit = SubmitField('注册')
    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经被注册')
    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经被使用')
