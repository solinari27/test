#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: quoteCfiSpider.py 
@time: 2018/04/01 
"""  

import os

class quoteCfiSpider(scrapy.Spider):

    def __init__(self):

    def crawl(self):
        os.system("scrapy runspider stockcode/spider/scrapyCfiSpider.py -o Data/quoteCfiSpider.json --logfile Log/quoteCfiSpider.log --loglevel ERROR")

