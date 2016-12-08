# coding:utf-8
import os
'''
    配置文件
'''
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_PER_PAGE = 10
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = '2810752073@qq.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = True
    MAIL_USERNAME = '2810752073@qq.com'
    MAIL_PASSWORD = 'vufmglghcajgddca'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/flask'

class TestingConfig(Config):
    Testing = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/tes_db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/pro_db'

config = {
    'development' : DevelopmentConfig,
    'testing'      : TestingConfig,
    'production'   : ProductionConfig,
    'default'      : DevelopmentConfig
}
