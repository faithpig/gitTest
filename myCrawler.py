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
            	html = urllib2.urlopen(request).read()
        except urllib2.URLError as e:
                print 'Download error:', e.reason
                html = None
	return html

def link_crawler(start_url, link_pat):
	'''爬取匹配模式的url页面
	'''
	crawl_queue = [start_url]
	while crawl_queue:
		url = crawl_queue.pop()
		html = download(url, user_agent='xc')
		for link in get_links(html):
			if re.match(link_pat, link):
				link = urlparse.urljoin(start_url, link)
				crawl_queue.append(link)
def get_links(html):
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE) #这个正则表达式略复杂...匹配了a标签里的链接
	print webpage_regex.findall(html)
	return webpage_regex.findall(html)

if __name__ == '__main__':
        link_crawler('http://xcfish.cn/MyBlog/','.*/home_viewBlog')
