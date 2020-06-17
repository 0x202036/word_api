#用于接受信息
class Security:
    # 初始化Security
    # 传入用户名、MD5（key+时间戳）、时间戳
    def __init__(self, security_dict):
        self.uname = security_dict['uname']
        self.key = security_dict['key']
        self.time = security_dict['time']


class Option:
    # 初始化Option
    # 传入例句难度
    def __init__(self, option_dict):
        self.level = option_dict['level']


class Receive:
    # 初始化接收类
    # 传入接收的参数
    def __init__(self, receive_dict):
        self.security = Security(receive_dict['security'])
        self.word = receive_dict['word']
        self.option = Option(receive_dict['option'])


