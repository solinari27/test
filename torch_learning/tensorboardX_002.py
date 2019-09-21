#!/usr/bin/env python
# coding: utf-8

# In[15]:


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

# input pytorch tensor
x = torch.linspace(-5, 5, 200)
x = Variable(x)
x_np = x.data.numpy()
y_tanh = torch.tanh(x).data.numpy()
tag = 'my image'

#use fig to plot
fig = plt.figure()
# plt.plot(x_np, y_tanh, c='red', label='relu')
plt.plot(x_np, y_tanh, label=tag)
# plt.legend(loc='best')

# writer = SummaryWriter('/mnt/c/Users/solinari/.tensorboard/img')
# writer.add_figure(tag='activation_function_' + str(uuid4()), figure=fig)
# writer.close()

if __name__ == '__main__':
    try:
        get_ipython().system('jupyter nbconvert --to python tensorboardX_002.ipynb')
    except:
        pass


# In[ ]:




