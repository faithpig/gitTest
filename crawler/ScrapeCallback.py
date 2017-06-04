#!/usr/bin/python
#*- coding:utf-8 -*
#爬虫爬取的回调类将html文本某些属性的value存入csv文件中
#by faithfish
#2017/06/04

import csv
import lxml.html#xml解析器
import myCrawler
import re

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

class ScrapeCallback:

	def __init__(self):
		self.writer = csv.writer(open('news.csv', 'w'))
		self.fields = ('来源', '责任编辑', '标题')
		self.writer.writerow(self.fields)
	
	def __call__(self, url, html):
		if re.search('/CM\w+(\.html)$', url):
			tree = lxml.html.fromstring(html)
			row = []
			for field in self.fields:
				if field=='来源':
					row.append(tree.cssselect('div.ep-source.cDGray >span.left')[0].text_content())
				elif field=='责任编辑':
					row.append(tree.cssselect('div.ep-source.cDGray >span.ep-editor')[0].text_content())
				else:
					row.append(tree.cssselect('div.post_content_main >h1')[0].text_content())
			self.writer.writerow(row)

if __name__ == '__main__':
	myCrawler.link_crawler('http://www.163.com/', re.compile(r'http://news\.163.*?/CM\w+(\.html)$'), scrape_callback=ScrapeCallback())
