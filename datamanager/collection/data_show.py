#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: test.py
@time: 2019/02/10
"""
import plotly.offline as pyoff
import plotly.graph_objs as go
import numpy as np


class Plt(object):
    def __init__(self):
        pass

    def load_data(self, data):
        self._data = data

    def plot(self):
        date = []
        open = []
        high = []
        low = []
        close = []
        for item in self._data:
            date.append(item['DATE'])
            open.append(item['TOPEN'])
            high.append(item['HIGH'])
            low.append(item['LOW'])
            close.append(item['TCLOSE'])

        trace = go.Ohlc(x=date,
                        open=open,
                        high=high,
                        low=low,
                        close=close,
                        increasing=dict(line=dict(color='red')),
                        decreasing=dict(line=dict(color='green')))
        data = [trace]
        pyoff.plot(data)
