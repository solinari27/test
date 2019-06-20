#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author: solinari
@file: torch_less1.py
@time: 2018/10/17
"""

import torch
import torch.optim as optim

x = torch.Tensor(2,3,4) #torch.Tensor(shape) 创建出一个未初始化的Tensor
print x
print x.size

a = torch.rand(2,3,4)
b = torch.rand(2,3,4)

print (a,b)
_=torch.add(a,b,out=x) #使用Tensor()方法创建出来的Tensor用来接收计算结果，当然torch.add(..)也会返回计算结果
print x

a.add_(b) #所有带_的operation，都会更改调用对象的值
print "after add_ ", a

print torch.cuda.is_available() #检查CUDA

from torch.autograd import Variable
x = torch.rand(5)
x = Variable(x, requires_grad=True)
y = x*2
grads = torch.FloatTensor([1,2,3,4,5])
print y.backward(grads) #如果y是scalar的话，那么直接y.backward()，然后通过x.grad的方式，就可以得到var的梯度

print x.grad

#----------------------------------------------------------------------------------------------------

import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):

    def __init__(self):
        """
        建立一个网络
        网络结构：
        2个卷积层
        3个全连接层
        """
        super(Net, self).__init__()
        #建立了两个卷积层, self.conv1, self.conv2， 注意：这些层都是不包含激活函数的
        self.conv1 = nn.Conv2d(1,6,5) #1input image channel, 6output channels, 5x5 square convolution kernel
        self.conv2 = nn.Conv2d(6,16,5)
        #3个全连接层
        self.fc1 = nn.Linear(16*5*5, 120) # an affine operation: y=Wx + b
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x): #注意： 2D卷积层的输入data维数是batchsize*channel*height*width
        x = F.max_pool2d(F.relu(self.conv1(x)), (2,2)) #max pooling over a (2,2) window
        x = F.max_pool2d(F.relu(self.conv2(x)), 2) #if the size is a square you can only specify a single number
        x = x.view(-1, self.num_flat_features(x))
        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        x=self.fc3
        return x

    def num_flat_feature(self, x):
        size = x.size()[1:] #all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features

# net = Net()
# print net
# print len(list(net.parameters())) #为什么是10呢？因为不仅有weights，还有bias， 10=5x2
# input = Variable(torch.randn(1,1,32,32))
# out = net(input) #调用Net(nn.Module)的__call__函数
# print out
# out.backward(torch.randn(1,10))

# net = Net()
# #create your optimizer
# learning_rate = 0.01
# opertimizer = optim.SGD(net.parameters(),
#                         lr=learning_rate)
# #optim.Adam
#
# #in your training loop:
# num_iterations = 10
# for i in range(num_iterations):
#     optimizer.zero_grad() #gradient清零，如果不清零会累加
#     output = net(input) #这里就体现出来动态建图了，你还可以传入其他的参数来改变网络的结构
#     loss =criterion(ouput, target)
#     loss.backward() #得到grad i.e. 给Variable.grad赋值
#     optimizer.step() #DOes the update, i.e. Variable.data -= learning_rate*Variable.grad
