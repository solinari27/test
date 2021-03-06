#!usr/bin/env python
# -*- coding:utf-8 _*-

"""
@author: solinari
@file: test.py
@time: 2019/02/10
"""

import sys
import time
import numpy as np

sys.path.append('D:/workspace/test')
# sys.path.append('D:/workspace/stockCrawler')

# sys.path.append('/home/ubuntu/test')
# sys.path.append('/home/solinari/workspace/test')
# sys.path.append('/mnt/d/workspace/test')
# sys.path.append('/home/ubuntu/stockCrawler')
# sys.path.append('/home/solinari/workspace/stockCrawler')
# os.system("export PYTHONPATH=/home/ubuntu/stockCrawler:/home/solinari/workspace/stockCrawler:%PYTHONPATH")
# os.system("export PYTHONPATH=/home/ubuntu/test:/home/solinari/workspace/test:%PYTHONPATH")
# paths = os.getcwd().split('/')
# del(paths[len(paths)-2])
# del(paths[len(paths)-1])
# _path = os.path.join(paths)
# print (_path)

from pytorch.sklearn_lineregression import do_regression
from collection import collection
from collection import data_show
import torch
from torch.autograd import Variable
from torch_learning.tensorboardX_002 import TBwriter



if __name__ == '__main__':
    c = collection.Collection()

    for result in c.getData(code="600059", start_date="2010-01-01", end_date="2018-12-31"):
        ret = do_regression(result, epochs=10000, thres=10,
                            DBSCAN_eps=3, DBSCAN_minsamples=4)
        for item in ret:
            w = item[0]
            b = item[1]
            score = item[4]

            # if line regression cov score < xx; drop this result
            if score < 0.2:
                continue

            dataset = result[item[2]: item[3]]
            print (w, b, score)
            _dt = []
            for _it in dataset:
                _dt.append(_it['TCLOSE'])
            c = TBwriter('D:/workspace/test')
            c.plotline(x_data=np.array(list(range(0, len(_dt)))), y_data=np.array(_dt))

        # show = data_show.Plt()
        # show.load_data(data=dataset)
        # show.plot(w=w, b=b)
        # time.sleep(1)
