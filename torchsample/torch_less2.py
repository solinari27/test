#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: solinari
@file: torch_less1.py
@time: 2018/10/17
"""

import torch
from torch.autograd import Variable
import torch.optim as optim

w1 = Variable(torch.Tensor([1.0, 2.0, 3.0]), requires_grad=True) #需要求导的话，requires_grad=True是必须的
w2 = Variable(torch.Tensor([1.0, 2.0, 3.0]), requires_grad=True)
print (w1.grad) #应该是None，没求
print (w2.grad) #应该是None

d=torch.mean(w1)
d.backward()
print w1.grad #grad自动累加

w1.grad.data.zero_() #grad清零
print w1.grad

learning_rate = 0.1
w1.data -= learning_rate*w1.grad.data #与下面式子等价
#自己写的更新， 可以使用torch.optim中的更新方法
w1.data.sub_(learning_rate*w1.grad.data) #w1.data是获取保存weights的Tensor

print w1, w1.data
print type(w1)
print type(w1.data)

from torch_less1 import Net
net = Net()
#create your optimizer
optimizer = optim.SGD(net.parameters(), lr=0.01)
#input: input data
# input channel: conv2d input channel: 1
# output_height: (input_height-kernel+2*padding/stride[height]+1
# output_width: (input_width-kernel+2*padding/stride[height]+1
#横向和纵向的跳数应该一致
input = Variable(torch.randn(10,1,32,32))
print "net:", net

#in your training loop:
#steps:
steps = 1
for i in range(steps):
    optimizer.zero_grad() #grad清零，必须
    output=net(input) #前向计算
    loss = criterion(output, target) #计算代价函数
    # pytorch 保存了loss function的定义，loss只能是Variable类型
    # 通过Tensor计算到的只能是Tensor， 通过Variable计算得到的也是Variable
    loss.backward() #计算梯度
    optimizer.step() #更新参数




