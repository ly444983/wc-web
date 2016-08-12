#coding=utf8
import itchat,os,random
import threading

def login():
	itchat.auto_login(hotReload = True)
	itchat.run()


t1 = threading.Thread(target=login,args=(,))
t1.setDaemon(True)
t1.start()