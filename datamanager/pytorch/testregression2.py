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


num_inputs = 2
num_examples = 1000

true_w = [2, -3.4]
true_b = 4.2

x = torch.randn(num_examples, num_inputs)
y = true_w[0] * x[:, 0] + true_w[1] * x[:, 1] + true_b

y = y + torch.randn(y.size()) * 0.01

dataset = TensorDataset(x, y)
trainloader = DataLoader(dataset, batch_size=256, shuffle=True)

for data, label in trainloader:
    print(data, label)
    break

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc = nn.Linear(2,1)
        print(self.fc.weight)

    def forward(self, x):
        x = self.fc(x)
        return x

net = Net()

criterion = nn.MSELoss()

optimizer = optim.SGD(net.parameters(), lr=0.1)

epochs = 100
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

        # total_loss = total_loss + loss.data[0]
        print type(loss)
    print("Epoch %d, average loss: %f" % (epoch, total_loss/num_examples))


params = list(net.parameters())
print(params[0])
print(params[1])
