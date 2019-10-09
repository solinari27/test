#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 13:08
# @Author  : Solinari
# @Site    : 
# @File    : datasets.py
# @Software: PyCharm

# use average price do clustering
# TODO: maybe TCLOSE better
def gen_avprice(rawdata):
    datas = []
    for item in rawdata:
        datas.append((item['TOPEN'] + item['TCLOSE'] + item['HIGH'] + item['LOW'])/4)
    return datas


def distance(x, y):
    pass


def clustering_DBSCAN(datas, extreme_points):
    clustering = []
    weights = []
    for p in extreme_points:
        if clustering == []:
            clustering.append(p)

        rangedatas = datas[clustering[len(clustering) - 1]:p]
        print(rangedatas)
        # TODO: rangedatas do sklineregression and do clustering
        clustering.append(p)


def gen_datasets(rawdata):
    datas = gen_avprice(rawdata=rawdata)

    # 5 points to select local extreme points
    # .   .    .
    #  . .    . .
    #   .    .   .
    extreme_points = []
    for i in range(2, len(datas)-2):
        rangelist = datas[i-2: i+3]
        if datas[i] == max(rangelist) or datas == min(rangelist):
            extreme_points.append(i)

    # do clustering
    # points distance with Radian
    ret = clustering_DBSCAN(datas=datas, extreme_points=extreme_points)