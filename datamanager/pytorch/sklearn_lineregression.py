#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: solinari
@file: sklearn_lineregression.py
@time: 2019/02/24
"""
from sklearn import linear_model        #表示，可以调用sklearn中的linear_model模块进行线性回归。
import numpy as np

def get_batch():
    X = [[6], [8], [10], [14], [18]]
    y = [[7], [9], [13], [17.5], [18]]
    return X, y

def do_regression():
    X, y = get_batch()
    model = linear_model.LinearRegression()
    model.fit(X, y)

    w = model.intercept_
    b = model.coef_
    return w, b

print do_regression()
