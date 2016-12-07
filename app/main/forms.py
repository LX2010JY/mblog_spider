# coding:utf-8
# from flask_wtf import Form
from flask_wtf import FlaskForm as Form
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required,DataRequired,Length

class NameForm(Form):
    '''
        继承flask_wtf 的form类，定义一个表单类
    '''
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')
class PostForm(Form):
    body = TextAreaField("what's your felling today ?",validators=[DataRequired()])
    submit = SubmitField('发送')

class EditProfileForm(Form):
    name = StringField('真实姓名',validators=[Length(0,10)])
    location = StringField('地址',validators=[Length(0,64)])
    about_me = TextAreaField('关于我')
    submit = SubmitField('修改')