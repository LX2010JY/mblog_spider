# coding:utf-8
from flask import Flask,render_template,redirect,abort,session,url_for,flash,current_app
# 专为flask开发的扩展都在flask.ext 命名空间可以找到，(下面两种方式等效)flask-script 是方便程序运行时设置模式
# from flask.ext.script import Manager
from flask_script import Manager,Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required,DataRequired
from flask_sqlalchemy import SQLAlchemy
import os
from flask_mail import Mail,Message
# __name__ 用于确定程序的根目录位置
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/flask"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '2810752073'
app.config['MAIL_PASSWORD'] = 'vufmglghcajgddca'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = '2810752073@qq.com'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')

db = SQLAlchemy(app)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
mail = Mail()
msg = Message('test Subject',sender='2810752073@qq.com',recipients=['jia6_yu6@163.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(msg)
class User(db.Model):
    '''
        在这里 role比user更广泛，role包含很多user，所以user是从表，role是主表
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(64),unique=True,index=True)
    last_login = db.Column(db.Integer)

    # role_id 是真是的数据包属性，其外键关联的是role表的id属性，这个可以比较好理解
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))

    def __repr__(self):
        return '<User %r>'%self.username

class Role(db.Model):
    '''
        实验外键临时表
    '''
    __tablename__ = 'role'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,index=True)

    user = db.relationship('User',backref='role')

# 每次启动shell的时候，自动加载 需要的对象
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell",Shell(make_context=make_shell_context))


class NameForm(Form):
    '''
        继承flask_wtf 的form类，定义一个表单类
    '''
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    '''
        视图函数，用于返回包含HTML的响应
    :return:
    '''
    # return '<h1>Hello World</h1>'
    form = NameForm()
    if form.validate_on_submit():
        # 数据存入session中
        if session.get('name') is not None and session.get('name') != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'),current_time=datetime.utcnow())

# <> 中包含的是动态内容，默认是字符串，也可以通过<int:id>方式指定为int
@app.route('/user/<name>')
def user(name):
    # return '<h1>hello ,%s</h1>' % name,404
    return render_template('user.html',name=name),404

@app.errorhandler(404)
def page_not_found(e):
    # 返回第二个参数可以是状态码，第三个参数是header组成的字典
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

# 使用jinjia2模板引擎
@app.route('/tem/<username>')
def tem(username):
    return render_template('tem.html',name=username)


if __name__ == '__main__':
    manager.run()
    # app.run(debug=True)
