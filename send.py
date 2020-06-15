#用于向客户端发送数据
class Sentence:
    # 初始化例句
    # 传入英文、中文例句和音频文件地址、所属电影
    def __init__(self, f_name, en,cn, voice):
        self.f_name = f_name
        self.en = en
        self.cn = cn
        self.voice = voice

    # def receive(self):
''' "fname":"电影名",
            "en":"英文原版例句",
            "cn":"中文翻译例句",
            "voice":"音频文件地址"'''

class Send:
    # 初始化发送类
    # 传入状态码、查询单词、中文释义和例句列表
    # def __init__(self, statue, word, trans, sentence_list):
    def __init__(self,  word, trans, sentence_list,length):
        self.word = word
        self.trans = trans
        self.sentences = self.sentsss(sentence_list,length)
        # # print(self.sentences[1].en)
        # print(self.sentences)
    def sentsss(self,sentence_list,length):
        vam =[]
        sent=sentence_list
        for i in range(length):
            java=Sentence(sent[i][0],sent[i][1],sent[i][2],sent[i][3])
            vam.append(java.__dict__)
        # print(vam)
        return vam

    def to_dict(obj):
        dict = {}
        dict.update(obj.__dict__)
        # print(dict)
        return dict
