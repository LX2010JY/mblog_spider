#-*- coding:utf-8-*-

class BlogInfo(object):
    def __init__(self):
        '''
            将每篇微博内容存入此类对象
            /user/create_at/pic
        '''
        self._user = ''
        self._create_at = ''
        self._id = ''
        self._text = ''
        self._original_pic = ''
        self._pics = []

    @property
    def user(self):
        return self._user
    @user.setter
    def user(self,value):
        self._user = value

    @property
    def create_at(self):
        return self._create_at
    @create_at.setter
    def create_at(self,value):
        self._create_at = value

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,value):
        self._id = value

    @property
    def text(self):
        return self._text
    @text.setter
    def text(self,value):
        self._text = value

    @property
    def original_pic(self):
        return self._original_pic
    @original_pic.setter
    def original_pic(self,value):
        self._original_pic = value
    @property
    def pics(self):
        return self._pics
    @pics.setter
    def pics(self,value):
         self._pics = value

