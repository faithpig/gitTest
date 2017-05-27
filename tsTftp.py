#! /usr/bin/python
# -*- coding:utf-8 -*-
# 一个简单的建立ftp连接获取文件的程序
# 2017/05/27

import ftplib
import os
import socket

HOST = 'ftp.debian.com'
DIRN = 'debian/doc/dedication/'
FILE = 'dedication-2.2.sigs.tar.gz'

def main():
	try:
		f = ftplib.FTP(HOST)
	except (socket.error, socket.gaierror) as e:
		print 'ERROR: cannot connect host %s' %HOST
		return
	try:
		f.login()
	except ftplib.error_perm as e:
		print 'ERROR: cannot login anonymously'
		f.quit()
		return
	try:
		f.cwd(DIRN)
	except ftplib.error_perm:
		print 'ERROR: cannot CD to %s Folder' %DIRN
		f.quit()
		return
	file = open(FILE,'wb')
	try:
		f.retrbinary('RETR %s' %FILE, file.write)
	except ftplib.error_perm:
		print 'cannot read file %s' %FILE
		os.unlink(FILE) #删除文件
	else:
		print '*** Downloaded %s to CWD' %FILE
	f.quit()

if __name__ == '__main__':
	main()



