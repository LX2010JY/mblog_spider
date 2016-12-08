#coding:utf-8
from datetime import datetime
from flask import render_template,session,redirect,url_for,flash,abort,current_app,request
from flask_login import current_user,login_required
from . import chat
from .. import db,socketio
from ..models import User,Mblog


# 聊天室 socket
@chat.route('/chatroom')
def chatroom():
    if not current_user.is_authenticated:
        flash('请说明您是谁，否则不允许进入聊天室！')
        return redirect(url_for('auth.login'))
    return render_template('chat/chatroom.html')
