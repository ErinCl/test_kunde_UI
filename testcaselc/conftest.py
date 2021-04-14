#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/23
# @Author  : chenlin
# @Site    :
# @File    : conftest.py
# @Software: PyCharm
"""
conftest.py 全局变量，主要实现以下功能：
1、添加命令行参数broswer， 用于切换不用浏览器
2、全局参数driver调用
"""

import time
import pytest
from public.common import pyselenium
from public.common import datainfo
from public.appmodel import loginaction
from config import globalparam
from public.common import log


log = log.Log()


@pytest.fixture(scope="session")
def driver(request):
    global driver
    '''只打开浏览器和关闭浏览器'''
    log.info("打开浏览器")
    driver = pyselenium.PySelenium(globalparam.browser)
    driver.max_window()  # 最大化

    def end():
        log.info("用例全部执行完毕，关闭浏览器")
        time.sleep(globalparam.small)
        driver.quit()

    request.addfinalizer(end)
    return driver


@pytest.fixture()
def login_admin(request, driver):
    """用户登录"""
    log.info("用户登录")
    login = loginaction.Login(driver)
    login.login('15928009284','www123456.')

    def end():
        log.info("测试用例执行完成，登出系统")
        driver.origin_driver.delete_all_cookies()

    request.addfinalizer(end)
    return driver
