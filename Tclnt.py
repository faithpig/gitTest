#!/usr/bin/python
# -*- coding:utf-8 -*
# 简单的tcp客户端程序
# 2017/05/2i7

from socket import *

HOST = '10.132.21.205'
PORT = 15089
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM);
tcpCliSock.connect(ADDR)
data = tcpCliSock.recv(BUFSIZ)
print data

while True:
	data = raw_input('>')
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print data

tcpCliSock.close()
