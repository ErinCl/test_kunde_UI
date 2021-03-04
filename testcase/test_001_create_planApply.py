#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/02/02 14:00
# @Author  : chenlin
# @Site    :
# @File    : test_001_create_planAppply.py
# @Software: PyCharm


import pytest
from public.common import datainfo
from public.appmodel import planapplyaction
from public.pages import planApplyPage
from public.common.publicfunction import *


@allure.feature("采购申请")
class TestCreateApply():
    '''创建采购申请'''

    @allure.story("创建主材采购申请")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_create_zc_apply(self, login_admin):
        dr = login_admin
        # t_data = {
        #     'casename': '主材采购申请',
        #     'applytype': '1.2',
        #     'project': '21010004',
        #     'goodnum1': 10,
        #     'goodnum2': 20
        # }
        t_data = datainfo.get_xls_to_dict("planapply.xlsx", "Sheet1")["主材采购申请"]
        ua = planapplyaction.CreatePlanApplyAction(dr)
        ua.create_apply(str(t_data["applytype"]), str(t_data["project"]), str(t_data["goodnum1"]),
                        str(t_data["goodnum2"]))
        # flag = dr.element_exist('xpath-> //span[text()="已审核"]')
        # assert flag
        add_image(dr, "主材采购申请")

    @allure.story("创建劳务采购申请")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_create_lw_apply(self, login_admin):
        dr = login_admin
        # t_data = {
        #     'casename': '劳务采购申请',
        #     'applytype': '2.2',
        #     'project': '21010004',
        #     'cost': 'cost-type-002.001.001_1_1',
        #     'part': '000001',
        #     'nature': '000001',
        #     'quantities': '1000',
        #     'quantities1': '2000',
        #     'goodnum1': '10',
        #     'goodnum2': '20'
        # }
        t_data = datainfo.get_xls_to_dict("planapply.xlsx", "Sheet1")["劳务采购申请"]
        ua = planapplyaction.CreatePlanApplyAction(dr)
        ua.create_apply_lw(str(t_data["applytype"]), str(t_data["project"]), str(t_data["quantities"]),
                           str(t_data["quantities1"]),
                           str(t_data["goodnum1"]),
                           str(t_data["goodnum2"]),
                           str(t_data["cost"]), str(t_data["part"]), str(t_data["nature"]))
        # flag = dr.element_exist('xpath-> //span[text()="已审核"]')
        # assert flag
        add_image(dr, "劳务采购申请")


if __name__ == "__main__":
    pytest.main(["-s", "test_001_create_planApply.py"])
