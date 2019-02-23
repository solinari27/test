#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: testregression.py
@time: 2019/02/16
"""

from __future__ import print_function
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from torch.autograd import Variable
from torch.utils.data import TensorDataset, DataLoader


# num_inputs = 1
# num_examples = 1000
#
# true_w = [2, -3.4]
# true_b = 4.2
#
# x = torch.randn(num_examples, num_inputs)
# y = true_w[0] * x[:, 0] + true_w[1] * x[:, 0] + true_b
#
# y = y + torch.randn(y.size()) * 0.01
# print (x, x.size())
# print (y, y.size())
#
# dataset = TensorDataset(x, y)
# trainloader = DataLoader(dataset, batch_size=256, shuffle=True)

# for data, label in trainloader:
#     print(data, label)
#     break

def get_batch(dataset):
    """Builds a batch i.e. (x, f(x)) pair."""
    size = len(dataset)
    x_rand = []
    y_list = []
    ymin = 1000
    ymax = 0
    for i in range(0, size):
        x_rand.append(torch.tensor(i).float())
        y_list.append(dataset[i]['TCLOSE'])
        if ymin > dataset[i]['TCLOSE']:
            ymin = dataset[i]['TCLOSE']
        if ymax < dataset[i]['TCLOSE']:
            ymax = dataset[i]['TCLOSE']
    x_stretch = len(x_rand)
    y_stretch = ymax - ymin
    x_scale = y_stretch/x_stretch
    for i in range(0, size):
        x_rand[i] = x_rand[i]*x_scale
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
    optimizer = optim.SGD(net.parameters(), lr=0.05)

    for epoch in range(epochs):
        total_loss = 0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            data = Variable(inputs)
            label = Variable(labels).float()

            optimizer.zero_grad()
            out = net(data)
            loss = criterion(out, label)
            loss.backward()
            optimizer.step()
            print (list(net.parameters())[0], list(net.parameters())[1])

            total_loss = total_loss + loss.item()
        print("Epoch %d, total loss: %f" % (epoch, total_loss))


    params = list(net.parameters())
    k = (params[0].item())*x_scale
    b = (params[1].item())
    return k, b
