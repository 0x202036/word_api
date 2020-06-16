from flask import Flask,request,jsonify
import db_manager
import receive
import check
import send
app = Flask(__name__)

@app.route("/",methods=["POST"])
#主交互函数
#get_receive_info(raw_info):
#调用Db_manager.get_send_data(👆)
#返回 get_send_json(send)
def api_main():
    try:
        my_json =request.get_json()
        obj_receive = receive.Receive(my_json)
        # print(obj_receive.option.level)
        obj_check = check.Check(receive=obj_receive)
        result = obj_check.begin_check()
        print(result)
        if result == "safe":
            print(1)
        else:
            obj_db_manager = db_manager.Db_Manager(receive=obj_receive)
            obj_get_word_data = obj_db_manager.get_send_data()
            if obj_get_word_data == "NULL":
                return jsonify("该单词未录入")
            obj_send = send.Send(obj_get_word_data[0], obj_get_word_data[1], obj_get_word_data[2], obj_get_word_data[3])
            fasong = get_send_json(obj_send)
        return jsonify(fasong)
    except Exception as e:
        return jsonify(msg="您的消息缺失")

# 将send对象序列化为json字符串
def get_send_json(obj):
    dict = {}
    dict.update(obj.__dict__)
    print(dict)
    return dict

if __name__ == '__main__':
    app.run()
