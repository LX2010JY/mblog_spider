# coding:utf-8
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
# 多个继承，要使用flask_login user模型需要几个默认的方法，UserMixin 已实现，只需继承即可
class User(UserMixin,db.Model):
    '''
        在这里 role比user更广泛，role包含很多user，所以user是从表，role是主表
    '''
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    email = db.Column(db.String(64),unique=True,index=True)
    headsculpture = db.Column(db.String(128),default='flasky.jpg')
    last_login = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    # datetime.utcnow 本身是个函数，但是这里不加括号
    member_since = db.Column(db.DateTime(),default = datetime.utcnow)
    last_seen = db.Column(db.DateTime(),default=datetime.utcnow)
    # role_id 是真是的数据包属性，其外键关联的是role表的id属性，这个可以比较好理解
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))

    # 这项不是在user中添加，而是在 mblog 模型中添加 一个 backref 指定的属性，建立反向关系
    # mblog是表名，Mblog是类名
    mblog = db.relationship('Mblog',backref='author',lazy='dynamic')

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

    def ping(self):
        # 每次登陆刷新上次登陆时间
        self.last_seen = datetime.utcnow()
        db.session.add(self)
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
    default = db.Column(db.Boolean,default=False,index=True)
    permissions = db.Column(db.Integer)
    user = db.relationship('User',backref='role')

    @staticmethod
    def insert_roles():
        roles = {
            # 这里不明白 | 什么意思，怎么就相加了
            'User':(Permission.FOLLOW|Permission.COMMENT|Permission.WRITE_ARTICLES,True),
            'Moderator':(Permission.FOLLOW|Permission.COMMENT|Permission.WRITE_ARTICLES|Permission.MODERATE_COMMENTS,False),
            'Administrator':(0xff,False)
        }
        for r in roles:
            # python 字典 循环遍历，这样只能得到key值，要得到value，需要 dict[key]
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>'%self.name

class Permission:
    FOLLOW = 0x01         #关注
    COMMENT = 0x02        #评论
    WRITE_ARTICLES = 0x04 #写文章
    MODERATE_COMMENTS = 0x08 #管理文章
    ADMINISTER = 0x80        #后台管理员


class Mblog(db.Model):
    __tablename__ = 'mblog'
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))