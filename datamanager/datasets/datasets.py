#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 13:08
# @Author  : Solinari
# @Site    : 
# @File    : datasets.py
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

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
            continue

        rangedatas = datas[clustering[len(clustering) - 1]:p]
        # print(rangedatas)

        X = np.array(list(range(0, len(rangedatas)))).reshape(-1, 1)
        y = np.array(rangedatas).reshape(-1, 1)
        model = linear_model.LinearRegression()
        model.fit(X=X, y=y)

        w = model.coef_[0][0]
        b = model.intercept_[0]
        cov_score = model.score(X, y)
        print (w, b, cov_score)

        # fig = plt.figure()
        # plt.plot(X, y, label=str(cov_score))
        # plt.show()

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