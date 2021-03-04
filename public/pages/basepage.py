#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/21
# @Author  : chenlin
# @Site    :
# @Software: PyCharm

from public.common import log
from config import globalparam
from public.common import publicfunction


class Page(object):
    """
    This is a base page class for Page Object.
    """

    def __init__(self, selenium_driver):
        self.dr = selenium_driver
        self.log = log.Log()

    def getscroll(self, position, direction, num):
        """
        Control the scroll bar to scroll in the desired direction
        Usage:
                getscroll('document.getElementById("flexapp")','scrollTop','10000')
        """
        self.log.debug("滑动滚动条")
        js = '%s.%s=%s' % (position, direction, num)  # 找到滚动条
        print(js)
        self.dr.js(js)

    def move_to_el_icon(self, el):
        self.log.debug("鼠标悬停")
        self.dr.move_to_element(el)

