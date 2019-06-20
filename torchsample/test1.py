#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: solinari 
@file: test1.py 
@time: 2018/05/05 
"""  

import torch
import torchvision

print torch.cuda.is_available()
print torch.cuda._check_driver()
if torch.cuda.is_available():
    print "ok"

