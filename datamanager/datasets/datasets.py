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


def clustering(datas, extreme_points):
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


def lineregression_score(datas, head, end):
    return 0


# two dimension DP(dynamic plan) algo do dataset split
# judgement： higher line regression coeffeient score
def dp2way(datas, extreme_points):
    _size = len(extreme_points)
    mat_score = np.zeros((_size, _size))
    mat_policy = np.zeros((_size, _size)).astype(int)

    for i in range(1, _size):
        for j in range(i, _size):
            # conjuction from left elem head is the non-zero most left elem
            # the score_conjuction is the lineregression score from head to elem
            k = j-1
            while mat_score[i, k]>0:
                k -= 1
            # cal score from elem_k to elem_j
            score_conjunction = lineregression_score(datas=datas, head=extreme_points[k], end=extreme_points[j])

            # disconnect from this elem and from upper elem
            score_disconnect = lineregression_score(datas=datas, head=extreme_points[j-1], end=extreme_points[j])

            # compare score and do choice
            # TODO: score compare

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