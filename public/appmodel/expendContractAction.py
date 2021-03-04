#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 14:45
# @Author  : chenlin
# @Site    :
# @File    : expendContractAction.py
# @Software: PyCharm


import allure

from time import sleep
from public.pages import expendContractPage
from public.common import log


class CreateExpendContractAction(object):

    def __init__(self, driver):
        self.dr = driver
        self.propg = expendContractPage.expendContractPage(self.dr)
        self.log = log.Log()

    def create_expend_contract(self,pricing_type,project,contract_officer,supplier,pricing_id,main_content,contract_explain,payment_type):
        """
        主材采购合同
        :param pricing_type:
        :param project:
        :param contract_officer:
        :param supplier:
        :param pricing_id:
        :param main_content:
        :param contract_explain:
        :param payment_type:
        :return:
        """
        with allure.step("主材合同申请"):
            allure.attach('定价类型:%s' % pricing_type)
            allure.attach("工程项目：%s" % project)
            allure.attach("甲方代表：%s" % contract_officer)
            allure.attach("供应商：%s" % supplier)
            allure.attach("定价单号：%s" % pricing_id)
            allure.attach("合同主要内容:%s" % main_content)
            allure.attach("合同说明:%s" % contract_explain)
            allure.attach("付款方式:%s" % payment_type)

        # 点击应用
        self.propg.click_use_button()
        sleep(1)
        self.propg.move_use_scroll_bar()
        sleep(2)
