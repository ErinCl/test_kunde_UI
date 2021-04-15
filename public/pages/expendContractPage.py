# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 16:04
# @Author  : chenlin
# @Site    :
# @File    : planApplyPage.py
# @Software: PyCharm


from public.pages import basepage
from time import sleep


class expendContractPage(basepage.Page):

    def click_use_button(self):
        '点击应用'
        self.dr.click("xpath-> //*[@id='flexpanelap']/div[3]/div/div[2]/div[1]")
        # self.dr.click('xpath-> //*[text()=]')

    def move_use_scroll_bar(self):
        '滑动应用滚动条'
        self.dr.js("document.getElementsByClassName('_1uIyPNat Ww32GbIl _3yukbAjt _3csOpDHD')[1].scrollTop=5500")

    def click_good_button(self):
        "点击物资管理"
        self.dr.click(
            "xpath-> //*[@title='合同签订、结算、变更、收付款、资金计划等']")

    def click_sidebar_button(self):
        "鼠标移动到侧边栏"
        self.move_to_el_icon("xpath-> //*[@id='flexpanelap']/div[1]/div/div[3]/i")
        self.log.debug("点击合同列表")
        self.dr.click("xpath-> //li[@title='合同列表']/span")

    def click_create_button(self):
        # 先点一下框架移开遮挡页面的菜单
        self.dr.click("xpath-> //*[@id='flexpanelap1']")
        sleep(0.5)
        # 点击新增按钮
        self.log.debug("点击新增合同列表")
        self.dr.click("xpath-> //*[@id='tblnew']/span/span")

    def input_purchase_type(self, value):
        "填写采购类型"
        self.dr.type_and_enter('xpath-> //*[@id="kdzl_purchasetype"]/div[2]/div/div[1]/input', value)

    def input_project(self, value):
        "填写工程项目"
        self.dr.type_and_enter('xpath-> //*[@id="project"]/div[2]/div/div[1]/input', value)

    def intput_owner_representative(self, value):
        "填写甲方代表"
        self.dr.type_and_enter('xpath-> //*[@id="kdzl_partylinkman"]/div[2]/input', value)

    def input_supplier_name(self, value):
        "填写供应商名称"
        self.dr.type_and_enter('xpath-> //*[@id="partb"]/div[2]/div/div[1]/input', value)

    def click_pricing_num(self):
        "选择定价单"
        self.dr.click('xpath-> //*[@id="kdzl_priceorder"]/div[2]/div/div[2]')
        sleep(1)
        self.dr.click(
            'xpath-> /html/body/div[10]/div/div[2]/div/div/div[3]/div[1]/div[2]/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/div/div')
        # self.dr.js_click('')
        sleep(1)
        self.dr.click('xpath-> //*[@id="btnok"]/span')

    def input_contract_content(self, value):
        '输入合同内容'
        self.dr.type_and_enter('xpath-> //*[@id="kdzl_lwcontent"]/div[2]/div/div[1]/input', value)

    def input_contract_explain(self, value):
        '输入合同说明'
        self.dr.type_and_enter('xpath-> //*[@id="description"]/div[2]/div/textarea', value)

    def input_payment_type(self, value):
        '输入付款方式'
        self.dr.type_and_enter('xpath-> //*[@id="kdzl_payinfo"]/div[2]/div/textarea', value)

    def click_good_detail(self):
        '选择物料明细'
        self.dr.click('xpath-> //*[@id="kdzl_selectentry"]/span')

    def click_pricing_detail(self):
        '选择劳务明细'
        self.dr.click(
            'xpath-> /html/body/div[11]/div/div[2]/div/div/div[3]/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div/div[2]/div')
        self.dr.click('xpath-> //*[@id="btnok"]/span')

    def input_contract_zip(self,value):
        "上传预审附件"
        self.dr.type('xpath-> //*[@id="kdzl_preparefile"]/div[1]/div/input',value)

    def click_submit_button(self):
        '提交预审'
        self.dr.click('xpath-> //*[@id="kdzl_baritemap1"]/span[1]/span')
        self.dr.click("xpath-> //*[@title='合同预审']")
