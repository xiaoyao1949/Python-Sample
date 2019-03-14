import itchat,time,re,requests
from threading  import Timer
from itchat.content import *
def get_tl_res(msg):
    url = "http://www.tuling123.com/openapi/api"
    data = {
        "key": "75137612d89c42f0b9d7a3f5133ec656",# 自己注册图灵，获取KEY
        "info": msg,
        "userid": "pth-robot"
    }
    res = requests.post(url, data=data).json()
    return res.get("text")
@itchat.msg_register([TEXT],isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        res = get_tl_res(msg["Text"])
        itchat.send((res), msg["FromUserName"])
@itchat.msg_register([PICTURE,RECORDING,VIDEO,SHARING],isGroupChat=True)
def other_reply(msg):
    if  msg['isAt']:
        res = get_tl_res(msg[PICTURE,RECORDING,VIDEO,SHARING])
        itchat.send((res),msg["FromUserName"])
itchat.login()
itchat.run()