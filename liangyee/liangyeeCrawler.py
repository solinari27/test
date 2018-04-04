#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: liangyeeCrawler.py 
@time: 2018/02/25 
"""  

import requests
import json
import logging
import time

import urlAgent
import mongoConn

class liangyeeCrawler():

    def __init__(self):
        with open('Conf/liangyee.conf') as f:
            self._liangyeeConf = json.load(f)

        # init logging:
        self._logConf = self._liangyeeConf['logging']
        self._name = self._logConf['name']
        self._logger = logging.getLogger(self._name)
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
        date_str = time.strftime('%Y_%m_%d', time.gmtime())
        filename = self._logConf['logpath'] + "/crawler_" + date_str + ".log"
        self._logfile_handler = logging.FileHandler(filename)
        self._logfile_handler.setFormatter(formatter)
        self._logger.addHandler(self._logfile_handler)

        self._logger.warn("liangyee crwler started.")

        #init other：
        self._conf = self._liangyeeConf['crawler']
        self._timeLimit = self._conf['timelimit']
        self._repeatTime = self._conf['requestrepeat']
        self._agent = urlAgent.urlAgent()
        # userkey = '6F49F56DCE594273BF0B927C8ABE0A12'
        # self._agent.setUseKey(userkey)
        # self._logger.debug("liangyee crwler set userkey: " + userkey + " .")
        # self._agent.setTimesLimit(200)
        # self._logger.debug("liangyee crwler set time limit: " + 200 + " .")

        self._conn = mongoConn.mongoConn()
        self._logger.debug("liangyee crwler init mongo connection.")

        self._setID(self._getNextID())

    def __del__(self):
        self._logger.warn("liangyee crwler stopped.")
        self._logger.removeHandler(self._logfile_handler)

    def _setID(self, userKey):
        self._agent.setUserKey(userKey)
        self._logger.debug("liangyee crwler set userkey: " + userKey + " .")
        self._agent.setTimesLimit(self._timeLimit)
        self._logger.debug("liangyee crwler set time limit: " + str(self._timeLimit) + " .")

    def _getNextID(self):
        #TODO 检查ID update 时间
        return '6F49F56DCE594273BF0B927C8ABE0A12'

    def _requestJson(self, url):
        for i in range (self._repeatTime):
            try:
                response = requests.get(url=url)
                content = json.loads(response.content)
                return content
            except requests.exceptions.ConnectionError:
                self._logger.error("liangyee crwler request url " + url + " connection error.")
            except requests.exceptions.ChunkedEncodingError:
                self._logger.error("liangyee crwler request url " + url + " chunked encoding error.")
            except:
                self._logger.error("liangyee crwler request url " + url + " other error.")
        return {}

    def _getstockslist(self):
        return self._conn.getStocks()

    def getDailyKData(self, stock, startDay, endDay):
        url = self._agent.getDailyKUrl(stock, startDay, endDay)
        if url != "":
            return self._requestJson(url=url)['result']
        else:
            self._setID(self._getNextID())
            return self.getDailyKData(stock, startDay, endDay)

    def get5MinKData(self, stock):
        url = self._agent.get5MinKUrl(stock)
        return self._requestJson(url=url)['result']

    def getMarketData(self, stocks):
        url = self._agent.getMarketDataUrl(stocks)
        return self._requestJson(url=url)['result']

    def crawlliangyee(self):
        stockcodelist = self._getstockslist()
        for code in stockcodelist:
            # 0 for stockcode 1 for updatetime
            print code
            if code[1] == None:
                lastDate = time.strptime("2000:01:01", "%Y:%m:%d")
            else:
                lastDate = code[1]
            now = time.gmtime()
            nowDate = time.strptime(str(now.tm_year) + ":" + str(now.tm_mon) + ":" + str(now.tm_mday), "%Y:%m:%d")
            # self.getDailyKData(code[0], lastDate, nowDate)

        #debuginfo
        print self.getDailyKData(code[0], lastDate, nowDate)




