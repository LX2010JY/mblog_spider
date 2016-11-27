from getindex import getindex
from getmblog import GetMblog
from bloginfo import BlogInfo
from picdrawl import PicDrawl

if __name__ == '__main__':
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

    num = 1
    for blog in mblog.mblog_data:
        pics = blog.pics
        for pic in pics:
            pdrawl.download_pic(num,blog.create_at,pic,blog)
            num+=1
    repeat = 0
    # while pdrawl.failnum>1:
    #     print('又一次轮回，又失败了，再来吧，还有{0}张失败'.format(pdrawl.failnum))
    #     pdrawl.download_wrong_pic(repeat)
    #     repeat += 1
