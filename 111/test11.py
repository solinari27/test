#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: test.py
@time: 2019/02/10
"""
# import pandas as pd
# import numpy as np
# from sklearn.ensemble import IsolationForest
# ilf = IsolationForest(n_estimators=100,
#                       n_jobs=-1,          # 使用全部cpu
#                       verbose=2,
#                       )
# data = pd.read_csv('data.csv', index_col="id")
# data = data.fillna(0)
# # 选取特征，不使用标签(类型)
# X_cols = ["number_count", "p_count", "prefix_count"]
# # print data.shape
# print data[X_cols]
#
# # 训练
# ilf.fit(data[X_cols])
# shape = data.shape[0]
# batch = 10**6
#
# all_pred = []
# for i in range(shape / batch + 1):
#     start = i * batch
#     end = (i + 1) * batch
#     test = data[X_cols][start:end]
#     # 预测
#     pred = ilf.predict(test)
#     all_pred.extend(pred)
#
# data['pred'] = all_pred
# data.to_csv('outliers.csv', columns=["pred", ], header=False)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

rng = np.random.RandomState(42)

# Generate train data
X = 0.3 * rng.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
# Generate some regular novel observations
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
# Generate some abnormal novel observations
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))

# fit the model
# clf = IsolationForest(behaviour='new', max_samples=100,
#                       random_state=rng, contamination='auto')
clf = IsolationForest(behaviour='new', max_samples=100,
                      n_jobs=-1, verbose=2, contamination='auto')
clf.fit(X_train)
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
print "train: ", y_pred_train
print "test: ", y_pred_test
print "outliers: ", y_pred_outliers

# plot the line, the samples, and the nearest vectors to the plane
xx, yy = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("IsolationForest")
plt.contourf(xx, yy, Z, cmap=plt.cm.Blues_r)

b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c='white',
                 s=20, edgecolor='k')
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c='green',
                 s=20, edgecolor='k')
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c='red',
                s=20, edgecolor='k')
plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend([b1, b2, c],
           ["training observations",
            "new regular observations", "new abnormal observations"],
           loc="upper left")
plt.show()
