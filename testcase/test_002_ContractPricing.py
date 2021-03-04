#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021年2月25日13:34:43
# @Author  : Dannaliu
# @Site    :
# @File    : ContractPricingAction.py
# @Software: PyCharm


import pytest
from public.common import datainfo
from public.appmodel import ContractPricingAction
from public.pages import ContractPricingPage
from public.common.publicfunction import *


@allure.feature("合同定价")
class TestContractPricing():
    '''合同定价'''

    @allure.story("创建合同定价")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_create_price(self, login_admin):
        dr = login_admin
        t_data = {
            'casename': '合同定价',
            'applytype': '1.2',
            'project': '21010004'
        }
        # t_data = datainfo.get_xls_to_dict("planapply.xlsx", "Sheet1")["合同定价"]
        upage = ContractPricingPage.ContractPricingPage(dr)
        ua = ContractPricingAction.ContractPricingAction(dr)
        ua.create_pricing(str(t_data["applytype"]), str(t_data["project"]))
        # add_image(dr, "合同定价")


if __name__ == "__main__":
    pytest.main(["-s", "test_002_ContractPricing.py"])
