# from flask import Flask,request,jsonify
import db_manager
import check
import receive
import send
# '''本地跑了一遍项目'''
# def first_post():
#     my_json = {'security': {'uname': "amy", 'key': 12323, 'time': "2321", }, 'word': 'abc', 'option': {'level':1}}
#     shuju=receive.Receive(my_json)
#     receive1 = {'word' :shuju.word,'level':shuju.option.level}
#
#     yanzheng =db_manager.Db_Manager(receive=shuju)
#     key=yanzheng.get_user_data()
#     ch =check.Check(client_time=shuju.security.time,client_MD5=shuju.security.key,u_key=key)
#     ch.begin_check()
#     chaci =yanzheng.get_send_data()
#     finly = send.Send(chaci[0],chaci[1],chaci[2],chaci[3])
#     # print(finly)
#     to_dict(finly)
#     # 将目前对象转换为字典
# def to_dict(obj):
#     dict = {}
#     dict.update(obj.__dict__)
#     print(dict)
#     return dict
# first_post()
# 将send对象序列化为json字符串
# def get_send_json(send):
#     json.dumps(send.to_dict())
# my_json=request.get_json()
# receive.Receive(my_json)
# yanzheng = db_manager.Db_Manager(receive=shuju)
# key = yanzheng.get_user_data()
# ch = check.Check(client_time=shuju.security.time, client_MD5=shuju.security.key)
# fankui=ch.begin_check()
# if fankui =="safe":
#     chaci = yanzheng.get_send_data()
#     finly = send.Send(chaci[0], chaci[1], chaci[2], chaci[3])
#     back_json = send.Send.to_dict(finly)
#     # 将目前对象转换为字典
#     print(back_json)
#     return jsonify(back_json)
# else:return jsonify(fankui)
my_json={"security": {
    "uname": "amy", "key": 12323, "time": 2321
    },
 "word": "a",
  "option": {
      "level":1
      }
      }
obj_receive =receive.Receive(my_json)
print(obj_receive.option.level)
obj_check =check.Check(receive=obj_receive)
result=obj_check.begin_check()
if result =="safe":
    print(1)
else:
    obj_db_manager=db_manager.Db_Manager(receive=obj_receive)
    obj_get_word_data=obj_db_manager.get_send_data()
    obj_send = send.Send(obj_get_word_data[0], obj_get_word_data[1], obj_get_word_data[2], obj_get_word_data[3])
    print(obj_send)
        # fasong = get_send_json(obj_send)