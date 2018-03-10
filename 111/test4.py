#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: solinari 
@file: test4.py 
@time: 2018/02/{DAY} 
"""

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
# 数据库test 集合test use test db.test.find()
db = conn.test
mySet = db.test

mySet.insert({"name": "zhangsan", "age": 18})


# connect db
        try:
            self.conn = pymongo.MongoClient(MONGODB_CONFIG['host'], MONGODB_CONFIG['port'])
            self.db = self.conn[MONGODB_CONFIG['db_name']]  # connect db
            self.username=MONGODB_CONFIG['username']
            self.password=MONGODB_CONFIG['password']
            if self.username and self.password:
                self.connected = self.db.authenticate(self.username, self.password)
            else:
                self.connected = True
        except Exception:
            print traceback.format_exc()
            print 'Connect Statics Database Fail.'
            sys.exit(1)


startDayStr = time.strftime('%Y-%m-%d', startDay)


