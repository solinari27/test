#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: solinari
@file: test9.py
@time: 2018/06/06
"""

import urllib2;
import requests;
import json;

boundary = '-----------------------------1585359196875797843831364763'
data = []
data.append ('--%s' % boundary)
data.append ('Content-Disposition: form-data; name="sessionKey"\r\n')
data.append ('xxxxxx')
data.append ('--%s' % boundary)
data.append ('Content-Disposition: form-data; name="parentId"\r\n')
data.append ('9139432089925930')
data.append ('--%s' % boundary)
data.append ('Content-Disposition: form-data; name="albumId"\r\n')
data.append ('undefined')
data.append ('--%s' % boundary)
data.append ('Content-Disposition: form-data; name="opertype"\r\n')
data.append ('5')
data.append ('--%s' % boundary)
data.append ('Content-Disposition: form-data; name="fname"\r\n')
data.append ('xxxxx')
data.append ('--%s' % boundary)
data.append ('Content-Disposition: form-data; name="Filedata"; filename="Readme.txt"')
data.append ('Content-Type: text/plain\r\n')

fr = open ('white.jpg')
content = fr.read ()
data.append (content)
# print content
fr.close ()
data.append ('--%s--\r\n' % boundary)
httpBody = '\r\n'.join (data)

# print type (httpBody)
print httpBody

postDataUrl = 'http://xxxxxxxx'
# req = urllib2.Request (postDataUrl, data=httpBody)
req = requests.Request(postDataUrl, data=httpBody)

