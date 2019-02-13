#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: solinari
@file: test.py
@time: 2019/02/10
"""
import sys

sys.path.append('/home/ubuntu/test')
sys.path.append('/home/solinari/workspace/test')
# sys.path.append('/home/ubuntu/stockCrawler')
# sys.path.append('/home/solinari/workspace/stockCrawler')
# os.system("export PYTHONPATH=/home/ubuntu/stockCrawler:/home/solinari/workspace/stockCrawler:%PYTHONPATH")
# os.system("export PYTHONPATH=/home/ubuntu/test:/home/solinari/workspace/test:%PYTHONPATH")
# paths = os.getcwd().split('/')
# del(paths[len(paths)-2])
# del(paths[len(paths)-1])
# _path = os.path.join(paths)
# print (_path)

from pytorch.testregression import iter_batch
from collection import collection
from collection import data_show


c = collection.Collection()
# result = c.getData(code="600000", start_date="2017-01-01", end_date="2017-12-31")

for result in c.getData(code="600000", start_date="2017-01-01", end_date="2017-12-31"):
    iter_batch(result)
    show = data_show.Plt()
    show.load_data(data=result)
    show.plot()
