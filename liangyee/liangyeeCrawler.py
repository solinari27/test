#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: liangyeeCrawler.py 
@time: 2018/02/25 
"""  

#TODO: add log!!!
import requests
import json

import urlAgent

class liangyeeCrawler():

    def __init__(self):
        self._agent = urlAgent.urlAgent()
        # self._agent.setUseKey('6F49F56DCE594273BF0B927C8ABE0A12')

    def setID(self, userKey):
        self._agent.setUseKey(userKey)

    def _requestJson(self, url):
        response = requests.get(url=url)
        content = json.loads(response.content)
        return content

    def getDailyKData(self, stock, startDay, endDay):
        url = self._agent.getDailyKUrl(stock, startDay, endDay)
        return self._requestJson(url=url)['result']

    def get5MinKData(self, stock):
        url = self._agent.get5MinKUrl(stock)
        return self._requestJson(url=url)['result']

    def getMarketData(self, stocks):
        url = self._agent.getMarketDataUrl(stocks)
        print url
        return self._requestJson(url=url)['result']





