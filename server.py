#coding=utf8
import time,os,json
import threading
import ItChat_do
from ItChat_do import itchat
import requests
from flask import Flask,request,render_template,redirect,send_from_directory
app = Flask(__name__,static_url_path='')
PORT = int(os.getenv('PORT', 80))

@app.route('/senda/<a>')
def senda(a):
    try:
        itchat.send(request.META.get("REMOTE_ADDR")+","+a+","+request.headers.get('User-Agent'),itchat.__client.web_init()["UserName"])
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
    return send_from_directory("templates",'favicon.ico')

@app.route('/rn')
def rn():
    return send_from_directory("templates",'rnWatcher.html')

@app.route('/d')
def d():
    t1 = threading.Thread(target=dAs,args=(request.args.get('url'),))
    t1.setDaemon(True)
    t1.start()
    return "ok",200
global a
a=[]
def dAs(url):
    local_filename = url.split('/')[-1]
    if local_filename in a:
        print(local_filename+" is downloaded")
        return
    a.append(local_filename)
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f: f.write(r.content)
    itchat.send('@img@'+local_filename)
    os.remove(local_filename)

def keep():
    while 1:
        time.sleep(60*10)
        requests.get("http://ly0.herokuapp.com/favicon.ico").text

t1 = threading.Thread(target=keep,args=())
t1.setDaemon(True)
t1.start()

app.run(host='0.0.0.0',port=PORT)
