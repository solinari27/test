#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Time    : 2018/4/19 19:27
#@Author  : Aries
#@Site    : 
#@File    : test7.py
#@Software: PyCharm

# import random
#
# print(random.randint(0, 9))
#
# str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
# print str.split( )
# print str.split(' ', 1 )
#
# str2 = 'aaa,bbb'
# print str2.split(',')
#
# #Code highlighting produced by Actipro CodeHighlighter (freeware)http://www.CodeHighlighter.com/-->
#
# import base64
#
# s1 = base64.encodestring('hello world')
# s2 = base64.decodestring(s1)
# print s1,s2
#
# # aGVsbG8gd29ybGQ=\n
# # hello world
import sys


from selenium import webdriver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# client = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\Program Files (x86)\Google\chromedriver\chromedriver')
#
# client.get("https://www.baidu.com")
# content = client.page_source.encode('utf-8')
# print content
# client.quit()


from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://cloud.189.cn/')