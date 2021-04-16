#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/02/26
# @Author  : chenlin
# @Site    :
# @File    : test_003_create_planAppply.py
# @Software: PyCharm


import pytest
from public.common import datainfo
from public.appmodel import expendContractAction
from public.pages import expendContractPage
from public.common.publicfunction import *


@allure.feature("创建主材采购合同")
class TestCreateContract():
    '''创建采购合同'''

    @allure.story("创建主材采购合同")
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_create_zc_contract(self, login_admin):
        dr = login_admin
        # t_data = {'casename': '主材采购合同',
        #           'pricing_type': '1.0',
        #           'project': '21010004',
        #           'contract_officer': '测试甲方',
        #           'supplier': 'SUP-20201016-0001',
        #           'pricing_id': 'HTDJ-20210310-0004',
        #           'main_content': '010002',
        #           'contract_explain': '合同说明',
        #           'payment_type': '付款方式',
        #           'compress_zip': r'C:\Users\admin\Desktop\应收.txt'
        #           }
        t_data = datainfo.get_xls_to_dict("contract.xlsx", "Sheet1")["主材采购合同"]
        ua = expendContractAction.CreateExpendContractAction(dr)
        ua.create_expend_contract(str(t_data["pricing_type"]), str(t_data["project"]), str(t_data["contract_officer"]),
                                  str(t_data["supplier"]),
                                  str(t_data["main_content"]),
                                  str(t_data["contract_explain"]),
                                  str(t_data["payment_type"]),
                                  str(t_data["compress_zip"]))

    @allure.story('创建劳务合同')
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_create_lw_contract(self, login_admin):
        dr = login_admin
        t_data = datainfo.get_xls_to_dict("contract.xlsx", "Sheet1")["劳务采购合同"]
        ua = expendContractAction.CreateExpendContractAction(dr)
        ua.create_expend_lw_contract(str(t_data["purchase_type"]), str(t_data["project"]),
                                     str(t_data["contract_officer"]),
                                     str(t_data["supplier"]),
                                     str(t_data["main_content"]),
                                     str(t_data["contract_explain"]),
                                     str(t_data["payment_type"]),
                                     str(t_data["compress_zip"]))


    @allure.story('审核预审合同')
    @pytest.mark.flaky(reruns=globalparam.RENUM)
    def test_audit_contract(self,login_admin):
        dr=login_admin
        ua = expendContractAction.CreateExpendContractAction(dr)



if __name__ == "__main__":
    pytest.main(["-s", "test_003_create_expend_contract.py"])
