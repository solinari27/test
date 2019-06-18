#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: run_test.py
@time: 2018/10/09
"""
import sys
import math
import pandas as pd
import numpy as np
import tushare as ts
import datetime
import matplotlib.pyplot as plt
import stockstats

sys.path.append('/home/ubuntu/stockCrawler')
sys.path.append('/home/solinari/workspace/stockCrawler')

import collection.collection as collection



c = collection.Collection()
alldata = c.getAllData(code="600007", start_date='1990-01-01', end_date='2019-01-01')
# print alldata
datadict = {}
for item in alldata:
    # print item
    # ma 5日均线
    # v_ma 5日量均线

    datekey = item['DATE']
    datadict[datekey] = {
        'open': item['TOPEN'],
        'high': item['HIGH'],
        'close': item['TCLOSE'],
        'low': item['LOW'],
        'volume': item['VOTURNOVER']/100,
        'price_change': item['CHG'],
        'p_change': item['PCHG']
        # 'ma5'：
        # 'ma10':
        # 'ma20':
        # 'v_ma5':
        # 'v_ma10':
        # 'vma_20':
    }

data_df = pd.DataFrame(datadict).T # 如果需要转置，则改为pd.DataFrame(data_dic).T
data_df.fillna(0)
# print data_df


begin_time = '1990-01-01'
end_time = '2019-01-01'
code = "600007"
stock = ts.get_hist_data(code, start=begin_time, end=end_time)
stock = data_df
# print stock, "type:", type(stock)
stock["date"] = stock.index.values  # 增加日期列。
stock = stock.sort_index(0)  # 将数据按照日期排序下。
# print(stock) [186 rows x 14 columns]
# 初始化统计类
# stockStat = stockstats.StockDataFrame.retype(pd.read_csv('002032.csv'))
stockStat = stockstats.StockDataFrame.retype(stock)
# print("init finish .")


# volume delta against previous day
# The Volume Delta (Vol ∆)
# stockStat[['volume', 'volume_delta']].plot(figsize=(20, 10), grid=True)
# print stockStat[['volume', 'volume_delta']]
print stockStat[['close', 'cr', 'cr-ma1', 'cr-ma2', 'cr-ma3']]
# plt.show()
# 交易量的delta转换。交易量是正，volume_delta把跌变成负值。
# stockStat[['close', 'close_delta']].plot(
# subplots=True, figsize=(20, 10), grid=True)
# plt.show()


@classmethod
def _get_kdjk(cls, df, n_days):
    """ Get the K of KDJ
    K ＝ 2/3 × (prev. K) +1/3 × (curr. RSV)
    2/3 and 1/3 are the smooth parameters.
    :param df: data
    :param n_days: calculation range
    :return: None
    """
    rsv_column = 'rsv_{}'.format(n_days)
    k_column = 'kdjk_{}'.format(n_days)
    df[k_column] = list(cls._calc_kd(df.get(rsv_column)))
