#! /usr/bin/python
#*- coding:utf-8 -*
#一个简单的爬虫程序 by faithpig
#2015/06/03

import re
import urlparse
import urllib2
import time
from datetime import datetime
import robotparser
import Queue

'''
设置python编码为utf-8,默认为ascii
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''

def download(url, user_agent='xc'):
        print 'downloading:', url
        headers = {'User-agent':user_agent}
        request = urllib2.Request(url,headers=headers)
        try:
            	html = urllib2.urlopen(request).readlines()
        except urllib2.URLError as e:
                print 'Download error:', e.reason
                html = None
        for line in html:
                print line
if __name__ == '__main__':
        download('http://xcfish.cn/MyBlog/','xc')
