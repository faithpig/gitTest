#!/usr/bin/python
# -*- coding:utf-8 -*
#基于SocketServer模块TCP客户端
#2017/05/27

from socket import *

HOST = '10.132.21.205'
PORT = 15789
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
	tcpCliSoc = socket(AF_INET, SOCK_STREAM)
	tcpCliSoc.connect(ADDR)
	data = raw_input('>')
	if not data:
		break
	tcpCliSoc.send('%s\r\n' %data)
	data = tcpCliSoc.recv(BUFSIZ)
	if not data:
		break
	print data.strip()
	tcpCliSoc.close()
