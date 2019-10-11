#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 13:08
# @Author  : Solinari
# @Site    : 
# @File    : datasets.py
# @Software: PyCharm

import numpy as np


# use average price do clustering
# TODO: maybe TCLOSE better
def gen_avprice(rawdata):
    datas = []
    for item in rawdata:
        datas.append((item['TOPEN'] + item['TCLOSE'] + item['HIGH'] + item['LOW'])/4)
    return datas


# APclustering  algo
# not use
def clustering(datas, extreme_points):
    clustering = []
    weights = []
    for p in extreme_points:
        if clustering == []:
            clustering.append(p)

        rangedatas = datas[clustering[len(clustering) - 1]:p]
        print(rangedatas)
        # TODO: rangedatas do sklineregression and do clustering
        clustering.append(p)


# two dimension DP(dynamic plan) algo do dataset split
# judgement： higher line regression coeffeient score
def dp2way(datas, extreme_points):
    _size = len(extreme_points)
    mat_score = np.zeros((_size, _size))
    mat_policy = np.zeros((_size, _size)).astype(int)
    for i in range(1, _size):
        for j in range(1, _size):
            print (mat_score[i, j])


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
    # ret = clustering(datas=datas, extreme_points=extreme_points)
    ret = dp2way(datas=datas, extreme_points=extreme_points)