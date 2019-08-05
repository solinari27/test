# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 20:43
# @Author  : Solinari
# @Email   : deeper1@163.com
# @File    : chap_03.py
# @Software: PyCharm
"""
实现一个全连接(full connection)网络
"""


# import tensorflow as tf
# from tensorflow.examples.tutorials.mnist import input_data
#
# # number 1 to 10 data
# mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
#
#
# def compute_accuracy(v_xs, v_ys):
#     global prediction
#     y_pre = sess.run(prediction, feed_dict={inputs: v_xs})
#     correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(v_ys, 1))
#     accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
#     result = sess.run(accuracy, feed_dict={inputs: v_xs, outputs: v_ys})
#     return result
#
#
# # 定义相关参数
# in_size = 784  # 输入的尺寸
# out_size = 10  # 输出的尺寸
# learning_rate = 0.1  # 学习率
# max_epochs = 3000  # 最大训练步数
#
# inputs = tf.placeholder(tf.float32, [None, in_size])  # 28x28
# outputs = tf.placeholder(tf.float32, [None, out_size])  # 10
#
# Weights = tf.Variable(tf.random_normal([in_size, out_size]))
# biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, )
#
# prediction = tf.nn.softmax(tf.matmul(inputs, Weights) + biases)
# #################################################################
# # 请在下面补全交叉熵 和 训练两个节点。
# cross_entropy =
#
# train_step =
#
# #################################################################
# sess = tf.Session()
# init = tf.global_variables_initializer()  # 注意tensorflow 版本在 0.12 以后，才能执行这句命令
# sess.run(init)
# for i in range(max_epochs):
#     batch_xs, batch_ys = mnist.train.next_batch(100)
#     sess.run(train_step, feed_dict={inputs: batch_xs, outputs: batch_ys})
#     if i % 500 == 0:
#         print(compute_accuracy(
#             mnist.test.images, mnist.test.labels))


import torch
import torchvision
import torchvision.transforms as transforms
from torch import nn


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


class simpleNet(nn.Module):
    """
    定义了一个简单的三层全连接神经网络，每一层都是线性的
    """

    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super(simpleNet, self).__init__()
        self.layer1 = nn.Linear(in_dim, n_hidden_1)     #nn.XXX 这个花样比较多，线性的，卷积的，sequential...
        self.layer2 = nn.Linear(n_hidden_1, n_hidden_2)
        self.layer3 = nn.Linear(n_hidden_2, out_dim)

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x


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
