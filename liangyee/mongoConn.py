#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: mongoConn.py 
@time: 2018/02/25 
"""  

from pymongo import MongoClient
import sys
import json
import time
import logging

class mongoConn():

    def __init__(self):
        #注意路径配置
        with open('Conf/liangyee.conf') as f:
            self._mongoConf = json.load(f)

        #init logging:
        self._logConf = self._mongoConf['logging']
        self._name = self._logConf['name']
        self._logger = logging.getLogger(self._name)
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
        date_str = time.strftime('%Y_%m_%d', time.gmtime ())
        filename = self._logConf['logpath'] + "/crawler_" + date_str + ".log"
        self._logfile_handler = logging.FileHandler (filename)
        self._logfile_handler.setFormatter(formatter)
        self._logger.addHandler(self._logfile_handler)

        #init mongo connection
        self._dbConf = self._mongoConf['mongo']
        self._host = self._dbConf['host']
        self._port = int (self._dbConf['port'])
        self._username = self._dbConf['username']
        self._password = self._dbConf['password']

        self._logger.warn("stockcode crwler started.")

        try:
            self._conn = MongoClient(self._host, self._port)
            if not self._check_connected(self._conn):
                self._logger.error("mongodb connection failed.")
                sys.exit(1)

            # self.connected = self.db.authenticate (self._username, self._password)
            self._db = self._conn.stockinfo

        except Exceptions:
            self._logger.error("mongodb connection failed.")
            # sys.exit (1)

    def __del__(self):
        self._logger.warn("stockcode crwler stopped.")
        self._logger.removeHandler(self._logfile_handler)

    # 检查是否连接成功
    def _check_connected (self, conn):
        return conn.connected

    def getStocks(self):
        stockslist = []
        try:
            stocks = self._db.stocklist.find()
            for stock in stocks:
                stockslist.append([stock['code'] , stock['updatetime']])
            return stockslist
        except Exceptions:
            self._logger.error("mongodb get stocklist error.")











