#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: testregression.py
@time: 2019/02/16
"""
from __future__ import print_function
import math
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from torch.autograd import Variable
from torch.utils.data import TensorDataset, DataLoader

MIN_PRICE = 0
MAX_PRICE = 10000

def get_batch(dataset):
    """Builds a batch i.e. (x, f(x)) pair."""
    size = len(dataset)
    x_rand = []
    y_list = []
    ymin = MAX_PRICE
    ymax = MIN_PRICE
    for i in range(0, size):
        x_rand.append(torch.tensor(i).float())
        y_list.append(dataset[i]['TCLOSE'])
        if ymin > dataset[i]['TCLOSE']:
            ymin = dataset[i]['TCLOSE']
        if ymax < dataset[i]['TCLOSE']:
            ymax = dataset[i]['TCLOSE']
    x_stretch = len(x_rand)
    y_stretch = ymax - ymin
    x_scale = y_stretch / x_stretch
    for i in range(0, size):
        x_rand[i] = x_rand[i] * x_scale
    batch_x = torch.tensor(np.array([x_rand]).T)
    batch_y = torch.tensor(y_list).float()
    return batch_x, batch_y, x_scale


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(1, 1)

    def forward(self, x):
        x = self.fc(x)
        return x


def do_regression(dataset, epochs, **kwargs):
    batch_x, batch_y, x_scale = get_batch(dataset=dataset)
    dataset = TensorDataset(batch_x, batch_y)
    batch_size = list(batch_y.size())[0]
    trainloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    net = Net()
    criterion = nn.MSELoss(reduce=True, size_average=True)
    # criterion = nn.SmoothL1Loss()
    # optimizer = optim.SGD(net.parameters(), lr=0.05)

    for epoch in range(epochs):
        total_loss = 0
        lr = 0.05 / math.log(epoch + 2, 10)
        optimizer = optim.SGD(net.parameters(), lr=lr)
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            data = Variable(inputs)
            label = Variable(labels).float()

            optimizer.zero_grad()
            out = net(data)
            loss = criterion(out, label)
            loss.backward()
            optimizer.step()

            total_loss = total_loss + loss.item()
        print("Epoch %d, total loss: %f" % (epoch, total_loss))

    params = list(net.parameters())
    k = (params[0].item()) * x_scale
    b = (params[1].item())
    return k, b
