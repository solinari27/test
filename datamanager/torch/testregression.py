#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author: solinari
@file: testregression.py
@time: 2019/02/09
"""

from itertools import count
import torch
import torch.autograd
import torch.nn.functional as F


POLY_DEGREE = 1
def make_features(x):
    """Builds features i.e. a matrix with columns [x, x^2, x^3, x^4]."""
    x = x.unsqueeze(1)
    # torch.cat 实现tensor拼接
    return torch.cat([x ** i for i in range(1, POLY_DEGREE + 1)], 1)


W_target = torch.randn(POLY_DEGREE, 1)
b_target = torch.randn(1)


def f(x):
    """Approximated function."""
    return x.mm(W_target) + b_target.item()


def get_batch(batch_size=32):
    """Builds a batch i.e. (x, f(x)) pair."""
    random = torch.randn(batch_size)
    x = make_features(random)
    y = f(x)
    return x, y


# Define model
fc = torch.nn.Linear(W_target.size(0), 1)

###################训练#########################


for batch_idx in count(1):
    # Get data
    batch_x, batch_y = get_batch()

    # Reset gradients
    fc.zero_grad()

    # Forward pass
    output = F.smooth_l1_loss(fc(batch_x), batch_y)
    loss = output.item()

    # Backward pass
    output.backward()

    # Apply gradients
    for param in fc.parameters():
        param.data.add_(-0.1 * param.grad.data)

    # Stop criterion
    if loss < 1e-3:
        break


def poly_desc(W, b):
    """Creates a string description of a polynomial."""
    result = 'y = '
    for i, w in enumerate(W):
        result += '{:+.2f} x^{} '.format(w, len(W) - i)
    result += '{:+.2f}'.format(b[0])
    return result


print('Loss: {:.6f} after {} batches'.format(loss, batch_idx))
print('==> Learned function:\t' + poly_desc(fc.weight.view(-1), fc.bias))
print('==> Actual function:\t' + poly_desc(W_target.view(-1), b_target))
