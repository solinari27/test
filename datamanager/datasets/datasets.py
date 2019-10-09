#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 13:08
# @Author  : Solinari
# @Site    : 
# @File    : datasets.py
# @Software: PyCharm

def gen_avprice(rawdata):
    datas = []
    for item in rawdata:
        datas.append((item['TOPEN'] + item['TCLOSE'] + item['HIGH'] + item['LOW'])/4)
    return datas


def if_extreme_point(data_list):
    pass

def gen_datasets(rawdata):
    datas = gen_avprice(rawdata=rawdata)

    ret = []
    for i in range(2, len(datas)-2):
        rangelist = datas[i-2: i+3]
        if datas[i] == max(rangelist) or datas == min(rangelist):
            ret.append(i)
    return ret

    # p_start = 0
    # p_end = len(rawdata)
    # for i in range(p_start, p_end):
    #     print (rawdata[i])