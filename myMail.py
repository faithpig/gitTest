#! /usr/bin/python
#*-* coding:utf-8 -*
#邮件接收（pop协议）、发送（smtp协议）的客户端程序
#2017/05/28

from smtplib import SMTP_SSL
from poplib import POP3_SSL
from time import sleep

SMTPSER = 'smtp.qq.com'
POP3SER = 'pop.qq.com'
SMTPPORT = 465
POPPORT = 995

uname = '446546739@qq.com'
password = '*****' #这部分用自己的服务商给的密码就行
body = '''\
From: %(uname)s
TO: %(uname)s
Subject: test msg

Hello World!
''' %{'uname' : uname}

sendSvr = SMTP_SSL(SMTPSER, SMTPPORT)
sendSvr.login(uname, password)
errs = sendSvr.sendmail(uname, [uname], body)
sendSvr.quit()
assert len(errs) == 0, errs
sleep(10)

recvSvr = POP3_SSL(POP3SER, POPPORT)
recvSvr.user(uname)
recvSvr.pass_(password)
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('') #定位到消息正文
recvBody = msg[sep+1:]
print recvBody
recvSvr.quit()
