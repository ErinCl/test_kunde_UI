#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/02/26
# @Author  : chenlin
# @Site    :
# @File    : test_001_create_planAppply.py
# @Software: PyCharm


import pytest
from public.common import datainfo
from public.appmodel import expendContractAction
from public.pages import expendContractPage
from public.common.publicfunction import *


@allure.feature("创建主材采购合同")
class TestCreateContract():
    '''创建主材采购合同'''

    @allure.story("创建主材采购合同")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_create_zc_contract(self, login_admin):
        dr = login_admin
        t_data = {'casename': '主材采购申请',
                  'pricing_type': '2.0',
                  'project': '21010004',
                  'contract_officer': '测试甲方',
                  'supplier': 'SUP-20201022-0001',
                  'pricing_id': 'HTDJ-20210208-0001',
                  'main_content': '010002',
                  'contract_explain': '合同说明',
                  'payment_type': '付款方式'
                  }
        ua = expendContractAction.CreateExpendContractAction(dr)
        ua.create_expend_contract(str(t_data["pricing_type"]), str(t_data["project"]), str(t_data["contract_officer"]),
                                  str(t_data["supplier"]),
                                  str(t_data["pricing_id"]), str(t_data["main_content"]),
                                  str(t_data["contract_explain"]), str(t_data["payment_type"])
                                  )


if __name__ == "__main__":
    pytest.main(["-s", "test_003_create_expend_contract.py"])
