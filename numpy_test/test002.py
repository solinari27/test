# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 20:34
# @Author  : Solinari
# @Email   : deeper1@163.com
# @File    : test002.py
# @Software: PyCharm

import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
print (my_array)
print (my_array.shape)
print (my_array[0])
print (my_array[1])


my_new_array = np.zeros((5, 3, 2))
print (my_new_array)

my_random_array = np.random.random((5))
print (my_random_array)


a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
sum = a + b
difference = a - b
product = a * b
quotient = a / b
print ("Sum = \n", sum)
print ("Difference = \n", difference)
print ("Product = \n", product)
print ("Quotient = \n", quotient)


matrix_product = a.dot(b)
print ("Matrix Product = ", matrix_product)



