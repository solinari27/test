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
#     wait.until(lambda dr: dr.find_element_by_id('么么哒').is_displayer
#     time.sleep(3)
#     driver.save_screenshot('C:\\screen.png')
#     driver.quit()
# 
# 
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


class eDrive:

    def __init__(self):
        # login URL
        self.loginURL = "https://cloud.189.cn/udb/udb_login.jsp?pageId=1&amp;redirectURL=/main.action"
        # message center
        self.TPL_username = '18167105607'
        self.TPL_password = 'ASdf1234!'
        self.service_args = [
            # '--proxy=218.241.30.187:8123',
            # '--proxy-type=http',
        ]

        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\Program Files (x86)\Google\chromedriver\chromedriver')

        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_size(1920, 1080)
        self.loginHeaders = {
                                'Host': 'https://cloud.189.cn/',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
                                'Referer': 'https://cloud.189.cn/',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Connection': 'Keep-Alive'
                            },
        self._tb_token_ = ''

    def __del__(self):
        self.driver.close ()

    def login(self):
        self.driver.get(self.loginURL)
        time.sleep(5)
        # print self.driver.page_source.encode('utf-8')
        # self.switchFromLogin()  
        self.inputUserName()    #username
        self.inputPassword()    #password
        self.driver.find_element_by_id("j-login").click()    #click to login
        time.sleep(3)
        cookie = self.driver.get_cookies()
        print "cookie:", cookie
#        return Null
#        cookiefilepath = './userCookie.txt'
#        cookiestr = self.saveCookie(cookie, cookiefilepath)
#        return cookiestr

    def needCode(self):
        return False

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

         
    # def saveCookie(self, cookies, cookfilepath):
    #     cookie = []
    #     for item in cookies:
    #         if (item["name"] == '_tb_token_'):
    #             self._tb_token_ = item["value"]
    #
    #     cookie = [item["name"] + "=" + item["value"] for item in cookies]
    #     cookiestr = ';'.join(item for item in cookie)
    #     f = open(cookfilepath, "a+")
    #     f.write(cookiestr)
    #     f.close()
    #     return cookiestr
    #
    # # save to File
    # def saveFile(self, content, filepath):
    #     f = open(filepath, "a+")
    #     f.write(content)
    #     f.close()

    def main(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')

        cookfilepath = self.login();

edrive = eDrive()
edrive.main()













