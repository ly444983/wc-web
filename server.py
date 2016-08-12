#coding=utf8
import time,os,json,thread
import ItChat_do
from ItChat_do import itchat
import requests
from flask import Flask,request,render_template,redirect,send_from_directory
app = Flask(__name__,static_url_path='')
PORT = int(os.getenv('PORT', 80))

@app.route('/senda/<a>')
def senda(a):
	try:
		itchat.send(request.headers.get("X-Client-Ip")+","+a+","+request.headers.get('User-Agent'),itchat.__client.web_init()["UserName"])
		return "OK"
	except Exception as e:
		return str(e)
@app.route('/')
def index():
	if os.path.exists('QR.jpg'):
		itchat.__client.showedQR=1
		return send_from_directory("","QR.jpg")
	return itchat.__client.web_init()["NickName"]
@app.route('/llcx')
def llcx():
	a='8986061609000073005'
	try:
		data_string=requests.get("http://10010.mahalian.cn/Home/Index/index?search_id="+a).text
		
		data_string=json.loads(data_string)["result"]["left_usage"]
	except:
		return render_template('llcx2.html',t="!")
	else:
		return render_template('llcx2.html',t=data_string)

@app.route('/favicon.ico')
def favicon():
    return "",404
@app.route('/rn')
def rn():
    return send_from_directory("templates",'rnWatcher.html')
@app.route('/js/<name>')
def js(name):
    return send_from_directory("templates",name)
@app.route('/d')
def d():
	thread.start_new_thread(dAs,(request.args.get('url'),))
	return "ok",200

def dAs(url):
    print (url)
    local_filename = url.split('/')[-1]  
    r = requests.get(url, stream=True) # here we need to set stream = True parameter  
    with open(local_filename, 'wb') as f: f.write(r.content)
    itchat.send('@img@'+local_filename)


app.run(host='0.0.0.0',port=PORT)
