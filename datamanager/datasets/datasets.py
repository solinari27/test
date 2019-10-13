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
        datas.append(
            (item['TOPEN'] +
             item['TCLOSE'] +
                item['HIGH'] +
                item['LOW']) /
            4)
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
        print(w, b, cov_score)

        # fig = plt.figure()
        # plt.plot(X, y, label=str(cov_score))
        # plt.show()

        clustering.append(p)


def lineregression_score(datas, head, end):
    """
    cal score of lineregression from dataset head to end
    :param datas:
    :param head:
    :param end:
    :return:
    """
    cov_score = 0
    rangedatas = datas[head: end]
    X = np.array(list(range(0, len(rangedatas)))).reshape(-1, 1)
    y = np.array(rangedatas).reshape(-1, 1)
    model = linear_model.LinearRegression()
    model.fit(X=X, y=y)
    cov_score = model.score(X, y)

    # TODO: consider if should power score of data count
    return cov_score

# two dimension DP(dynamic plan) algo do dataset split
# two status: conjunction disconnect
# judgement： higher line regression coeffeient score
# Dynamic Plan:
# esp1|      esp2       |   esp3        esp4        esp5 ...
#     |↖vs.↑
# esp1|      esp1~esp2  |   esp2~esp3   esp3~esp4   esp4~esp5
#                      ↖vs.↑
# esp1|     esp1~esp2   |   esp1~esp3 or esp1!esp2|esp3
#                              ↓
#                           if esp3 not conjunction with esp1~eps2 this decision makes esp1~esp2 is a absolutely independent dataset series
# DP policy:
# 3 statement:
# 1. disconnection better -> disconnection
# 2. conjunction better && prev elem choices disconnection -> conjunction
# 3. conjunction better && prev elem choices conjunction -> compare prev elem is conjunction with prev elem or conjunction with now elem -> select some conjunction
# 4. conjunction better -> find if prev elem is conjunction with prev elem is better and find on do dicision if should reconjunction?
def dp2way(datas, extreme_points):
    _size = len(extreme_points)
    mat_score = np.zeros((_size, _size))
    mat_policy = np.zeros((_size, _size)).astype(int)

    for i in range(1, _size):
        for j in range(i, _size):
            score_disconnect = lineregression_score(
                datas=datas, head=extreme_points[j - 1], end=extreme_points[j])

            score_conjunction = lineregression_score(
                datas=datas, head=extreme_points[k], end=extreme_points[j])

            # compare score and do choice
            # TODO: score compare


# three dimension DP(dynamic plan) algo do dataset split
# three status: conjunction disconnect noise
# noise score is zero(first idea)
# judgement： higher line regression coeffeient score
def dp3way(datas, extreme_points):
    pass

def gen_datasets(rawdata):
    datas = gen_avprice(rawdata=rawdata)

    # 5 points to select local extreme points
    # .   .    .
    #  . .    . .
    #   .    .   .
    extreme_points = []
    for i in range(2, len(datas) - 2):
        rangelist = datas[i - 2: i + 3]
        if datas[i] == max(rangelist) or datas == min(rangelist):
            extreme_points.append(i)

    ret = dp2way(datas=datas, extreme_points=extreme_points)
