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

    def create_expend_contract(self, pricing_type, project, contract_officer, supplier, main_content,
                               contract_explain, payment_type, compress_zip):
        """
        主材支出合同
        :param pricing_type:
        :param project:
        :param contract_officer:
        :param supplier:
        :param main_content:
        :param contract_explain:
        :param payment_type:
        :param compress_zip:
        :return:
        """
        with allure.step("主材合同申请"):
            allure.attach('定价类型:%s' % pricing_type)
            allure.attach("工程项目：%s" % project)
            allure.attach("甲方代表：%s" % contract_officer)
            allure.attach("供应商：%s" % supplier)
            allure.attach("合同主要内容:%s" % main_content)
            allure.attach("合同说明:%s" % contract_explain)
            allure.attach("付款方式:%s" % payment_type)

        # 点击应用
        self.propg.click_use_button()
        sleep(1)
        # 点击应用
        self.propg.move_use_scroll_bar()
        sleep(2)
        # 点击合同管理
        self.propg.click_good_button()
        # 点击侧边栏
        self.propg.click_sidebar_button()
        # 点击新增合同
        self.propg.click_create_button()
        # 填写定价类型
        self.propg.input_pricing_type(pricing_type)
        sleep(1)
        # 填写工程项目
        self.propg.input_project(project)
        sleep(2)
        # 填写甲方代表
        self.propg.intput_owner_representative(contract_officer)
        # 填写供应商
        self.propg.input_supplier_name(supplier)
        sleep(2)
        # 选择定价单
        self.propg.click_pricing_num()
        sleep(2)
        # 输入合同内容
        self.propg.input_zc_contract_content(main_content)
        # 输入合同说明
        self.propg.input_contract_explain(contract_explain)
        # 输入付款方式
        self.propg.input_payment_type(payment_type)
        # 选择物料信息
        self.propg.click_zc_good_detail()
        sleep(1)
        # 选择定价单明细
        self.propg.click_zc_pricing_detail()
        sleep(1)
        # 上传附件
        self.propg.input_contract_zip(compress_zip)
        sleep(2)
        # 提交合同
        self.propg.click_submit_button()
        # 断言
        flag = self.dr.element_exist('xpath-> //input[text()="预审"]')
        assert flag

    def create_expend_lw_contract(self, purchase_type, project, contract_officer, supplier, main_content,
                                  contract_explain, payment_type, compress_zip):
        """
        创建劳务合同
        :param pricing_type:
        :param project:
        :param contract_officer:
        :param supplier:
        :param main_content:
        :param contract_explain:
        :param payment_type:
        :param compress_zip:
        :return:
        """
        with allure.step("劳务合同申请"):
            allure.attach('采购类型:%s' % purchase_type)
            allure.attach("工程项目：%s" % project)
            allure.attach("甲方代表：%s" % contract_officer)
            allure.attach("供应商：%s" % supplier)
            allure.attach("合同主要内容:%s" % main_content)
            allure.attach("合同说明:%s" % contract_explain)
            allure.attach("付款方式:%s" % payment_type)
            # 点击应用
            self.propg.click_use_button()
            sleep(1)
            # 点击应用
            self.propg.move_use_scroll_bar()
            sleep(2)
            # 点击合同管理
            self.propg.click_good_button()
            # 点击侧边栏
            self.propg.click_sidebar_button()
            # 点击新增合同
            self.propg.click_create_button()
            # 填写定价类型
            self.propg.input_purchase_type(purchase_type)
            sleep(1)
            # 填写工程项目
            self.propg.input_project(project)
            sleep(2)
            # 填写甲方代表
            self.propg.intput_owner_representative(contract_officer)
            # 填写供应商
            self.propg.input_supplier_name(supplier)
            sleep(2)
            # 选择定价单
            self.propg.click_pricing_num()
            sleep(2)
            # 输入合同内容
            self.propg.input_lw_contract_content(main_content)
            # 输入合同说明
            self.propg.input_contract_explain(contract_explain)
            # 输入付款方式
            self.propg.input_payment_type(payment_type)
            # 选择物料信息
            self.propg.click_lw_good_detail()
            # 选择定价单明细
            self.propg.click_lw_pricing_detail()
            sleep(1)
            # 上传附件
            self.propg.input_contract_zip(compress_zip)
            sleep(2)
            # 提交合同
            self.propg.click_submit_button()

    def audit_contract(self):
        """审核预审合同"""
