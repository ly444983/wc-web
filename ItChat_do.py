#coding=utf8
import itchat,json,requests
import threading,time

def login():
    itchat.auto_login(hotReload = True)
    itchat.run()

@itchat.msg_register('Text')
def music_player(msg):
    if msg['Text'] == "car":
        return car()
    if msg['Text'].isdigit() :
        if 898606160900007300 < int(msg['Text']) < 89860616090000730050:
            return llcx(msg['Text'])
    if msg['Text']=="cxll":
        print(1)
        return llcx("8986061609000073005")
    print(msg['Text'])
    itchat.send("get:"+msg['Text'], msg['FromUserName'])

def car():
    headers = \
        {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 3W MIUI/V7.5.6.0.MXDCNDE)',
         'encryptValue': '4Z9u1KJRrJU=',
         'host':'admin.bjev520.com'
         }
    data = {"id": "14469"}
    data_string = requests.post("http://121.42.144.98/jsp/interface/statusCharging/do/statusCharging.jsp",data=data, headers=headers).text
    data_string = json.loads(data_string)["data"]
    return (json.dumps(data_string).replace(",", "\n"))

def llcx(a):
    
    try:
        data_string= requests.post("http://ty.bdlm188.com/Home/Index/index",data ={'search_id': a}).text
        

        data_string=json.loads(data_string)["result"]
    except:
        return "!"
    else:
        return (json.dumps(data_string).replace(",", "\n"))

t = threading.Thread(target=login,args=())
t.setDaemon(True)
t.start()
def keep():
    while 1:
        time.sleep(60*10)
        itchat.auto_login(hotReload=True)

t1 = threading.Thread(target=keep,args=())
t1.setDaemon(True)
t1.start()