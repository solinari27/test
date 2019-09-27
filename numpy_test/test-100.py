#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 22:05
# @Author  : Solinari
# @Site    : 
# @File    : test-100.py
# @Software: PyCharm


import numpy as np

Z = np.random.random((10,2))
X,Y = np.atleast_2d(Z[:,0], Z[:,1])
D = np.sqrt( (X-X.T)**2 + (Y-Y.T)**2)
print(D)

# Much faster with scipy
import scipy
# Thanks Gavin Heverly-Coulson (#issue 1)
import scipy.spatial

Z = np.random.random((10,2))
D = scipy.spatial.distance.cdist(Z,Z)
print(D)



Z = np.arange(10, dtype=np.float32)
Z = Z.astype(np.int32, copy=False)
print(Z)


X = np.random.rand(5, 10)

# Recent versions of numpy
Y = X - X.mean(axis=1, keepdims=True)

# Older versions of numpy
Y = X - X.mean(axis=1).reshape(-1, 1)

print(Y)

print ('======================================================')

X = np.array([1, 2, 3, 4, 5])
Y = np.array([X, 0, 0, 0])
print (Y)