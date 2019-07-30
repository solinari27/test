# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 22:07
# @Author  : Solinari
# @Email   : deeper1@163.com
# @File    : chap_01.py
# @Software: PyCharm

import numpy as np

a = np.array([4, 5, 6])
print (a.dtype)
print (a.shape)
print (a[0])

b = np.array([[4, 5, 6], [1, 2, 3]])
print (b.shape)
print (b[0, 0], b[0, 1], b[1, 1])

a = np.zeros([3, 3], dtype=int)
b = np.ones([4, 5], dtype=int)
d = np.random.random([3, 2])
print (a)
print (b)
print (d)

a=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print (a)
print (a[2, 3])
print (a[0, 0])

# 6
b = a[0:2,2:4]
print (b)
print (b[0, 0])

# 7
c = a[1:3][:]
print (c)
print (c[0][-1])

#8
a=np.array([[1, 2], [3, 4], [5, 6]])
print (a[[0, 1, 2],[0, 1, 0]])

#9
a=np.mat([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
b=np.array[0, 2, 0, 1]
print (a[np.arrange(4), b])

#10
c = a[np.arrange(4), b]
c +=10
print (c)