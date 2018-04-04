#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/3 17:03
# @Author  : Aries
# @Site    : 
# @File    : try.py
# @Software: PyCharm

import time
import liangyee.liangyeeCrawler
ll = liangyee.liangyeeCrawler.liangyeeCrawler()
# print ll.get5MinKData('600000')
#
# time.sleep(3)
# print ll.getMarketData([600027, 600100])

ll.crawlliangyee()

# now = time.gmtime()
# print now.tm_year
# print now.tm_mon
# print now.tm_mday

