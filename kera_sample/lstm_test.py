#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: PolynomialRegression.py
@time: 2018/11/11
"""

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

max_features = 1024

model = Sequential()
model.add(Embedding(max_features, output_dim=256))
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=16, epochs=10)
score = model.evaluate(x_test, y_test, batch_size=16)