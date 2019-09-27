#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   tensorboardX_002.py
@Time    :   2019/09/20 19:50:58
@Author  :   Solinari
@Contact :   deeper1@163.com
@License :   (C)Copyright 2017-2018, GPLv3
"""

# here put the import lib
import os
import torch
import yaml
import matplotlib.pyplot as plt
from uuid import uuid4
from tensorboardX import SummaryWriter


class TBwriter():

    def __init__(self, homepath):
        self.homepath = homepath
        self.conf = dict()
        with open(homepath + '/Conf/tensorboard.yaml') as f:
            self.conf = yaml.safe_load(f)

    def plotline(self, x_data, y_data, label=None):
        # non-interactive matplotlib backend 'svg' 'agg' for png image svg for svg image
        plt.switch_backend('svg')
        fig = plt.figure()

        plt.plot(x_data, y_data, label=label)

        # output to tensorboard
        self.__writeResult(fig=fig)

    def plotscatter(self):
        pass
    
    def plotbar(self):
        pass
    
    def plotstock(self, stock_data, label=None):
        pass

    def __writeResult(self, fig, output_type='img'):
        writer = SummaryWriter(self.conf[output_type])
        writer.add_figure(tag='plot_' + str(uuid4()), figure=fig)
        writer.close()




