#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: test5.py 
@time: 2018/03/10 
"""

import scrapy
import re

class quoteCfiSpider(scrapy.Spider):
    name = "quoteCfiSpider"                 #爬虫名称
    start_urls = ['http://quote.cfi.cn/stockList.aspx?t=11']
    allowed_domains = ["quote.cfi.cn"]    #域名#url列表

    #scrpay解析函数
    def parse(self, response):
        # current_url = response.url  # 爬取时请求的url
        # body = response.body  # 返回的html
        # unicode_body = response.body_as_unicode ()  # 返回的html unicode编码
        # print body
        body = response.body
        unicode_body = response.body_as_unicode ()
        stock = {}
        for sel in response.xpath ('//div[@id="divcontent"]'):
            # print sel.extract()
            stocks = sel.re (r'<td><a href=*>*(.+?)</a>(.+?)</td>')
            if not stocks:
                pass
            else:
                print stocks
                # print len(stocks)
                for it in stocks:
                    # print it
                    codestr = re.search(r'\d\d\d\d\d\d', it)
                    code = codestr.group()
                    left = re.search(r'(?<=\"\>).+?$', it)
                    leftname = left.group()
                    stocknamesplit = leftname.split("(")
                    stockname = stocknamesplit[0]
                    stock['code'] = code
                    stock['name'] = stockname
                    yield stock
                    # num1 = re.findall(r'\b\d.*\d\b', item)
                    # print num1
                    # num2 = re.search(r"(*\'", num1)
                    # print "num2:", num2







