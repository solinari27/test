#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 9:23
# @Author  : Aries
# @Site    : 
# @File    : test6.py
# @Software: PyCharm

import json

with open("../Data/out.json",'r') as load_f:
    stocks = json.load(load_f)

for item in stocks:
    print item['code'], item['name']
# load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
# print(load_dict)
#
# with open("../config/record.json","w") as dump_f:
#     json.dump(load_dict,dump_f)