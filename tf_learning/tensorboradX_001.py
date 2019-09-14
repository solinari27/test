#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: collection.py
@time: 2018/10/09
"""

from tensorboardX import SummaryWriter
import cv2 as cv

# writer = SummaryWriter('C:\Users\solinari\.tensorboard\data')
writer = SummaryWriter('/mnt/c/Users/solinari/.tensorboard/data')
writer.add_image('countdown',
                 cv.imread('data/image/jpg1.jiff'.format(1)))
                 
# for i in range(1, 6):
#     writer.add_image('countdown',
#                      cv.cvtColor(cv.imread('{}.jpg'.format(i)),
#                                  cv.COLOR_BGR2RGB),
#                      global_step=i,
#                      dataformats='HWC')

# import numpy as np
# from tensorboardX import SummaryWriter
# import tensorflow as tf

# writer = SummaryWriter(log_dir='C:\Users\solinari\.tensorboard\data')
# file = open('data/image/logo.png', 'rb')
# data = file.read()
# image = tf.image.decode_png(data, channels=4)
# with tf.Session() as sess:
#     # print type(sess.run(image))
#     writer.add_image(tag='test', img_tensor=sess.run(image))

# for epoch in range(100):

#     writer.add_scalar('scalar/test', np.random.rand(), epoch)
#     writer.add_scalars('scalar/scalars_test',
#                        {'xsinx': epoch * np.sin(epoch), 'xcosx': epoch * np.cos(epoch)}, epoch)

writer.close()


# import tensorflow as tf

# # 获取图片数据
# file = open('data/image/logo.png', 'rb')
# data = file.read()
# file.close()

# # 图片处理
# image = tf.image.decode_png(data, channels=1)
# image = tf.expand_dims(image, 0)

# # 添加到日志中
# sess = tf.Session()
# writer = tf.summary.FileWriter('C:\Users\solinari\.tensorboard\data')
# summary_op = tf.summary.image("image1", image)

# # 运行并写入日志
# summary = sess.run(summary_op)
# writer.add_summary(summary)

# # 关闭
# writer.close()
# sess.close()
