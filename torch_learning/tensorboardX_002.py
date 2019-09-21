#!/usr/bin/env python
# coding: utf-8

# In[9]:


#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tensorboardX_002.py
@Time    :   2019/09/20 19:50:58
@Author  :   Solinari 
@Contact :   deeper1@163.com
@License :   (C)Copyright 2017-2018, GPLv3
'''

# here put the import lib
# %matplotlib inline
import numpy as np
import torch
import matplotlib.pyplot as plt
from tensorboardX import SummaryWriter
from torch.autograd import Variable
from uuid import uuid4

# switch matplotlib into non-interactive backennd
# dont show img on screen
plt.switch_backend('svg') # or 'svg' agg for png image svg for svg image

# fake data
x = torch.linspace(-5, 5, 200)
x = Variable(x)
x_np = x.data.numpy()

# y_relu = F.relu(x).data.numpy()
# y_sigmoid = F.sigmoid(x).data.numpy()
y_tanh = torch.tanh(x).data.numpy()
# y_softplus = F.softplus(x).data.numpy()
# y_softmax = F.softmax(x)

# fig = plt.figure(1, figsize=(8, 6))
fig = plt.figure()
plt.plot(x_np, y_tanh, c='red', label='relu')
plt.ylim((-1, 5))
plt.legend(loc='best')

# writer = SummaryWriter('/mnt/c/Users/solinari/.tensorboard/img')
# writer.add_figure(tag='activation_function_' + str(uuid4()), figure=fig)
# writer.close()

try:    
    get_ipython().system('jupyter nbconvert --to python tensorboardX_002.ipynb')
except:
    pass


# In[ ]:




