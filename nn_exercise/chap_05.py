# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 20:34
# @Author  : Solinari
# @Email   : deeper1@163.com
# @File    : chap_05.py
# @Software: PyCharm

"""
标准CNN
tensorflow版的卷积神经网路 conv2d() 和max_pool_2x2()函数，然后补全两层卷积的 8个空；
pytorch版本的卷积神经网络 需要补齐 self.conv1 中 nn.Conv2d( ) 和 self.conv2( ) 的参数，还需要填写 x = x.view( )中的内容。
"""

import os
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision
import torch.nn.functional as F
import numpy as np

learning_rate = 1e-4
keep_prob_rate = 0.7  #
max_epoch = 3
BATCH_SIZE = 50

DOWNLOAD_MNIST = False
if not (os.path.exists('./mnist/')) or not os.listdir('./mnist/'):
    # not mnist dir or mnist is empyt dir
    DOWNLOAD_MNIST = True

train_data = torchvision.datasets.MNIST(root='./mnist/', train=True,
                                        transform=torchvision.transforms.ToTensor(),
                                        download=DOWNLOAD_MNIST, )
train_loader = Data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE,
                               shuffle=True)

test_data = torchvision.datasets.MNIST(root='./mnist/', train=False)
test_x = Variable(torch.unsqueeze(test_data.test_data, dim=1),
                  volatile=True).type(torch.FloatTensor)[:500] / 255.
test_y = test_data.test_labels[:500].numpy()


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(  # ???
                # patch 7 * 7 ; 1  in channels ; 32 out channels ; ; stride is 1
                # padding style is same(that means the convolution opration's input and output have the same size)
                in_channels=1,
                out_channels=32,
                kernel_size=7,
                stride=1,
                padding=0,
            ),
            nn.ReLU(),  # activation function
            nn.MaxPool2d(2),  # pooling operation
        )
        # 28-7+1/2=11
        # 32*11*11
        self.conv2 = nn.Sequential(  # ???
            # line 1 : convolution function, patch 5*5 , 32 in channels ;64 out channels; padding style is same; stride is 1
            # line 2 : choosing your activation funciont
            # line 3 : pooling operation function.
            nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=5,
                stride=1,
                padding=0,
            ),
            nn.ReLU(),
            nn.MaxPool2d(1),
        )
        # 64*7*7
        self.out1 = nn.Linear(7 * 7 * 64, 1024,
                              bias=True)  # full connection layer one

        self.dropout = nn.Dropout(keep_prob_rate)
        self.out2 = nn.Linear(1024, 10, bias=True)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(-1, 64*7*7)  # flatten the output of coonv2 to (batch_size ,32 * 7 * 7)    # ???
        out1 = self.out1(x)
        out1 = F.relu(out1)
        out1 = self.dropout(out1)
        out2 = self.out2(out1)
        output = F.softmax(out2)
        return output


def test(cnn, device):
    global prediction
    y_pre = cnn(test_x)
    _, pre_index = torch.max(y_pre, 1)
    pre_index = pre_index.view(-1)
    prediction = pre_index.data.to('cpu').numpy()
    correct = np.sum(prediction == test_y)
    return correct / 500.0


def train(cnn, device):
    optimizer = torch.optim.Adam(cnn.parameters(), lr=learning_rate)
    loss_func = nn.CrossEntropyLoss()
    for epoch in range(max_epoch):
        for step, (x_, y_) in enumerate(train_loader):
            x, y = Variable(x_), Variable(y_)
            x = x.to(device)
            y = y.to(device)
            output = cnn(x)
            loss = loss_func(output, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if step != 0 and step % 20 == 0:
                # print ("epoch.")
                print("=" * 10, step, "=" * 5, "=" * 5, "test accuracy is ",
                      test(cnn, device), "=" * 10)


if __name__ == '__main__':
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    cnn = CNN().to(device)
    test_x = test_x.to(device)
    train(cnn, device)