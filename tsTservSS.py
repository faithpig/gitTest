#!/usr/bin/python
#-*- coding:utf-8 *-
#基于SocketServer模块的tcp服务器,继承StreamRequestHandler类并重写handler方法，事件驱动。
#2017/05/27

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 15789
ADDR = (HOST,PORT)

class MyHandler(SRH):
	def handle(self):
		print 'connect from:', self.client_address
		self.wfile.write('[%s] %s' %(ctime(), self.rfile.readline()))
tcpServ = TCP(ADDR,MyHandler)
print 'waiting for connetion...'
tcpServ.serve_forever()
