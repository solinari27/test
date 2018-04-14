#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: liangyeeUser.py 
@time: 2018/04/14 
"""  

import json
from pymongo import MongoClient

with open ('../Conf/liangyee.conf') as f:
    liangyeeConf = json.load (f)

#init
mongoconf = liangyeeConf['mongo']
mongohost = mongoconf['host']
mongoport = int(mongoconf['port'])

with open ('info/mailbox.json') as f:
    mailboxs = json.load(f)

for item in mailboxs:
    print item
    print mailboxs[item]['key']


# conn = MongoClient(mongohost, mongoport)
# # 数据库test 集合test use test db.test.find()
# db = conn.stockinfo
# mySet = db.liangyee


# mySet.insert({"name": "zhangsan", "age": 18})

# conn.close()