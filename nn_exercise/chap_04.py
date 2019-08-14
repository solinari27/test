# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 22:38
# @Author  : Solinari
# @Email   : deeper1@163.com
# @File    : chap_04.py
# @Software: PyCharm

import torch
import torchvision
import torchvision.transforms as transforms
import torch.nn.functional as F
import torch.optim as optim
from torch import nn
from torch.autograd import Variable


transform = transforms.ToTensor()
BATCH_SIZE = 100

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 定义训练数据集
trainset = torchvision.datasets.MNIST(
    root='./data/',
    train=True,
    download=True,
    transform=transform)

# 定义测试数据集
testset = torchvision.datasets.MNIST(
    root='./data/',
    train=False,
    download=True,
    transform=transform)

# 定义训练批处理数据
trainloader = torch.utils.data.DataLoader(
    trainset,
    batch_size=BATCH_SIZE,
    shuffle=True,
    )

# 定义测试批处理数据
testloader = torch.utils.data.DataLoader(
    testset,
    batch_size=BATCH_SIZE,
    shuffle=False,
    )


