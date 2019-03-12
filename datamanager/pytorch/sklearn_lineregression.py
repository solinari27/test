#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: sklearn_lineregression.py
@time: 2019/02/24
"""
import math
from sklearn import linear_model  # 表示，可以调用sklearn中的linear_model模块进行线性回归。
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
from sklearn import preprocessing


def get_batch(dataset):
    size = len(dataset)
    if size < 10:
        return [], []

    x_rand = []
    y_list = []
    for i in range(0, size):
        x_rand.append([i])
        y_list.append([dataset[i]['TCLOSE']])
    return x_rand, y_list


# def valid(dataset, model):
#     X, y = dataset[0], dataset[1]
#     clf = IsolationForest(behaviour='new', max_samples=10,
#                           n_jobs=-1, verbose=2, contamination=0.01)
#
#     diff = model.predict(X) - y
#     _excps = []
#     for _d in diff:
#         _excps.append(_d)
#
#     data_array = []
#     for _i in range(0, len(X)):
#         _x = X[_i][0]
#         _y = y[_i][0]
#         data_array.append([_x, _y])
#     data_array = np.array(data_array)
#     clf.fit(data_array)
#     pred = clf.predict(data_array)
#
#     index_list = []
#     for _i in range(0, len(pred)):
#         if pred[_i] == -1:
#             _diff = math.sqrt(_excps[_i])
#             if y[_i][0]/_diff < 20:
#                 index_list.append([_i, X[_i][0], y[_i][0]])
#
#     return index_list
#
# def split_1(index_list):
#     indexs = []
#     slices = 0
#     indexs.append([index_list[0]])
#     for _i in range(1, len(index_list)):
#         if index_list[_i][0] - indexs[slices][len(indexs[slices])][0] < 3:
#             indexs[slices].append(index_list[_i])
#         else:
#             slices += 1
#             indexs.append([index_list[_i]])
#
#     return indexs

def check_results(datasets, model, thres, DBSCAN_eps, DBSCAN_minsamples):
    X, y = datasets[0], datasets[1]
    diff = model.predict(X) - y
    far_x = []
    fars = []
    for _i in range(0, len(diff)):
        _diff = math.fabs(diff[_i][0])
        if (_diff > 0):
            if (y[_i][0] / _diff) < thres:
                far_x.append([X[_i][0]])
                fars.append(_diff)

    ret = [[]]
    ret = []
    res = [[]]
    if len(far_x) > 0:
        fars_scale = np.array(far_x)
        y_pred = DBSCAN(
            eps=DBSCAN_eps, min_samples=DBSCAN_minsamples).fit_predict(fars_scale)

        for _i, pred in enumerate(y_pred):
            if pred >= 0:
                if pred > len(ret) - 1:
                    ret.append([far_x[_i][0]])
                    res.append([fars[_i]])
                else:
                    ret[pred].append(far_x[_i][0])
                    res[pred].append(fars[_i])

        for _i, group in enumerate(ret):
            _y = 0
            k = -1
            for _j, y in enumerate(group):
                if y > _y:
                    k = _j
                    _y = y
            ret[_i] = k
    return ret


def do_regression(dataset, **kwargs):
    """
    return a list of regression results:
    [(w0, b0, x0_0, x0_max), (w1, b1, x1_0, x1_max), ...]
    """
    ret = []

    X, y = get_batch(dataset)
    if X != [] and y != []:
        model = linear_model.LinearRegression()
        model.fit(X, y)

        w = model.coef_[0][0]
        b = model.intercept_[0]
        far_points = check_results(
            [X, y], model, kwargs['thres'], kwargs['DBSCAN_eps'], kwargs['DBSCAN_minsamples'])

        if far_points == []:
            ret.append([w, b, 0, len(dataset)])
        else:
            x0 = 0
            far_points.append(len(dataset) - 1)
            for x1 in far_points:
                res = do_regression(
                    dataset[x0:x1], epochs=10000, thres=10, DBSCAN_eps=3, DBSCAN_minsamples=4)
                for item in res:
                    item[2] += x0
                    item[3] += x0
                    ret.append(item)
                x0 = x1

    return ret
