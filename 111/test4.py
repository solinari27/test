#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: solinari 
@file: test4.py 
@time: 2018/02/{DAY} 
"""

# from pymongo import MongoClient
import calendar
import time

# conn = MongoClient('127.0.0.1', 27017)
# # 数据库test 集合test use test db.test.find()
# db = conn.test
# mySet = db.test
#
# mySet.insert({"name": "zhangsan", "age": 18})

# print calendar.calendar
print time.time()
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print time.strftime("%Y-%m-%d", time.localtime())

print time.strftime('%Y-%m-%d %H:%M:%S',(2017,11,14,13,59,7,1,318,0))
print time.strftime('%Y-%m-%d',(2017,11,14,0,0,0,0,0,0))

timestamp = time.strptime("2014:01:01", "%Y:%m:%d")
print "stamp: ", timestamp
print "time: ", time.strftime('%Y-%m-%d',timestamp)