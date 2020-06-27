#用于验证合法用户
import time
import hashlib
import db_manager
class Check():
    def __init__(self,receive):
        # 允许超时
        self.__over_time = 5
        # 超时时间内访问的MD5值
        self.__visited_dict ={}
        self.client_time = receive.security.time
        self.server_time = time.time()
        self.client_MD5 = receive.security.key
        self.uname =receive.security.uname
        self.receive =receive
        # 禁止五秒前的访问
    def __check_over_time(self):
        client_time = self.client_time
        server_time = self.server_time
        if client_time + 5 < server_time:
            return "超时！"

    # 查询并更新字典，禁止五秒内重复的访问
    def __check_revisit(self):
        '''字典遍历时不能修改元素'''
        for k in list(self.__visited_dict.keys()):
            if int(self.__visited_dict[k]) +5 < self.server_time:
                del self.__visited_dict[k]
                continue
        if self.__visited_dict.get(self.client_MD5)==None:
            self.__visited_dict[self.client_MD5] = self.client_time
        else:return "拒绝使用重复信息"

    # 查询数据库，得到密钥+时间戳的MD5值
    def __generate_md5(self,u_k):
        u_key = u_k
        self.pwd = str(u_key) + str(self.client_time)
        chachong=self.__visited_dict.get('addr')
        # hashlib.md5加密不支持类型转换，故都转为字符串
        self.server_MD5key = hashlib.md5(self.pwd.encode("latin1")).hexdigest()
        if self.server_MD5key != self.client_MD5:
            return "休想"


    # 开始检测
    def begin_check(self):
        message = {}
        message[0] = self.__check_over_time()
        if message[0] == "超时！":
            return message[0]
        else:
            message[1] = self.__visited_dict
        if message[1] == "拒绝使用重复信息":
            return message[1]
        else:
            self.obj_db = db_manager.Db_Manager(self.receive)
            key = self.obj_db.get_user_data()
            message[2] = self.__generate_md5(key)
            if message[2] == "休想":
                #self.obj_db.close()
                return message[2]
            else:
                return "safe"
