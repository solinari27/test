#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: urlAgent.py 
@time: 2018/02/25 
"""  

import time

class urlAgent():
    """
    give liangyee url
    """

    def __init__(self, *args, **kwargs):
        self._userkey = ''

    def setUseKey(self, key):
        self._userkey = key

    def _getSymbolString(self, stocks):
        symbols = ''
        for stock in stocks:
            if (symbols == ''):
                symbols = str(stock)
            else:
                symbols += ',' + str(stock)
        return symbols

    #params:
    #stock: stock id
    #Day: timestamp of the YY-MM-DD
    def getDailyKUrl(self, stock, startDay, endDay):
        #check params ...
        startDayStr = time.strftime('%Y-%m-%d', startDay)
        endDayStr = time.strftime('%Y-%m-%d', endDay)
        url = r'http://stock.liangyee.com/bus-api/stock/freeStockMarketData/getDailyKBar?userKey=' + self._userkey + r'&startDate=' + startDayStr + r'&symbol=' + str(stock) + '&endDate=' + endDayStr + r'&type=0'
        return url

    def get5MinKUrl(self, stock):
        url = r'http://stock.liangyee.com/bus-api/stock/freeStockMarketData/get5MinK?userKey=' + self._userkey + r'&symbol=' + str(stock) + r'&type=0'
        return url

    def getMarketDataUrl(self, stocks):
        # this stock must be tuples
        symbolist = self._getSymbolString(stocks)
        url = r'http://stock.liangyee.com/bus-api/stock/freeStockMarketData/GetMarketData?userKey=' + self._userkey + r'&symbol='+ symbolist + r'&type=0'
        return url