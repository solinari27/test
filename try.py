#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 17:03
# @Author  : Aries
# @Site    : 
# @File    : try.py
# @Software: PyCharm

import liangyee.liangyeeCrawler
ll = liangyee.liangyeeCrawler.liangyeeCrawler()
ll.setID('6F49F56DCE594273BF0B927C8ABE0A12')
# print ll.get5MinKData('600000')

ll.crawlliangyee()

