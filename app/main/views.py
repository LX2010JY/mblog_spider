# coding:utf-8
from datetime import datetime
from flask import render_template,session,redirect,url_for,flash,abort,current_app,request
from flask_login import current_user,login_required
from . import main
from .forms import NameForm,PostForm,EditProfileForm
from .. import db
from ..models import User,Mblog


@main.route('/',methods=['GET','POST'])
def index():
    '''
        视图函数，用于返回包含HTML的响应
    :return:
    '''
    form = PostForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            flash('必须先登录才能发送')
            return redirect(url_for('main.index'))
        # 数据存入session中
        # if session.get('name') is not None and session.get('name') != form.name.data:
        #     flash('Looks like you have changed your name!')
        # session['name'] = form.name.data
        mblog = Mblog(body=form.body.data,author=current_user._get_current_object())
        db.session.add(mblog)
        db.session.commit()
        return redirect(url_for('main.index'))
    page = request.args.get('page',1,type=int)
    pagination = Mblog.query.order_by(Mblog.timestamp.desc()).paginate(page,per_page=current_app.config['FLASK_PER_PAGE'],error_out=True)
    mblogs = pagination.items
    # mblogs = Mblog.query.order_by(Mblog.timestamp.desc()).all()
    return render_template('index.html',form=form,mblogs=mblogs,pagination=pagination,current_time=datetime.utcnow())

# <> 中包含的是动态内容，默认是字符串，也可以通过<int:id>方式指定为int
@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html',user=user)

@main.route('/user/edit',methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('更新个人信息成功')
        return redirect(url_for('main.user',username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html',form=form)



# 测试 socketio
@main.route('/chat/<name>')
def chat(name):
    return render_template('chat.html',name=name)

# 聊天室 socket
@main.route('/chatroom')
def chatroom():
    if not current_user.is_authenticated:
        flash('请说明您是谁，否则不允许进入聊天室！')
        return redirect(url_for('auth.login'))
    return render_template('chatroom.html')


