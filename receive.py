#用于接受信息
class Security:
    # 初始化Security
    # 传入用户名、MD5（key+时间戳）、时间戳
    def __init__(self, security_dict):
        self.uname = security_dict['uname']
        self.stage=0
        if self.uname=="":
            self.stage=3
        elif type(self.uname)!=str:
            self.stage = 3
        self.key = security_dict['key']
        if self.key == "":
            self.stage = 3
        elif type(self.key) != str:
            self.stage = 3
        self.time = security_dict['time']
        if self.uname == "":
            self.stage = 3
        elif type(self.time) != float:
            self.stage = 3


class Option:
    # 初始化Option
    # 传入例句难度
    def __init__(self, option_dict):
        self.stage=0
        self.level = option_dict['level']
        if self.level == "":
            self.stage = 3
        elif type(self.level) != int:
            self.stage = 3

class Receive:
    # 初始化接收类
    # 传入接收的参数
    def __init__(self, receive_dict):
        self.stage=0
        self.receive_dict_security = receive_dict['security']
        if self.receive_dict_security =="":
            self.stage = 3
        elif type(self.receive_dict_security) != dict:
            self.stage = 3
        self.security = Security(receive_dict['security'])
        if self.security.stage == 3:
            self.stage = 3
        self.word = receive_dict['word']

        if self.word =="":
            self.stage = 3
        elif type(self.word)!=str:
            self.stage = 3
        self.receive_dict_option = receive_dict['option']
        if self.receive_dict_option == "":
            self.stage = 3
        elif type(self.receive_dict_option)!= dict:
            self.stage = 3
        self.option = Option( receive_dict['option'])
        if self.option.stage==3:
            self.stage = 3


