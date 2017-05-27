#! /usr/bin/python
# 一个简单的tcp服务器
from socket import *
from time import ctime

Host = '';
PORT = 15089;
BUFSIZ = 1024;
ADDR = (HOST, PORT);

tcpSerSock = socket(AF_INET, SOCK_STREAM);
tcpSerSock.bind(ADDR);
tcpSerSock.listen(5);

while True:
	print 'waiting for connection....'
	tcpCliSock, addr =  tcpSerSock.accept()
	print '...connected from:', addr
	tcpCliSock.send('welcome to faithfish_pi home!')
	while True:
		data = tcpCliSock.recv(BUFSIZ)
		if NOT data:
			break
		else:
			tcpSerSock.send('[%s] %s' %(ctime(),data))
	tcpCliSock.close()
tcpSerSock.close()
