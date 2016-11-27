#-*-coding:utf-8-*-
import requests
import json
from bloginfo import BlogInfo

class getindex(object):
    def __init__(self,url):
        self.url = url
        self.header = {
            'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'cookie' : 'ALF=1482675243; SCF=AoKQadfeZf-w9AQPbDJLBbNjBvF2U5jJ9fyp1PkUk7GCvVmuAi883fY7HDpMBp_qibWqLRmkSsVdVIzlFlD9Au0.; SUB=_2A251PUbJDeTxGedJ41oQ8y7EyD6IHXVW3mqBrDV6PUJbktAKLVXFkW0uLXl9YFWocp1_-M2BR2igu9it9Q..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW4WZjyTH6gV_1VJTUaDWeE5JpX5o2p5NHD95QpS0nReKe71heEWs4DqcjCi--Ni-iFiKn0i--Ni-ihiK.R; SUHB=0h1YlmL4iwOyDv; SSOLoginState=1480144537; _T_WM=28b38d62a30abf82898e7b98b8c07753; H5_INDEX=3; H5_INDEX_TITLE=%E7%BB%83%E7%BC%98; M_WEIBOCN_PARAMS=featurecode%3D20000181%26luicode%3D10000011%26lfid%3D2304131353112775_-_WEIBO_SECOND_PROFILE_MORE_WEIBO%26fid%3D2304131353112775_-_WEIBO_SECOND_PROFILE_MORE_WEIBO%26uicode%3D10000011'
        }
    def crawl(self):
        '''
            获取每页的json数据，变为对象并返回
        :return:
        '''
        res = requests.get(self.url,headers=self.header).text
        res = res.replace('\/','/')
        mjson = json.loads(res,encoding='utf-8')
        return res

if __name__ == '__main__':
    url = 'http://m.weibo.cn/container/getIndex?containerid=2304131353112775_-_WEIBO_SECOND_PROFILE_MORE_WEIBO&uid=1788130832&page=4'
    sina = getindex(url)
    response = sina.crawl()
    res = response.text
    res = res.replace('\/','/')
    zifeng = json.loads(res,encoding='utf-8')
    cards = zifeng['cards']
    for blog in cards:
        if 'mblog' in blog:
            mblog = blog['mblog']
            text = mblog['text']
            if 'original_pic' in mblog:
                pics = mblog['original_pic']
                print(pics)
            if 'pics' in mblog:
                pics = []
                for i in mblog['pics']:
                    pics.append(i['large']['url'])
                    # print(i['large']['url'])
                print(pics)
    print(len(cards))
    with(open('../../file/sina.json','w',encoding='utf-8')) as f:
        f.write(res)
    # print(response)
#