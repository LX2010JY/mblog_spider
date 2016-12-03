# coding:utf-8
from . import db
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
