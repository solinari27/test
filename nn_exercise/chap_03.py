# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 20:43
# @Author  : Solinari
# @Email   : deeper1@163.com
# @File    : chap_03.py
# @Software: PyCharm
"""
实现一个全连接(full connection)网络
"""


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


# for item in trainloader:
# #     for yuansu in item:
# #         # print (yuansu.size())
# #         pass


class simpleNet(nn.Module):
    """
    定义了一个简单的三层全连接神经网络，每一层都是线性的
    """

    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(784, 520)
        self.l2 = nn.Linear(520, 320)
        self.l3 = nn.Linear(320, 240)
        self.l4 = nn.Linear(240, 120)
        self.l5 = nn.Linear(120, 10)

    def forward(self, x):
        x = x.view(-1, 784)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        return F.log_softmax(self.l5(x), dim=1)


if __name__ == '__main__':
    model = simpleNet()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)

    for batch_idx, (data, target) in enumerate(trainloader):
        data, target = Variable(data), Variable(target)

        optimizer.zero_grad()
        output = model(data)
        # print (output)
        # print (target)

        # loss
        # loss = F.nll_loss(output, target)
        loss = F.cross_entropy(output, target)
        loss.backward()
        # update
        optimizer.step()
        if batch_idx % 100 == 0:
            print('Train Epoch.')








# # 定义网络结构
# class LeNet(nn.Module):
#     def __init__(self):
#         super(LeNet, self).__init__()
#         self.conv1 = nn.Sequential(     #input_size=(1*28*28)
#             nn.Conv2d(1, 6, 5, 1, 2), #padding=2保证输入输出尺寸相同
#             nn.ReLU(),      #input_size=(6*28*28)
#             nn.MaxPool2d(kernel_size=2, stride=2),#output_size=(6*14*14)
#         )
#         self.conv2 = nn.Sequential(
#             nn.Conv2d(6, 16, 5),
#             nn.ReLU(),      #input_size=(16*10*10)
#             nn.MaxPool2d(2, 2)  #output_size=(16*5*5)
#         )
#         self.fc1 = nn.Sequential(
#             nn.Linear(16 * 5 * 5, 120),
#             nn.ReLU()
#         )
#         self.fc2 = nn.Sequential(
#             nn.Linear(120, 84),
#             nn.ReLU()
#         )
#         self.fc3 = nn.Linear(84, 10)
#
#     # 定义前向传播过程，输入为x
#     def forward(self, x):
#         x = self.conv1(x)
#         x = self.conv2(x)
#         # nn.Linear()的输入输出都是维度为一的值，所以要把多维度的tensor展平成一维
#         x = x.view(x.size()[0], -1)
#         x = self.fc1(x)
#         x = self.fc2(x)
#         x = self.fc3(x)
#         return x
