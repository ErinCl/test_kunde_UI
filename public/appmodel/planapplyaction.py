#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 14:45
# @Author  : chenlin
# @Site    :
# @File    : planapplyaction.py
# @Software: PyCharm

import allure

from time import sleep
from public.pages import planApplyPage
from public.common import log


class CreatePlanApplyAction(object):

    def __init__(self, driver):
        self.dr = driver
        self.propg = planApplyPage.planApplyPage(self.dr)
        self.log = log.Log()

    def create_apply(self, applytype, project, goodnum1, goodnum2):
        """
        主材采购申请
        :param applytype:
        :param project:
        :param goodcode:
        :param goodnum:
        :return:
        """
        with allure.step("物资申请"):
            allure.attach('申请类型:%s' % applytype)
            allure.attach("工程项目：%s" % project)
            # allure.attach("物料编码：%s" % goodcode)
            allure.attach("物料数量：%s" % goodnum1)
            allure.attach("物料数量:%s" % goodnum2)

            sleep(3)
            # 点击应用
            self.propg.click_use_button()
            sleep(3)
            # 点击物资管理，暂时无法通过应用下物资管理进入页面
            self.propg.move_to_window_jz()
            self.propg.click_good_button()
            sleep(1)
            # 点击侧边栏
            self.propg.click_sidebar_button()
            sleep(1)
            # 点击需用计划
            self.propg.click_plan_button()
            # 点击采购申请
            self.propg.click_apply_button()
            sleep(3)
            # 点击新增
            self.propg.click_create_apply_button()
            sleep(1)
            # 填写采购类型
            self.propg.input_applytype(applytype)
            sleep(1)
            # 填写工程项目
            self.propg.input_project(project)
            sleep(1)
            # 下拉滚动条
            self.propg.move_scroll_bar()
            # 点击新增物料
            self.propg.click_add_button()
            sleep(1)
            # 点击输入框，显示放大镜
            self.propg.click_goods_button()
            # 点击放大镜
            self.propg.click_good_glass()
            sleep(1)
            # 点击物资：混凝土
            self.propg.click_good_id1()
            sleep(1)
            # 点击下拉框：主要材料
            self.propg.click_down_drop()
            sleep(1)
            # 点击下拉框：水泥
            self.propg.click_down_drop_sr()
            sleep(1)
            self.propg.click_good_szsr()
            sleep(1)
            # 选择水泥
            self.propg.click_good_id2()
            # 确定
            self.propg.click_confirm_button()
            sleep(1)
            # 点击数量输入框
            self.propg.click_good_num1()
            # 输入数量
            self.propg.input_good_num1(goodnum1)
            sleep(1)
            self.propg.click_good_num2()
            self.propg.input_good_num2(goodnum2)
            # 点击提交
            self.propg.click_good_sumbit()
            sleep(2)
            # 点击审核
            self.propg.click_audit_button()
            sleep(1)
            # 断言
            flag =self.dr.element_exist('xpath-> //span[text()="已审核"]')
            assert flag
            # 关闭物资管理
            self.propg.move_good_button()
            self.propg.close_good_button()


            # # 点击退出
            # self.propg.click_quit_button()

    def create_apply_lw(self, applytype, project, quantities, quantities1, goodnum1, goodnum2, cost, part, nature):
        """
        劳务采购申请
        :param applytype:
        :param project:
        :param quantities:
        :param quantities1:
        :param goodnum1:
        :param goodnum2:
        :param cost:
        :param part:
        :param nature:
        :return:
        """
        with allure.step("劳务申请"):
            allure.attach('申请类型:%s' % applytype)
            allure.attach("工程项目：%s" % project)
            allure.attach("工程量：%s" % quantities)
            allure.attach("工程量2：%s" % quantities1)
            allure.attach("物料数量：%s" % goodnum1)
            allure.attach("物料数量:%s" % goodnum2)
            allure.attach("费用名称:%s" % cost)
            allure.attach("部位:%s" % part)
            allure.attach("合同性质%s" % nature)

            sleep(3)
            # 点击应用
            self.propg.click_use_button()
            sleep(3)
            # 点击物资管理
            self.propg.move_to_window_jz()
            self.propg.click_good_button()
            sleep(1)
            # 点击侧边栏
            self.propg.click_sidebar_button()
            sleep(1)
            # 点击需用计划
            self.propg.click_plan_button()
            # 点击采购申请
            self.propg.click_apply_button()
            sleep(3)
            # 点击新增
            self.propg.click_create_apply_button()
            # 填写采购类型
            self.propg.input_applytype(applytype)
            sleep(1)
            # 填写工程项目
            self.propg.input_project(project)
            sleep(1)
            # 下拉滚动条
            self.propg.move_scroll_bar()
            sleep(1)
            # 点击新增物料
            self.propg.click_add_labour_button()
            sleep(1)
            # 点击费用名称
            self.propg.click_cost_name()
            self.propg.input_cost_name(cost)
            sleep(1)
            # 输入部位
            self.propg.click_part_id()
            self.propg.input_part_id(part)
            # 输入合同性质
            self.propg.click_nature_id()
            self.propg.input_nature_id(nature)
            sleep(1)
            # 滚动条右拉
            self.propg.move_drop_right()
            sleep(2)
            # 输入工程量
            self.propg.click_quantities_num()
            sleep(2)
            self.propg.input_quantities_num(quantities)
            sleep(1)
            self.propg.click_equitment_num()
            sleep(1)
            self.propg.input_equitment_num(goodnum1)
            self.propg.click_good_sumbit()
            sleep(1)
            # 审核
            self.propg.click_audit_button()


if __name__ == '__main__':
    from public.common import pyselenium
    from config import globalparam
    from public.appmodel.loginaction import Login

    dr = pyselenium.PySelenium(globalparam.browser)
    dr.max_window()
    login = Login(dr).login("15928009283", "qqq123456")
    ta = CreatePlanApplyAction(dr)
