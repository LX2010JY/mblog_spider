from datetime import datetime
from flask import render_template,session,redirect,url_for,flash

from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/',methods=['GET','POST'])
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
        return redirect(url_for('main.index'))
    return render_template('index.html',form=form,name=session.get('name'),current_time=datetime.utcnow())

# <> 中包含的是动态内容，默认是字符串，也可以通过<int:id>方式指定为int
@main.route('/user/<name>')
def user(name):
    # return '<h1>hello ,%s</h1>' % name,404
    return render_template('user.html',name=name),404

# 测试 socketio
@main.route('/chat/<name>')
def chat(name):
    return render_template('chat.html',name=name)

# 聊天室 socket
@main.route('/chatroom')
def chatroom():
    if session.get('name') is None:
        flash('请说明您是谁，否则不允许进入聊天室！')
        return redirect(url_for('main.index'))
    return render_template('chatroom.html',name=session.get('name'))


