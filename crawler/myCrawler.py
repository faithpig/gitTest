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
from ScrapeCallback import ScrapeCallback

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
            	html = urllib2.urlopen(request).read().decode('gbk') #解码为gbk编码
        except urllib2.URLError as e:
                print 'Download error:', e.reason
                html = None
	return html

def link_crawler(start_url, link_pat, max_depth = 10, scrape_callback=ScrapeCallback()):#max_depth为爬虫深度
	'''爬取匹配模式的url页面
	'''
	crawl_queue = [start_url]
	seen =  {} #用字典记录不重复的链接
	seen[start_url] = 1
	while crawl_queue:
		url = crawl_queue.pop()
		depth = seen[url]
		if depth != max_depth:
			html = download(url, user_agent='xc')
			links = []
			if scrape_callback:
                		links.extend(scrape_callback(url, html) or [])
			links += get_links(html)
			for link in links:
				if re.match(link_pat, link):
					link = urlparse.urljoin(start_url, link)
					if link not in seen:
						crawl_queue.append(link)
						seen[link] = depth+1
def get_links(html):
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE) # precompile
	#print webpage_regex.findall(html)
	return webpage_regex.findall(html)

if __name__ == '__main__':
        link_crawler('http://www.163.com/', re.compile(r'http://news\.163.*?/CM\w+(\.html)$')) #下载网易163的新闻网页

