#coding=utf8
import itchat,json,requests
import threading

def login():
	itchat.auto_login(hotReload = True)
	itchat.run()

@itchat.msg_register('Text')
def music_player(msg):
	if msg['FromUserName'] != msg['ToUserName']:
		return
#		if itchat.__client.web_init()["UserName"]!=msg['ToUserName']:
	if msg['Text'].isdigit() :
		if 898606160900007300 < int(msg['Text']) < 89860616090000730050:
			return llcx(msg['Text'])
	elif msg['Text']=="cxll":
		return llcx("8986061609000073005")

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