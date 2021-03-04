#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021年2月25日09:59:25
# @Author  : Dannaliu
# @Site    :
# @File    : ContractPricingPage.py
# @Software: PyCharm

from public.pages import basepage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# 合同定价类
class ContractPricingPage(basepage.Page):

    def click_app_button(self):
        self.log.debug("点击应用")
        self.dr.click("xpath-> //*[@id='flexpanelap']/div[3]/div/div[2]/div[1]")

    def get_scorll_button(self,position,direction,num):
        #获取并滑动滚动条
        self.getscroll(position,direction,num)

    def click_menu_button(self):
        self.log.debug("点击合同管理")
        self.dr.click("xpath-> //*[@title='合同签订、结算、变更、收付款、资金计划等']")

    def click_sidebar_button(self):
        "鼠标移动到侧边栏"
        self.move_to_el_icon("xpath-> //*[@id='flexpanelap']/div[1]/div/div[3]/i")
        self.log.debug("点击合同定价")
        self.dr.click("xpath-> //li[@title='合同定价']/span")

    def click_create_button(self):
        #先点一下框架移开遮挡页面的菜单
        self.dr.click("xpath-> //*[@id='flexpanelap1']")
        sleep(0.5)
        #点击新增按钮
        self.log.debug("点击新增合同定价")
        self.dr.click("xpath-> //*[@id='tblnew']/span/span")

    def input_project(self, value):
        "填写工程项目"
        self.dr.type_and_enter("xpath-> //*[@id='kdzl_project']/div[2]/div/div[1]/input", value)

    def input_applytype(self, value):
        "填写采购类型"
        self.dr.type_and_enter("xpath-> //*[@id='kdzl_purchasetype']/div[2]/div/div[1]/input", value,1)

    def click_add(self):
        "点击增行"
        self.dr.click("xpath-> //div[@id='kdzl_advconbaritemap']/span")

    def click_pricetype(self,type):
        self.log.debug("点击定价类型")
        self.dr.click("xpath-> //*[@id='kdzl_contapricedtlcl']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div")
        sleep(0.5)
        self.log.debug("点选择主材采购")
        self.dr.type_and_enter("xpath-> //*[@id='kdzl_contapricedtlcl']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div/div/div[1]/input", type)
        sleep(1)

    def click_materiel(self,materiel):
        self.log.debug("选择物料编码")
        self.dr.click("xpath-> //*[@id='kdzl_contapricedtlcl']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[3]/div")
        self.log.debug("选择泵送混凝土")
        self.dr.type_and_enter("xpath-> //*[@id='kdzl_contapricedtlcl']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[3]/div/div/div[1]/input",materiel)

    def choice_supplier(self,sup):
        self.log.debug("选择供应商")
        self.dr.click("xpath-> //*[@id='kdzl_contapricedtlcl']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[6]/div")
        sleep(0.5)
        self.dr.type_and_enter("xpath-> //*[@id='kdzl_contapricedtlcl']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[6]/div/div/div[1]/input",sup)

    def input_price(self,price):
        self.log.debug("输入单价")
        self.dr.click("xpath-> //*[@id='kdzl_contapricedtlcl']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[7]/div")
        sleep(0.5)
        self.dr.type_and_enter("xpath-> //*[@id='kdzl_contapricedtlcl']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[7]/div/div[1]/input",price)

    def purchase_details(self):
        self.log.debug("关联采购申请明细")
        self.dr.click("xpath-> //*[@id='kdzl_contapricedtlcl']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[11]/div")
        sleep(0.2)
        self.dr.click("xpath-> //*[@id='kdzl_contapricedtlcl']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[11]/div/div/div[2]")
        sleep(1)