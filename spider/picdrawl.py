from urllib.request import urlretrieve
import os
import requests

class PicDrawl(object):

    def __init__(self):
        self.failurl = [] #下载失败url地址列表
        self.failnum = 0 #下载失败图片数量
    def write_mblog(self,path,id,text):
        '''
            写入博客内容到相应文件夹下
        :param path: 写入路径
        :param id:  微博id
        :param text:  微博内容
        :return:
        '''
        if not os.path.exists(path+'/'+id+'.txt'):
            with(open(path+'/'+id+'.txt','w',encoding='utf-8')) as f:
                f.write(text)

    def download_pic(self,num,create_at,url,blog):
        try:
            arr = url.strip().split('/')
            filename = arr[-1]
            if '.' not in filename:
                filename = filename+'.jpg'
            print('第{0}张图片下载中......'.format(num))
            # urlretrieve(url,'../../file/zifeng/'+filename)
            # urlretrieve 很多图片都下载失败 改为直接文件写入
            path = '../../file/zifeng/{0}'.format(create_at.replace(':','：'))

            if not os.path.exists(path):
                os.makedirs(path)

            try:
                self.write_mblog(path,blog.id,blog.text)
            except:
                print('时间为:{0}的微博内容写如失败！'.format(create_at))

            with open('{0}/{1}'.format(path,filename), 'wb') as file:
                file.write(requests.get(url).content)

        except:
            arr = url.strip().split('/')
            filename = arr[-1]
            print('第{0}张图片 url:{1} 下载失败...{2}'.format(num,url,filename))
            # 下载失败的图片加入 错误列表，以供重新下载
            if url not in self.failurl:
                self.failnum += 1
                self.failurl.append(url)

    def download_wrong_pic(self,repeat):
        '''
            重新下载失败的图片
        :param repeat:
        :return:
        '''
        num =0
        for url in self.failurl:
            num += 1
            try:
                print('第{0}张错误图片下载中...还有{1}张错误图片'.format(num,self.failnum))
                filename = 'wrong_'+str(repeat)+"_"+str(num)+'.jpg'
                urlretrieve(url,'../file/zifeng/'+filename)
                self.failnum -=1
                self.failurl.remove(url)
            except:
                print('第{0}张错误图片下载失败...还有{1}张错误图片'.format(num,self.failnum))









