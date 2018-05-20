#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/20 21:19
# @Author  : Aries
# @Site    :
# @File    : test8.py
# @Software: PyCharm

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui

import time

def hiBlog(blog_url, username, pwd):
    driver = webdriver.PhantomJS()
    driver.get("http://passport.cnblogs.com/user/signin?ReturnUrl=http%3A%2F%2Fwww.cnblogs.com%2F")
    wait = ui.WebDriverWait(driver, 10)
    wait.until(lambda dr: dr.find_element_by_id('signin').is_displayed())
    driver.find_element_by_id("input1").send_keys(username)
    driver.find_element_by_id("input2").send_keys(pwd)
    driver.find_element_by_id("signin").click()
    wait.until(lambda dr: dr.find_element_by_id('login_area').is_displayed())
    driver.get(blog_url)
    wait.until(lambda dr: dr.find_element_by_id('么么哒').is_displayed())
    # 么么哒，ヾ(￣▽￣)Bye~Bye~知道为什么要冷静三秒钟吗？自己想。
    time.sleep(3)
    driver.save_screenshot('C:\\screen.png')
    driver.quit()


# 执行该文件的主过程
if __name__ == '__main__':
    hiBlog("https://home.cnblogs.com/blog/", "solinari", "assign01!")















