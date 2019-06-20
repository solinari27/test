#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: test4.py
@time: 2018/02/{DAY}
"""

import time

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
# 数据库test 集合test use test db.test.find()
db = conn['test']
mySet = db['test']
mySet.remove({})
mySet.insert({"name": "zhangsan", "age": 18})

mySet.update({"name": "zhangsan"}, {"$set": {"age": 20}})
# 查一个collection
# print(mySet)
# print("test_collection")
array = mySet.find({"name": "zhangsan"})
for doc in array:
    print(doc)

db2 = conn.stockinfo
now = time.gmtime()
nowDate = time.strptime(str(now.tm_year) + ":" +
                        str(now.tm_mon) + ":" + str(now.tm_mday), "%Y:%m:%d")
print nowDate
un_time = time.mktime(nowDate)
print un_time  # 1509636609.0
# data = {}
# data['updatetime'] = nowDate
# db2.stocklist.update({"code": "600011"}, {"$set":data})

mySet.insert({"xxx": "aaa", "date": un_time})
array = mySet.find({"xxx": "aaa"})
for doc in array:
    print(doc)
    time_local = time.localtime(doc['date'])
    print time_local
    print time_local.tm_year

# # connect db
#         try:
#             self.conn = pymongo.MongoClient(MONGODB_CONFIG['host'], MONGODB_CONFIG['port'])
#             self.db = self.conn[MONGODB_CONFIG['db_name']]  # connect db
#             self.username=MONGODB_CONFIG['username']
#             self.password=MONGODB_CONFIG['password']
#             if self.username and self.password:
#                 self.connected = self.db.authenticate(self.username, self.password)
#             else:
#                 self.connected = True
#         except Exception:
#             print traceback.format_exc()
#             print 'Connect Statics Database Fail.'
#             sys.exit(1)
#
#
# startDayStr = time.strftime('%Y-%m-%d', startDay)
