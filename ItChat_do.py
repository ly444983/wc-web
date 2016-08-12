#coding=utf8
import itchat,os,random
import thread

def login():
	itchat.auto_login(hotReload = True)
	itchat.run()
thread.start_new_thread(login,())
