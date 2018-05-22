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
        self.loginURL = "https://open.e.189.cn/api/logbox/oauth2/unifyAccountLogin.do?appId=cloud&version=v1.5&clientType=10010&format=redirect&paras=BDD0E1B9249A4785959A9862EC291A2E50E5636D06716393177920103CB773FF5E5096DB29AC36FEB46E10228D551FD2E7C5BFCE922EC7EEBA0969EE5365370664558D139D4B90D5BB6AC4E6390A3553B959C0485A2985A1DF241D71F09A54B922B5098F6745DB92FA5F4D54B9A5A84E103DDF29A1C0FB9353B4F71CF1DD52FDC7CDCD679B42B92283AF246FC828FA96152D6C9246FE729761836E5AEE0A30C271B658EEF80249AA0DDEBD7B1DD663F15A7C0C532A389E2A4763EFB318CD9937D374BE0CE4F26275916F89C68627702D7B7EBD714845E0C7AF42ABCE06735ADE4C805DCD1B125E4ADBFB8744C10A775BC33ABBE244A85FE4BE0E723AD246881A0C27D4327E3244124B0579367B0068CEB4429C1C4D18A1E75631E9D8DE214D7841E53E8CE6F2D46795A5577665EA2AEC5742BC2FFF0DC332DBB666AEF52AE15038B8B3843D20E6A09223F9F1BEF7D66000A8A4097247226A01B59F6B2666B7159D17D0CDC4CE8EAE1408569AAC4BEB6FC1AE0BE8B56D44D6CA5CCDF6CBB5BB2E2032E6D2A468F90F4D4D9965CB2A463251A18B7436C0F8704585C71B441415B902E09E8F82A1231A61227BCB9C4FB462128DE28780866261EA31469481E0A1575C5D2FEDD56E25BFDFE9E836544194D992DFA82C31D4474DDE4EE300A45F4035A7628D2D208A4F6B&sign=A75DDF00841CB9991F3F11EB2C00486ED78E6133"
        # message center
        self.TPL_username = '18167105607'
        self.TPL_password = 'ASdf1234!'
        self.service_args = [
            # '--proxy=218.241.30.187:8123',
            # '--proxy-type=http',
        ]

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\Program Files (x86)\Google\chromedriver\chromedriver')

#        # se111r.set_window_size(1920, 1080)
        self.loginHeaders = {
                                'Host': 'https://cloud.189.cn/',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
                                'Referer': 'https://cloud.189.cn/',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'Connection': 'Keep-Alive'
                            },
        self._tb_token_ = ''


    def login(self):
        self.driver.get(self.loginURL)
        time.sleep(3)
#        print self.driver.page_source.encode('utf-8')
        # self.switchFromLogin()  
        self.inputUserName()    #username
        self.inputPassword()    #password
        self.driver.find_element_by_id("j-login").click()    #click to login
        time.sleep(1)
        cookie = self.driver.get_cookies()
        print cookie
#        return Null
#        cookiefilepath = './userCookie.txt'
#        cookiestr = self.saveCookie(cookie, cookiefilepath)
#        self.driver.close()
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

    # save to File
    def saveFile(self, content, filepath):
        f = open(filepath, "a+")
        f.write(content)
        f.close()

    def main(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')

        cookfilepath = self.login();

taobao = eDrive()
taobao.main()













