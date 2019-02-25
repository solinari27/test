#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: solinari
@file: sklearn_lineregression.py
@time: 2019/02/24
"""
from sklearn import linear_model        #表示，可以调用sklearn中的linear_model模块进行线性回归。
import numpy as np

def get_batch(dataset):
    size = len(dataset)
    x_rand = []
    y_list = []
    for i in range(0, size):
        x_rand.append([i])
        y_list.append([dataset[i]['TCLOSE']])
    return x_rand, y_list

def do_regression(dataset, **kwargs):
    X, y = get_batch(dataset)
    model = linear_model.LinearRegression()
    model.fit(X, y)

    w = model.coef_[0][0]
    b = model.intercept_[0]

    return w, b
