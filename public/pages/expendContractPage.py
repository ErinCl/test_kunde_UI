# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 16:04
# @Author  : chenlin
# @Site    :
# @File    : planApplyPage.py
# @Software: PyCharm


from public.pages import basepage


class expendContractPage(basepage.Page):

    def click_use_button(self):
        '点击应用'
        self.dr.click("xpath-> //*[@id='flexpanelap']/div[3]/div/div[2]/div[1]")

    def move_use_scroll_bar(self):
        '滑动应用滚动条'
        self.dr.js("document.getElementsByClassName('_1uIyPNat Ww32GbIl _3yukbAjt _3csOpDHD')[1].scrollTop=5500")

    # def click_contract_button(self):
    #     '点击合同管理'
    #     self.dr.click
