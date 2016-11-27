# -*-coding:utf-8-*-
from sqlalchemy import Column,String,create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from getindex import getindex
from getmblog import GetMblog
from bloginfo import BlogInfo
from picdrawl import PicDrawl
import json
Base = declarative_base()
class User(Base):
    __tablename__='mblog'

    id = Column(Integer,primary_key=True)
    name = Column(String)
    mblog_text = Column(String)
    mblog_id = Column(String,unique=True)
    pic_json = Column(String)
    create_at = Column(String)

if __name__ == '__main__':
    # create_engine 初始化数据库
    engine = create_engine('mysql+pymysql://root:@localhost:3306/tes_db?charset=utf8')
    # DBSession可视为当前数据库的连接
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    url = 'http://m.weibo.cn/container/getIndex?containerid=2304131353112775_-_WEIBO_SECOND_PROFILE_MORE_WEIBO&uid=1788130832&page={0}'
    page = 0
    mblog = GetMblog()
    pdrawl = PicDrawl()
    while page<116:
        sina = getindex(url.format(page))
        jdict = sina.crawl()
        mblog.writeinfo(jdict)
        page+=1
    print('微博条数:',len(mblog.mblog_data))
    print('字符解析错误数:',mblog.codecnum)
    num=1
    for blog in mblog.mblog_data:
        print('第{0}条信息写入'.format(num))
        pics = json.dumps(blog.pics)
        try:
            new_user = User(name='张子枫', mblog_text=blog.text, mblog_id=blog.id, pic_json=pics, create_at=blog.create_at)
            session.add(new_user)
            session.commit()
        except:
            print("第{0}条写入失败".format(num))
        num+=1
    session.close()
    print('数据库写入完毕。')
