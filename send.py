#用于向客户端发送数据

class Sentence(object):
    # 初始化例句
    # 传入英文、中文例句和音频文件地址、所属电影
    def __init__(self, f_name, en ,cn , voice):
        self.fname = f_name
        self.en = en
        self.cn = cn
        self.voice = voice

    def keys(self):
        '''当对实例化对象使用dict(obj)的时候, 会调用这个方法,这里定义了字典的键, 其对应的值将以obj['name']的形式取,
        但是对象是不可以以这种方式取值的, 为了支持这种取值, 可以为类增加一个方法'''
        return ( "fname", "en" , "cn" , "voice")

    def __getitem__(self, item):
        '''内置方法, 当使用obj['name']的形式的时候, 将调用这个方法, 这里返回的结果就是值'''
        return getattr(self, item)

class Send:
    # 初始化发送类
    # 传入状态码、查询单词、中文释义和例句列表
    def __init__(self, statue, word, trans, sentence_list,length):
        self.statue =statue
        self.word = word
        self.trans = trans
        tt=sentence_list
        if(tt==[['', '', '', '']]):
            self.sentences = []
        elif tt==[]:
            self.sentences=[]
            # print("例句正常")
        else:
            self.sentences = self.sentsss(tt,length)

    def keys(self):
        return ('statue','word','trans' ,'sentences')

    def __getitem__(self, item):
        return getattr(self, item)

    def sentsss(self,sentence_list,length):
        vam =[]
        sent = sentence_list
        print(sent)
        for i in range(length):
            hhh =dict(Sentence(sent[i][0], en=sent[i][2], cn=sent[i][1], voice=sent[i][3]))
            vam.append(hhh)
        return vam
