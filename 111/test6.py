#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/1 9:23
# @Author  : Aries
# @Site    : 
# @File    : test6.py
# @Software: PyCharm

import json

# with open("../Data/out.json",'r') as load_f:
#     stocks = json.load(load_f)
#
# for item in stocks:
#     print item['code'], item['name']



# load_dict['smallberg'] = [8200,{1:[['Python',81],['shirt',300]]}]
# print(load_dict)
#
# with open("../config/record.json","w") as dump_f:
#     json.dump(load_dict,dump_f)


# #注意路径配置
# with open('../Conf/liangyee.conf') as f:
#     self._liangyeeConf = json.load(f)
#
# #init logging:
# self._logConf = self._liangyeeConf['logging']
# self._name = self._logConf['name']
# self._logger = logging.getLogger(self._name)
# formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
# date_str = time.strftime('%Y_%m_%d', time.gmtime ())
# filename = self._logConf['logpath'] + "/crawler_" + date_str + ".log"
# self._logfile_handler = logging.FileHandler (filename)
# self._logfile_handler.setFormatter(formatter)
# self._logger.addHandler(self._logfile_handler)

#------------ init--------------------#

# while True:     #一直循环，知道访问站点成功
#         try:
#             #以下except都是用来捕获当requests请求出现异常时，
#             # 通过捕获然后等待网络情况的变化，以此来保护程序的不间断运行
#             req = requests.get(company_url, headers = headers, timeout = 20)
#             break
#         except requests.exceptions.ConnectionError:
#             print('ConnectionError -- please wait 3 seconds')
#             time.sleep(3)
#         except requests.exceptions.ChunkedEncodingError:
#             print('ChunkedEncodingError -- please wait 3 seconds')
#             time.sleep(3)
#         except:
#             print('Unfortunitely -- An Unknow Error Happened, Please wait 3 seconds')
#             time.sleep(3)


import liangyee.liangyeeCrawler
ll = liangyee.liangyeeCrawler.liangyeeCrawler()
ll.setID('6F49F56DCE594273BF0B927C8ABE0A12')
print ll.get5MinKData('600000')












