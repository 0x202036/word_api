from flask import Flask,request,jsonify
import db_manager
import receive
import check
import send
import json
app = Flask(__name__)
# 0:成功，1：没有单词，2：用户认证失败，3：传入数据格式错误
@app.route("/",methods=["POST"])
#主交互函数
#get_receive_info(raw_info):
#调用Db_manager.get_send_data(👆)
#返回 get_send_json(send)
def api_main():
    try:
        my_json =request.get_json()
        obj_receive = receive.Receive(my_json)
        if obj_receive.stage==3:
            angle11 = (obj_receive.word, '', [['', '', '', '']], 1)
            angle_send11 = send.Send(3, angle11[0], angle11[1], angle11[2], angle11[3])
            angle_zhazha11 = dict(angle_send11)
            angle_j11 = json.dumps(obj=angle_zhazha11)
            return angle_j11

        obj_check = check.Check(receive=obj_receive)
        print(4)
        result = obj_check.begin_check()
        angle = (obj_receive.word, '', [['', '', '', '']], 1)
        if result == "safe":
            '''应为result !="safe:
            return jsonify(result)方便测试其他数据'''
            angle_send = send.Send( 0,angle[0],angle[1],angle[2],angle[3])
            angle_zhazha = dict(angle_send)
            angle_j = json.dumps(obj=angle_zhazha)
            return angle_j
        else:
            obj_db_manager = db_manager.Db_Manager(receive=obj_receive)
            obj_get_word_data = obj_db_manager.get_send_data()
            if obj_get_word_data == "NULL":
                Null_angle_send = send.Send(1, angle[0], angle[1], angle[2], angle[3])
                Null_angle_zhazha = dict(Null_angle_send)
                Null_angle_j = json.dumps(obj=Null_angle_zhazha)
                #该单词未录入
                return Null_angle_j
            obj_send = send.Send( 0,obj_get_word_data[0],obj_get_word_data[1],obj_get_word_data[2],obj_get_word_data[3])
            zhazha=dict(obj_send)
            j = json.dumps(obj=zhazha)
            return j

    except Exception as e:
        angle12 =("", '', [['', '', '', '']], 1)
        angle_send = send.Send( 4,angle12[0],angle12[1],angle12[2],angle12[3])
        angle_zhazha = dict(angle_send)
        angle_j = json.dumps(obj=angle_zhazha)
        print("异常")
        return angle_j
if __name__ == '__main__':
    app.run()
