#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/9 12:54
# @Author  : Solinari
# @Site    : 
# @File    : trigger.py
# @Software: PyCharm

from datamanager.collection import collection
from datamanager.datasets.datasets import gen_datasets

start_date = "2010-01-01"
end_date = "2019-12-31"
c = collection.Collection()
code = "600000"

for result in c.getData(code=code, start_date=start_date, end_date=end_date):
    # print (result)
    ret_cluster = gen_datasets(rawdata=result)