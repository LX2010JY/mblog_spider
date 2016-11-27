from bloginfo import BlogInfo
import json
import re
import sys
class GetMblog(object):
    def __init__(self):
        self.blognum = 0
        self.codecnum = 0
        self.mblog_data = []
        self.blogtext = open('./file/zifeng.txt','a',encoding='utf-8')

    def writeinfo(self,jsoninfo):
        jsoninfo = json.loads(jsoninfo, encoding='utf-8')
        if 'cards' not in jsoninfo:
            # print('page:{0} cards 不存在...'.format(self.page))
            return
        cards = jsoninfo['cards']
        for blog in cards:
            bgin = BlogInfo()
            if 'mblog' in blog:
                mblog = blog['mblog']
                self.blognum+=1
                # 创建时间
                bgin.create_at = mblog['created_at']
                bgin.id = mblog['id']
                # 将微博内容写入bloginfo对象
                text = mblog['text']
                bgin.text = re.sub(r'</?\w+[^>]*>','',text)
                try:
                    print('第{0}条微博内容:{1}'.format(self.blognum,bgin.text))
                    self.blogtext.write('第{0}条微博内容:{1}'.format(self.blognum,bgin.text))
                    self.blogtext.write('\n\n')
                except:
                    self.codecnum += 1
                    print('第{0}条微博内容:字符解析错误...'.format(self.blognum))
                    self.blogtext.write('第{0}条微博内容:字符解析错误...'.format(self.blognum))
                    self.blogtext.write('\n\n')
                # 写入微博图片地址
                if 'pics' in mblog:
                    pics = []
                    for pic in mblog['pics']:
                        pics.append(pic['large']['url'])
                    bgin.pics = pics
                # 不知道这是什么图片，判断其是否在pics中，不在就添加进去
                if 'original_pic' in mblog:
                    original_pic = mblog['original_pic']
                    if original_pic not in bgin.pics:
                        bgin.pics.append(original_pic)
                # 将每条微博对象存入mblog_data 也就是整个程序目前只能用一个GetImage对象，存储一个人所有微博信息
                self.mblog_data.append(bgin)

