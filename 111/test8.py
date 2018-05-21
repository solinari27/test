#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 21:19
# @Author  : Aries
# @Site    :
# @File    : test8.py
# @Software: PyCharm

# from selenium import webdriver
# 
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# import selenium.webdriver.support.ui as ui
# 
# import time
# 
# def hiBlog(blog_url, username, pwd):
#     driver = webdriver.PhantomJS()
#     driver.get("http://passport.cnblogs.com/user/signin?ReturnUrl=http%3A%2F%2Fwww.cnblogs.com%2F")
#     wait = ui.WebDriverWait(driver, 10)
#     wait.until(lambda dr: dr.find_element_by_id('signin').is_displayed())
#     driver.find_element_by_id("input1").send_keys(username)
#     driver.find_element_by_id("input2").send_keys(pwd)
#     driver.find_element_by_id("signin").click()
#     wait.until(lambda dr: dr.find_element_by_id('login_area').is_displayed())
#     driver.get(blog_url)
#     wait.until(lambda dr: dr.find_element_by_id('么么哒').is_displayed())
#     # 么么哒，ヾ(￣▽￣)Bye~Bye~知道为什么要冷静三秒钟吗？自己想。
#     time.sleep(3)
#     driver.save_screenshot('C:\\screen.png')
#     driver.quit()
# 
# 
# # 执行该文件的主过程
# if __name__ == '__main__':
#     hiBlog("https://home.cnblogs.com/blog/", "solinari", "assign01!")

import urllib
import urllib2
import cookielib
import re
import webbrowser
import json
import sys
import time
import os
from selenium.webdriver.common.proxy import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Taobao:

    # 初始化方法
    def __init__(self):
        # 登录的URL
        self.loginURL = "https://cloud.189.cn/"
        # 检查是否需要滑块解锁的URL
        self.needCodeURL = "https://login.taobao.com/member/request_nick_check.do?_input_charset=utf-8"
        # 用户消息中心
        self.accountInfoURL = "http://ad.alimama.com/earned/settle/getAccountInfo.json"
        self.TPL_username = '18167105607'
        self.TPL_password = 'ASdf1234!'
        self.service_args = [
            # '--proxy=218.241.30.187:8123',
            # '--proxy-type=http',
        ]

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path='/home/solinari/chromedriver')  # 如果没有把chromedriver加入到PATH中,就需要指明路径

        # self.driver = webdriver.PhantomJS(executable_path="D:\\python\\phantomjs\\bin\\phantomjs.exe", service_args=self.service_args)
        # self.driver = webdriver.PhantomJS(service_args=self.service_args)
        # self.driver.set_window_size(1920, 1080)
        # 代理IP地址，防止自己的IP被封禁
        # self.proxyURL = 'http://120.193.146.97:843'
        # 登录POST数据时发送的头部信息
        self.loginHeaders = {
                                'Host': 'https://cloud.189.cn/',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '  
                        'Chrome/51.0.2704.63 Safari/537.36',
                                'Referer': 'https://cloud.189.cn/',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Connection': 'Keep-Alive'
                            },
        # 保存一个 taobao 全局 token
        self._tb_token_ = ''

    # 获取用户消息
    def getAccountInfo(self, cookiestr):
        postData = urllib.urlencode({
            'startTime': '2017-11-09',
            'endTime': '2017-11-16',
            '_tb_token_': self._tb_token_
        })
        print u'登录时候的Token:', self._tb_token_
        headers = {'cookie': cookiestr}
        req = urllib2.Request(self.accountInfoURL, postData, headers=headers)
        try:
            response = urllib2.urlopen(req)
            content = response.read()
            filename = './userMessage.html'
            self.saveFile(content, filename)
            print u'已经获取到账户内容:', content
        except:
            print u'获取用户消息失败!'

            # 登录获取cookie

    def login(self):
        self.driver.get(self.loginURL)
        time.sleep(5)
        print self.driver.page_source.encode('utf-8')
        # self.switchFromLogin()  #切换username/password方式登录，不扫二维码
        self.inputUserName()    #填入username
        self.inputPassword()    #填入password
        self.driver.find_element_by_id("j-login").click()    #点击登录
        time.sleep(1)
        cookie = self.driver.get_cookies()
        print cookie
        return Null
        cookiefilepath = './userCookie.txt'
        cookiestr = self.saveCookie(cookie, cookiefilepath)
        self.driver.close()
        return cookiestr

    # 监测是否需要滑动解锁 todo
    def needCode(self):
        return False

    # 切换普通表单登陆
    def switchFromLogin(self):
        self.driver.find_element_by_id("J_change_type").click()

    def inputUserName(self):
        user_name = self.driver.find_element_by_id('userName')
        user_name.clear()
        user_name.send_keys(self.TPL_username)

    def inputPassword(self):
        password = self.driver.find_element_by_id('password')
        password.clear()
        password.send_keys(self.TPL_password)

    # cookie 写入本地，利于查看,且可返回cookies string
    def saveCookie(self, cookies, cookfilepath):
        cookie = []
        for item in cookies:
            if (item["name"] == '_tb_token_'):
                self._tb_token_ = item["value"]

        cookie = [item["name"] + "=" + item["value"] for item in cookies]
        cookiestr = ';'.join(item for item in cookie)
        f = open(cookfilepath, "a+")
        f.write(cookiestr)
        f.close()
        return cookiestr

    # 临时写入文件 利于调试
    def saveFile(self, content, filepath):
        f = open(filepath, "a+")
        f.write(content)
        f.close()

    def main(self):
        #设置环境
        reload(sys)
        sys.setdefaultencoding('utf-8')

        cookfilepath = self.login();
        self.getAccountInfo(cookfilepath)

taobao = Taobao()
taobao.main()













