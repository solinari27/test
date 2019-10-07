#!usr/bin/env python
# -*- coding:utf-8 _*-

"""
@author: solinari
@file: test.py
@time: 2019/02/10
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from uuid import uuid4
import yaml
import json
import pickle
import time

import mlflow
from mlflow import log_metric, log_param, log_artifact
from pytorch.sklearn_lineregression import do_regression
from datamanager.collection import collection
from datamanager.collection import data_show
import torch
from torch.autograd import Variable
from torch_learning.tensorboardX_002 import TBwriter
from common.mongo.neteaseConn import NeteaseConn


def contrun_findit():
    runs = mlflow.search_runs()
    count = len(runs)

    for _index in range(0, count):
        if not runs.iloc[_index]['metrics.finished']:
            return runs.iloc[_index]['run_id']

    return None

def load_last_run(conf):
    """
    load last mlflow dataset run info
    """
    if not conf['dataset']['continue']:
        return None, []
    
    run_id = (contrun_findit())
    mlflow.end_run()
    mlflow.start_run(run_id=run_id)
    uri_base = mlflow.get_artifact_uri()
    try:
        filename = os.path.join(uri_base, 'datainfo')
        with open(filename, 'rb') as f:
            datainfo = pickle.load(f)
    except:
        datainfo = []

    return run_id, datainfo
    
    
def mlflow_log_params(conf):
    log_param('start_date', conf['main']['start_date'])
    log_param('end_date', conf['main']['end_date'])
    log_param('thres', conf['collection']['thres'])
    log_param('DBSCAN_eps', conf['collection']['sk_learn']['DBSCAN_eps'])
    log_param('DBSCAN_minsamples', conf['collection']['sk_learn']['DBSCAN_minsamples'])
    

def getStockList():
    client = NeteaseConn('D:/workspace/testproj/Conf/netease.conf')
    return client.getStocks()

def gen_plotdata(dataset):
    plotdata = []
    for item in dataset:
        plotdata.append([item[1], item[2], item[3], item[4]])
    return plotdata

def gen_training_data(code, conf):
    def gen_filename():
        filehead = str(code) + '_'
        return filehead + str(uuid4())

    def gen_storage_data(rawdata, regression_res):
        dataset = []
        dataset_info = {}

        w = regression_res[0]
        b = regression_res[1]
        score = regression_res[4]
        dataset_info['code'] = code
        dataset_info['regression_w'] = w
        dataset_info['regression_b'] = b
        dataset_info['regression_score'] = score

        for _i in rawdata:
            item = []
            item.append(_i['LCLOSE'])
            item.append(_i['TOPEN'])
            item.append(_i['TCLOSE'])
            item.append(_i['HIGH'])
            item.append(_i['LOW'])
            item.append(_i['TCAP'])
            item.append(_i['MCAP'])
            item.append(_i['CHG'])
            item.append(_i['PCHG'])
            item.append(_i['VATURNOVER'])
            item.append(_i['VOTURNOVER'])
            item.append(_i['TURNOVER'])
            dataset.append(item)
        return dataset, dataset_info

    start_date = conf['main']['start_date']
    end_date = conf['main']['end_date']
    c = collection.Collection()

    for result in c.getData(code=code, start_date=start_date, end_date=end_date):
        ret = do_regression(result,
                            epochs=conf['collection']['epochs'],
                            thres=conf['collection']['thres'],
                            DBSCAN_eps=conf['collection']['sk_learn']['DBSCAN_eps'],
                            DBSCAN_minsamples=conf['collection']['sk_learn']['DBSCAN_minsamples'])
        for item in ret:
            # if line regression cov score < xx; drop this result
            if item[4] < 0.2 or abs(item[0]) < 0.01:
                continue
            dataset, dataset_info = gen_storage_data(
                rawdata=result[item[2]: item[3]], regression_res=item)

            fig = plt.figure()
            plotdataset = gen_plotdata(dataset=dataset)
            plt.plot(np.array(list(range(0, len(plotdataset)))),
                     np.array(plotdataset), label='label')
            
            data = pd.DataFrame(np.array(dataset))
            filehead = gen_filename()
            
            dataset_info['filehead'] = filehead
            datainfo.append(dataset_info)
            
            count = len(datainfo)
            jd = json.dumps(dataset_info)
            with open(filehead + '.json', 'w') as f:
                f.write(jd)
            data.to_csv(filehead + '.csv')
            plt.savefig(filehead + '.png')
            log_artifact(filehead + '.json')
            log_artifact(filehead + '.csv')
            log_artifact(filehead + '.png')
            log_metric('dataset', count)
            os.remove(filehead + '.json')
            os.remove(filehead + '.csv')
            os.remove(filehead + '.png')
            

if __name__ == '__main__':
    with open('D:/workspace/testproj/Conf/mlflow.yaml') as f:
        mlflow_conf = yaml.safe_load(f)
    mlflow.set_tracking_uri(mlflow_conf['uri'])
    mlflow.set_experiment(mlflow_conf['experiment'])
    
    mlflow_runid, datainfo = (load_last_run(conf=mlflow_conf))
    if mlflow_runid is None:
#         mlflow.start_run()
#         mlflow_runid = mlflow.active_run()
        # not finished until all code generated
        log_metric('finished', False)
        codeslist = getStockList()
        codes = []
        for item in codeslist:
            codes.append(item[0])

    else:
        codeslist = getStockList()
        codes = []
        for item in codeslist:
            codes.append(item[0])
        codes_set = set(codes)
        for dataitem in datainfo:
            codes_set.discard(dataitem['code'])
        codes = list(codes_set)

    for code in codes:
        with open('D:/workspace/testproj/Conf/datamanager.yaml') as f:
            conf = yaml.safe_load(f)

        mlflow_log_params(conf=conf)

        gen_training_data(code=code, conf=conf)
        with open('datainfo', 'wb') as f:
            pickle.dump(datainfo, f)
        log_artifact('datainfo')
        os.remove('datainfo')

    log_metric('finished', True)
    mlflow.end_run()


