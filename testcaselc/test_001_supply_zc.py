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
from public.appmodel import ContractPricingAction
from public.pages import ContractPricingPage


@allure.feature("供应链采购流程")
class TestCreateApply():
    '''供应链采购流程'''

    @allure.story("供应链采购流程")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_create_zc_apply(self, login_admin):
        dr = login_admin
        dj_data = {
            'casename': '合同定价',
            'applytype': '1.2',
            'project': '21010004'
        }
        t_data = datainfo.get_xls_to_dict("planapply.xlsx", "Sheet1")["主材采购申请"]
        ua = planapplyaction.CreatePlanApplyAction(dr)
        ua.create_apply(str(t_data["applytype"]), str(t_data["project"]), str(t_data["goodnum1"]),
                        str(t_data["goodnum2"]))
        dj = ContractPricingAction.ContractPricingAction(dr)
        dj.create_pricing(str(dj_data["applytype"]), str(dj_data["project"]))

        # flag = dr.element_exist('xpath-> //span[text()="已审核"]')
        # assert flag

        add_image(dr, "主材采购申请")


if __name__ == "__main__":
    pytest.main(["-s", "test_001_supply_zc.py"])
