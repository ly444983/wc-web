#coding=utf8
import time,os,json
import threading
import requests
from flask import Flask,request,render_template,send_from_directory
app = Flask(__name__,static_url_path='')
PORT = int(os.getenv('PORT', 80))


@app.route('/')
def index():
    return "0"
def llcx(search_id):
    headers = \
        {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 3W MIUI/V7.5.6.0.MXDCNDE)',
         'host': 'ty.bdlm188.com'
         }
    data_string =requests.post("http://114.55.129.75/Home/Index/index",data ={'search_id': search_id}, headers=headers).text
    data =json.loads(data_string)["result"]
    left_usage = data["left_usage"]
    try:
        return render_template('llcx2.html', t=left_usage, d=json.dumps(data))
    except:
        return render_template('llcx2.html',t="!")
@app.route('/llcx')
def llcx_():
        return llcx(8986061609000073005)
@app.route('/llcx2')
def llcx_2():

        return llcx(8986061609000069357)
@app.route('/llcx-lr')
def llcx_lr():
        return llcx(8986061609000070286)
@app.route('/llcxany/<a>')
def llcxany(a):
        return llcx(int(a))

@app.route('/favicon.ico')
def favicon():
    return send_from_directory("templates",'favicon.ico')
@app.route('/file/<a>')
def file(a):
    return send_from_directory("file",a)
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
    os.remove(local_filename)

def keep():
    while 1:
        time.sleep(60*10)
        requests.get("http://ly0.herokuapp.com/survive").text

def format(s):
    return s.replace(",", "\n").replace('"', "")

@app.route('/car')
def car():
    headers = \
        {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 3W MIUI/V7.5.6.0.MXDCNDE)',
         'encryptValue': '4Z9u1KJRrJU=',
         'host':'admin.bjev520.com'
         }
    data = {"id": "14469"}
    data_string = requests.post("http://121.42.144.98/jsp/interface/statusCharging/do/statusCharging.jsp",data=data, headers=headers).text
    data_string = json.loads(data_string)["data"]
    t=int(data_string["travelTimeDate"])/1000+8*60*60
    data_string["travelTimeDate"]= time.strftime('%y-%m-%d %H:%M:%S',time.gmtime(t))
    return "<pre>"+format(json.dumps(data_string))

t1 = threading.Thread(target=keep,args=())
t1.setDaemon(True)
#t1.start()

app.run(host='0.0.0.0',port=PORT)
