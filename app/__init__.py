'''
    这个文件大概是初始化各种扩展的作用（构造文件）
'''
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from config import config

async_mode = "threading"

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
socketio = SocketIO(async_mode=async_mode)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # 下面看不懂，反正大概就是初始化各种扩展，将app对象传进去
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    socketio.init_app(app)
    # 只能写在下面，据说为了避免循环导入依赖 ， 给程序注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
