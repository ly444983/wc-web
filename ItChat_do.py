#coding=utf8
import itchat,json,requests
import threading

def login():
    itchat.auto_login(hotReload = True)
    itchat.run()

@itchat.msg_register('Text')
def music_player(msg):
    if msg['Text'] == "car":
        return car()
    if msg['FromUserName'] != msg['ToUserName']:
        return
#        if itchat.__client.web_init()["UserName"]!=msg['ToUserName']:
    if msg['Text'].isdigit() :
        if 898606160900007300 < int(msg['Text']) < 89860616090000730050:
            return llcx(msg['Text'])
    elif msg['Text']=="cxll":
        return llcx("8986061609000073005")
    
def car():
    cookies = {"JSESSIONID": "F91124FB808BFA61AF8C8321BE90FAEB"}
    headers = \
        {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 3W MIUI/V7.5.6.0.MXDCNDE)',
         'encryptValue': '4Z9u1KJRrJU='
         }
    data = {"id": "14469"}
    data_string = requests.post("http://admin.bjev520.com/jsp/interface/statusCharging/do/statusCharging.jsp",
                                data=data, headers=headers).text

    data_string = json.loads(data_string)["data"]
    return (json.dumps(data_string).replace(",", "\n"))
def llcx(a):
    try:
        data_string=requests.get("http://10010.mahalian.cn/Home/Index/index?search_id="+a).text
        data_string=json.loads(data_string)["result"]["left_usage"]
    except:
        return "!"
    else:
        return str(data_string)

t1 = threading.Thread(target=login,args=())
t1.setDaemon(True)
t1.start()