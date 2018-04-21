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
import random
import mongoConn

import urlAgent

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
        self._debug = self._conf['debug']
        self._repeatTime = self._conf['requestrepeat']
        self._agent = urlAgent.urlAgent()
        # userkey = '6F49F56DCE594273BF0B927C8ABE0A12'
        # self._agent.setUseKey(userkey)
        # self._logger.debug("liangyee crwler set userkey: " + userkey + " .")
        # self._agent.setTimesLimit(200)
        # self._logger.debug("liangyee crwler set time limit: " + 200 + " .")

        self._conn = mongoConn.mongoConn()
        self._logger.debug("liangyee crawler init mongo connection.")

        key, timelimit = self._getNextID()
        self._setID(key, timelimit)

    def __del__(self):
        self._logger.warn("liangyee crawler stopped.")
        self._logger.removeHandler(self._logfile_handler)

    def _setID(self, userKey, timelimit):
        self._agent.setUserKey(userKey)
        self._logger.debug("liangyee crawler set userkey: " + userKey + " .")
        self._agent.setTimesLimit(timelimit)
        self._logger.debug("liangyee crawler set time limit: " + str(timelimit) + " .")

    def _getNextID(self):
        return self._conn.getUserID(self._agent.getUserKey(), self._agent.getTimes(), self._debug)
        # return '6F49F56DCE594273BF0B927C8ABE0A12'

    def _requestJson(self, url):
        for i in range (self._repeatTime):
            try:
                response = requests.get(url=url)
                content = json.loads(response.content)
                return content
            except requests.exceptions.ConnectionError:
                self._logger.error("liangyee crawler request url " + url + " connection error.")
            except requests.exceptions.ChunkedEncodingError:
                self._logger.error("liangyee crawler request url " + url + " chunked encoding error.")
            except:
                self._logger.error("liangyee crawler request url " + url + " other error.")
        return {}

    def _getstockslist(self):
        return self._conn.getStocks()

    def _updateDataTime(self, code, date):
        self._conn.updateTime(code, date)

    def getDailyKData(self, stock, startDay, endDay):
        url = self._agent.getDailyKUrl(stock, startDay, endDay)
        if url != "":
            return self._requestJson(url=url)['result']
        else:
            userKey, timelimit = self._getNextID()
            if (userKey != None):
                self._setID(userKey, timelimit)
                return self.getDailyKData(stock, startDay, endDay)
            else:
                return None

    def get5MinKData(self, stock):
        url = self._agent.get5MinKUrl(stock)
        if url != "":
            return self._requestJson(url=url)['result']
        else:
            userKey, timelimit = self._getNextID()
            if (userKey != None):
                self._setID(userKey, timelimit)
                return self.get5MinKData(stock)
            else:
                return None

    def getMarketData(self, stocks):
        url = self._agent.getMarketDataUrl(stocks)
        if url != "":
            return self._requestJson(url=url)['result']
        else:
            userKey, timelimit = self._getNextID()
            if (userKey != None):
                self._setID(userKey, timelimit)
                return self.getMarketData(stocks)
            else:
                return None

    def crawlliangyee(self):
        def date_cmp(date1, date2):
            if ((date1.tm_year == date2.tm_year) and (date1.tm_mon == date2.tm_mon) and (date1.tm_mday == date2.tm_mday)):
                return True
            else:
                return False

        stockcodelist = self._getstockslist()
        for code in stockcodelist:
            # 0 for stockcode 1 for updatetime
            if code[1] == None:
                lastDate = time.strptime("2000:01:01", "%Y:%m:%d")
            else:
                time_local = time.localtime(code[1])
                lastDate = time_local
            now = time.gmtime()
            nowDate = time.strptime(str(now.tm_year) + ":" + str(now.tm_mon) + ":" + str(now.tm_mday), "%Y:%m:%d")
            if not date_cmp(nowDate, lastDate):
                try:
                    kData = self.getDailyKData(code[0], lastDate, nowDate)
                    time.sleep(random.randint(1, 5))
                    fiveMinData = self.get5MinKData(code[0])
                    time.sleep(random.randint(1, 5))
                    marketData = self.getMarketData([code[0]])
                    # print kData
                    # print fiveMinData
                    # print marketData
                    #TODO update database
                    self._updateDataTime(code[0], nowDate)
                except Exception:
                    continue
                time.sleep(10)

        #debuginfo
        # print self.getDailyKData(code[0], lastDate, nowDate)
        # time.sleep(3)
        # print self.get5MinKData(code[0])
        # time.sleep(3)
        # print self.getMarketData([code[0]])




