#!usr/bin/env python
# -*- coding:utf-8 _*-

"""
@author: solinari
@file: test.py
@time: 2019/02/10
"""

import sys
import time

sys.path.append('/home/ubuntu/test')
sys.path.append('/home/solinari/workspace/test')
sys.path.append('/mnt/d/workspace/test')
# sys.path.append('/home/ubuntu/stockCrawler')
# sys.path.append('/home/solinari/workspace/stockCrawler')
# os.system("export PYTHONPATH=/home/ubuntu/stockCrawler:/home/solinari/workspace/stockCrawler:%PYTHONPATH")
# os.system("export PYTHONPATH=/home/ubuntu/test:/home/solinari/workspace/test:%PYTHONPATH")
# paths = os.getcwd().split('/')
# del(paths[len(paths)-2])
# del(paths[len(paths)-1])
# _path = os.path.join(paths)f
# print (_path)

from pytorch.sklearn_lineregression import do_regression
from collection import collection
from collection import data_show


c = collection.Collection()

for result in c.getData(code="600000", start_date="2010-01-01", end_date="2018-12-31"):
    ret = do_regression(result, epochs=10000, thres=10,
                        DBSCAN_eps=3, DBSCAN_minsamples=4)
    for item in ret:
        w = item[0]
        b = item[1]
        dataset = result[item[2]: item[3]]
        if w>0.1 or w<-0.1:
            print (w, b)
            for line in result:
                pass
                # print (line['DATE'], line['TCLOSE'])
    #     print (dataset)
    # show = data_show.Plt()
    # show.load_data(data=dataset)
    #show.plot(w=w, b=b)
    # time.sleep(1)
