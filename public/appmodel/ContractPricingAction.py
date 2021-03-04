#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021年2月25日13:28:02
# @Author  : Dannaliu
# @Site    :
# @File    : ContractPricingAction.py
# @Software: PyCharm

import allure

from time import sleep
from public.pages import ContractPricingPage
from public.common import log


#合同定价
class ContractPricingAction(object):

    def __init__(self, driver):
        self.dr = driver
        self.propg = ContractPricingPage.ContractPricingPage(self.dr)
        self.log = log.Log()

    def create_pricing(self,applytype, project):
        """
        合同定价
        :param applytype:
        :param project:
        :param goodcode:
        :param goodnum:
        :return:
        """
        with allure.step("合同定价"):
            allure.attach('采购类型:%s' % applytype)
            allure.attach("工程项目：%s" % project)
            sleep(3)
            # 点击应用
            self.propg.click_app_button()
            sleep(3)
            #滚动下拉
            self.propg.get_scorll_button('document.getElementById("flexapp")', 'scrollTop',8000)
            # 点击合同管理
            self.propg.click_menu_button()
            sleep(1)
            # 点击合同定价
            self.propg.click_sidebar_button()
            sleep(1)
            # 点击新增
            self.propg.click_create_button()
            sleep(1)
            #选择工程项目
            self.propg.input_project(project)
            sleep(1)
            #选择采购类型
            self.propg.input_applytype(applytype)
            sleep(5)
            # 滚动下拉
            self.propg.get_scorll_button('document.getElementById("contentpanelflex")', 'scrollTop',9900)
            sleep(1)
            #点击增行增加明细列表
            self.propg.click_add()
            sleep(1)
            #点击第一行的定价类型
            self.propg.click_pricetype("1")
            sleep(0.5)
            #选择物料
            self.propg.click_materiel("01000200010001")
            sleep(0.5)
            #选择供应商
            self.propg.choice_supplier("SUP-20201016-0001")
            sleep(0.5)
            #输入单价
            self.propg.input_price("12.5")
            sleep(0.5)
            # 滚动右拉
            self.propg.get_scorll_button('document.getElementsByClassName("ag-body-horizontal-scroll-viewport")[1]', 'scrollLeft', 500)
            sleep(0.5)
            # 关联采购明细
            self.propg.purchase_details()






if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("13541349886","ld1234567!")
    sleep(1)
    t_data = {
        'applytype': '1.2',
        'project': '21010004'
    }
    ta = ContractPricingAction(dr)
    ta.create_pricing(str(t_data["applytype"]),str(t_data["project"]))