# -*- coding: utf-8 -*-
# @Author  : Solinari
# @Email   : 
# @File    : lixi.py
# @Software: PyCharm
# @Time    : 2019/04/12

def cal():
    total = 0
    bank = 0.041
    ben = 280

    year = 20
    li = 0.07
    # inc = 1
    inc = 1.04
    kongzhi = 0.8
    consume = 10

    for i in range(0, year):
        total += total*bank + ben*li*kongzhi - consume
        li = li*inc
        consume = consume*inc

    print total
    lixi = total/ben/1.2
    # r = 0.025
    # r = 0.033333333333333333333333
    # r = 0.04
    r = 0.05
    s1 = lixi**r
    print (s1 - 1)*100
    # print consume


cal()

# def con_bank():
#     ben = 450
#     total = ben
#     li = 0.042
#
#     year = 20
#     consume = 10
#     inc = 1.05
#     for i in range(0, year):
#         total += total*li - consume
#         consume = consume*inc
#
#     print total
#     lixi = total/ben
#     # r = 0.025
#     # r = 0.033333333333333333333333
#     # r = 0.04
#     r = 0.05
#     print lixi**r
#
# con_bank()
