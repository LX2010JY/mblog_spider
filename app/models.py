# coding:utf-8
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
# 多个继承，要使用flask_login user模型需要几个默认的方法，UserMixin 已实现，只需继承即可
class User(UserMixin,db.Model):
    '''
        在这里 role比user更广泛，role包含很多user，所以user是从表，role是主表
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    email = db.Column(db.String(64),unique=True,index=True)
    last_login = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    # role_id 是真是的数据包属性，其外键关联的是role表的id属性，这个可以比较好理解
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))

    def __repr__(self):
        return '<User %r>'%self.username
    #装饰器 将一个方法伪装成一个属性，其附带一个setter的装饰器，伪装的对属性赋值
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    '''
        实验外键临时表
    '''
    __tablename__ = 'role'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,index=True)

    user = db.relationship('User',backref='role')
