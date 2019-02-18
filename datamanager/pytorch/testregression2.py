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
    for i in range(0, size):
        x_rand.append(torch.tensor(i).float())
        y_list.append(dataset[i]['TCLOSE'])
    # npx = np.array(x_rand)
    # npy = np.array(y_list)
    # npx.reshape(94, 1, 1)
    # npy.reshape(94, 1)
    # batch_x = torch.tensor(npx).float()
    # batch_y = torch.tensor(npy).float()
    batch_x = torch.tensor(np.array([x_rand]).T)
    batch_y = torch.tensor(y_list).float()
    return batch_x, batch_y

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(1, 1)
        # print(self.fc.weight)

    def forward(self, x):
        x = self.fc(x)
        return x

def do_regression(dataset, epochs, **kwargs):
    batch_x, batch_y = get_batch(dataset=dataset)
    print (batch_x, batch_x.size())
    print (batch_y, batch_y.size())
    dataset = TensorDataset(batch_x, batch_y)
    trainloader = DataLoader(dataset, batch_size=32, shuffle=True)
    net = Net()
    criterion = nn.MSELoss()
    optimizer = optim.SGD(net.parameters(), lr=0.1)

    for epoch in range(epochs):
        total_loss = 0
        for i, data in enumerate(trainloader, 0):
            inputs, labels = data
            data = Variable(inputs)
            label = Variable(labels).float()
            print ("data", data)
            print ("label", label)

            optimizer.zero_grad()
            out = net(data)
            print ("out", out)
            loss = criterion(out, label)
            loss.backward()
            optimizer.step()

            total_loss = total_loss + loss.item()
        print("Epoch %d, average loss: %f" % (epoch, total_loss/32))


    params = list(net.parameters())
    print (params)
    # k = params[0]
    # b = params[1]
    # print(params[0])
    # print(params[1])
    # return k, b
