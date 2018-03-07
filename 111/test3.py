# -*- coding:utf-8 -*-

import requests
import urllib2
import json
import pandas as pd
import numpy as np

###定义取数据函数
def get_raw_data(x):
    # return json.loads(urllib.request.urlopen(x).read())['result']
    return json.loads(requests.get(url=x).read())['result']

####提取案例数据网址
#5分钟
url = r'http://stock.liangyee.com/bus-api/stock/freeStockMarketData/get5MinK?userKey=6F49F56DCE594273BF0B927C8ABE0A12&symbol=600100&type=0'

#日线
url = r'http://stock.liangyee.com/bus-api/stock/freeStockMarketData/getDailyKBar?userKey=6F49F56DCE594273BF0B927C8ABE0A12&startDate=2016-01-01&symbol=600300&endDate=2016-02-20&type=0'

#分时
url = r'http://stock.liangyee.com/bus-api/stock/freeStockMarketData/GetMarketData?userKey=6F49F56DCE594273BF0B927C8ABE0A12&symbol=600000,600300&type=0'

response = requests.get(url=url)
r = response.content
content = json.loads(r)
print content['result']

# ###提取数据
# data_day = get_raw_data(url)
#
# ###转换可数据分析的dataframe格式
# #定义转换dataframe函数
# all_colnames = ['code','open','high','low','close','volume','amount','avp','openvolume','closevolume','opentime','closetime','date']
# def to_dataframe(x):
#     df = pd.DataFrame(columns = all_colnames)
#     for s in x:
#         l = len(df)
#         df.loc[l,:] = s.split(',')
#     for f in['open','high','low','close','volume','amount','avp','openvolume','closevolume']:
#         df[f][df[f] == ''] = 0
#         df[f] = df[f].astype(float).fillna(0.0)
#     df = df[all_colnames]
#     return df
#
# #数据转换
# df_day = to_dataframe(data_day)
#
# print df_day