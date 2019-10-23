#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 13:08
# @Author  : Solinari
# @Site    :
# @File    : datasets.py
# @Software: PyCharm

import math
import matplotlib.pyplot as plt
import numpy as np
from math import degrees, radians, tan, atan
from sklearn import linear_model
from sklearn.cluster import AffinityPropagation
from sklearn.metrics import explained_variance_score


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


def regressdistance():
    """
    cal regression distance
    """
    pass

# clustering based on AffinityPropergation
# recompute extreme points distance by remapping to R^n space


def clustering(datas, extreme_points):
    """
    use clustering algorithm do dataset clustering
    clustering metrics: weight / cov_score
    weight: cal regression weight(line angle)
    cov_score: cal regression fit precision
    """
    def gen_dataset_smallcluster():
        elems = []
        totallen = len(extreme_points)
        for i in range(1, totallen):
            dataset = datas[extreme_points[i - 1]:extreme_points[i]]
            if len(dataset) > 2:
                X = np.array(list(range(0, len(dataset)))).reshape(-1, 1)
                y = np.array(dataset).reshape(-1, 1)
                model = linear_model.LinearRegression()
                model.fit(X=X, y=y)

                w = model.coef_[0][0]
                b = model.intercept_[0]
                cov_score = model.score(X, y)
                elems.append({'head': extreme_points[i - 1],
                              'end': extreme_points[i],
                              'weight': w,
                              'bias': b,
                              'score': cov_score})
            else:
                pass

        return elems

    def rank(i, j):
        """
        rank func:
        -ln(tan(角度差))*拟合度评分系数
        :param i:
        :param j:
        :return:
        """
        elem_i = small_clusters[i]
        elem_j = small_clusters[j]
        head = min(elem_i['head'], elem_j['head'])
        end = max(elem_i['head'], elem_j['end'])
        localdataset = datas[head:end]
        fitdataset = datas[elem_j['head']: elem_j['end']]

        X = np.array(list(range(0, len(localdataset)))).reshape(-1, 1)
        y = np.array(localdataset).reshape(-1, 1)
        _X = np.array(list(range(len(localdataset) -
                                 len(fitdataset), len(localdataset)))).reshape(-1, 1)
        _y = np.array(fitdataset).reshape(-1, 1)
        model = linear_model.LinearRegression()
        model.fit(X=X, y=y)

        w = model.coef_[0][0]
        b = model.intercept_[0]
        # _y_pred = model.predict(_X)
        # fit_score = explained_variance_score(_y, _y_pred)
        fit_score = model.score(_X, _y)

        fit_w = elem_j['weight']
        localangle = degrees(atan(w))
        fitangle = degrees(atan(fit_w))
        diffangle = radians(math.fabs(fitangle - localangle))
        weightrank = -math.log(tan(diffangle))
        fitrank = atan(fit_score - 1)

        # print(weightrank, fitrank)
        # plt.title("Matplotlib demo")
        # plt.xlabel("x axis caption")
        # plt.ylabel("y axis caption")
        # plty = w*X+b
        # plt.plot(X, plty)
        # plt.scatter(_X, _y, edgecolors='yellow')
        # print (X, _X)
        # plt.show()

        return weightrank * fitrank

    small_clusters = gen_dataset_smallcluster()
    # do AP clustering on small_clusters
    counts = len(small_clusters)
    mats = np.zeros((counts, counts))
    # mats for s(i,j) in APclustering
    # -1000     0.1        0.2     0.5
    # -1000     -1000      0.3     0.2
    # -1000     -1000    -1000     0.6
    # -1000     -1000    -1000    -1000
    for i in range(0, counts):
        for j in range(0, counts):
            # use -1000 present -inf
            mats[i, j] = -1000

    for i in range(0, counts):
        mats[i, i] = 0
        for j in range(i + 1, counts):
            mats[i, j] = rank(i=i, j=j)

    af = AffinityPropagation(affinity='precomputed').fit(mats)
    cluster_centers_indices = af.cluster_centers_indices_
    labels = af.labels_
    print (cluster_centers_indices)
    print (labels)

    # cal matrics of distance not euclidean
#     Y = np.array([[0, 1, 2],
#                   [1, 0, 3],
#                   [2, 3, 0]]) # 相似度矩阵,距离越小代表两个向量距离越近
#     # N = Y.shape[0]
#     db = DBSCAN(eps=0.13, metric='precomputed', min_samples=3).fit(Y)
#     labels = db.labels_
#     # 然后来看一下分类的结果吧!
#     n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0) # 类的数目
#     print('类的数目是:%d'%(n_clusters_))

#     clustering = []
#     weights = []
#     for p in extreme_points:
#         if clustering == []:
#             clustering.append(p)
#             continue

#         rangedatas = datas[clustering[len(clustering) - 1]:p]
#         # print(rangedatas)

#         X = np.array(list(range(0, len(rangedatas)))).reshape(-1, 1)
#         y = np.array(rangedatas).reshape(-1, 1)
#         model = linear_model.LinearRegression()
#         model.fit(X=X, y=y)

#         w = model.coef_[0][0]
#         b = model.intercept_[0]
#         cov_score = model.score(X, y)
#         print(w, b, cov_score)

#         # fig = plt.figure()
#         # plt.plot(X, y, label=str(cov_score))
#         # plt.show()

#         clustering.append(p)


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
# 4. conjunction better -> find if prev elem is conjunction with prev elem
# is better and find on do dicision if should reconjunction?


def dp2way(datas, extreme_points):
    _size = len(extreme_points)
    mat_score = np.zeros((_size, _size))
    mat_policy = np.zeros((_size, _size)).astype(int)

    for i in range(1, _size):
        for j in range(i, _size):
            pass
#             score_disconnect = lineregression_score(
# datas=datas, head=extreme_points[j - 1], end=extreme_points[j])

#             score_conjunction = lineregression_score(
#                 datas=datas, head=extreme_points[k], end=extreme_points[j])

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

    ret = clustering(datas=datas, extreme_points=extreme_points)
