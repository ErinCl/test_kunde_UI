# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 16:04
# @Author  : chenlin
# @Site    :
# @File    : planApplyPage.py
# @Software: PyCharm


from public.pages import basepage
from config import globalparam


class planApplyPage(basepage.Page):

    # def open_url(self):
    #     self.dr.open(globalparam.url)

    def click_use_button(self):
        '点击应用'
        self.dr.click("xpath-> //*[@id='flexpanelap']/div[3]/div/div[2]/div[1]")

    def move_to_window_jz(self):
        "移动到建筑项目云"
        self.dr.js("document.getElementsByClassName('_1uIyPNat Ww32GbIl _3yukbAjt _3csOpDHD')[1].scrollTop=5500")

    def click_good_button(self):
        "点击物资管理"
        self.dr.click(
            "xpath-> //*[@title='物资计划、采购、出入库、成本核算']")

    def click_sidebar_button(self):
        "点击侧边栏"
        self.dr.move_to_element("xpath-> //*[@id='flexpanelap']/div[1]/div/div[14]")

    def click_plan_button(self):
        "点击需用计划"
        self.dr.click("xpath-> //*[@id='flexpanelap']/div[1]/div[2]/div/div[3]")

    def click_apply_button(self):
        "点击采购申请"
        self.dr.click("xpath-> //*[@id='kd-theme']/ul/li/div")

    def click_create_apply_button(self):
        "点击新增"
        self.dr.js_click("#tblnew > span > span")
        # self.dr.move_to_element("xpath->//*[@id='tblnew']/span")

    def click_applytype(self):
        "点击输入框"
        self.dr.click("xpath-> //*[@id='kdzl_fpurchasetype']/div[2]/div/div[1]")

    def input_applytype(self, value):
        "填写采购类型"
        self.dr.type_and_enter("xpath-> //*[@id='kdzl_fpurchasetype']/div[2]/div/div[1]/input", value)

    def input_project(self, value):
        "填写工程项目"
        self.dr.type_and_enter("xpath-> //*[@id='project']/div[2]/div/div[1]/input", value)

    def move_scroll_bar(self):
        "滚动条下拉"
        self.dr.js(
            "document.getElementsByClassName('_1uIyPNat Ww32GbIl _1dgLl0oE _3CPzcXVZ _3csOpDHD _3rOkwVR1 _21KqN25A')[0].scrollTop=10000")

    def click_add_button(self):
        "点击物料新增按钮"
        self.dr.click("xpath->//*[@id='kdzl_advconbaritemap2']")

    def click_add_labour_button(self):
        "点击劳务明细新增"
        self.dr.js_click("#kdzl_openmodel > span")

    def click_cost_name(self):
        "点击劳务输入框"
        self.dr.click(
            "xpath-> //*[@id='kdzl_purapply_laborentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[4]/div")

    def click_goods_button(self):
        "点击主材物资"
        self.dr.click(
            "xpath-> //*[@id='kdzl_monthrequireentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div")

    def click_good_lw_glass(self):
        "点击放大镜"
        self.dr.click(
            "xpath-> //*[@id='kdzl_purapply_laborentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[4]/div/div/div[2]")

    def click_good_glass(self):
        "点击材料放大镜"
        self.dr.click(
            "xpath-> //*[@id='kdzl_monthrequireentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div/div/div[2]")

    def click_good_id1(self):
        "点击商品ID"
        self.dr.click(
            "xpath->//*[@id='gridview']/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div")

    def click_down_drop(self):
        "点击下拉框"
        self.dr.click("xpath-> //*[@id='treeview']/ul/li/ul/li[1]/a/i")

    def click_down_drop_sr(self):
        "点击水泥物料下拉框"
        self.dr.click("xpath-> //*[@id='treeview']/ul/li/ul/li[1]/ul/li[1]/a/i")

    def click_good_szsr(self):
        "点击散装水泥"
        self.dr.click("xpath-> //*[@id='treeview']/ul/li/ul/li[1]/ul/li[1]/ul/li[1]/a")

    def click_good_id2(self):
        "点击物资：水泥"
        self.dr.click(
            "xpath-> //*[@id='gridview']/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[2]/div/div/div")

    def click_lw_good_id(self):
        "点击劳务编码ID"
        self.dr.click(
            "xpath-> //*[@id='listgridviewap1']/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[1]/div/div/div")

    def click_lw_good_id2(self):
        "点击劳务编码ID2"
        self.dr.click(
            "xpath-> //*[@id='listgridviewap1']/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div/div/div")

    def click_confirm_button(self):
        "点击确定"
        self.dr.js_click("#btnok > span")

    def click_good_num1(self):
        "点击数量输入框"
        self.dr.click(
            "xpath-> //*[@id='kdzl_monthrequireentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[6]/div/div/div")

    def input_good_num1(self, value):
        "输入数量1"
        self.dr.type_and_enter(
            "xpath-> //*[@id='kdzl_monthrequireentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[6]/div/div/input",
            value)

    def click_good_num2(self):
        self.dr.click(
            "xpath-> //*[@id='kdzl_monthrequireentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[6]/div/div/div")

    def input_good_num2(self, value):
        "输入数量2"
        self.dr.type_and_enter(
            "xpath-> //*[@id='kdzl_monthrequireentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div[6]/div/div/input",
            value)

    def input_cost_name(self, value):
        "输入费用名称"
        self.dr.type_and_enter(
            "xpath->//*[@id='kdzl_purapply_laborentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[4]/div/div/div[1]/input",
            value)

    def click_part_id(self):
        "点击部位输入框"
        self.dr.click(
            "xpath-> //*[@id='kdzl_purapply_laborentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[5]/div")

    def click_nature_id(self):
        # 点击合同性质
        self.dr.click(
            "xpath-> //*[@id='kdzl_purapply_laborentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[6]/div")

    def click_quantities_num(self):
        # 点击工程量
        self.dr.click(
            'xpath-> //*[@id="kdzl_purapply_laborentry"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div')

    def input_quantities_num(self, value):
        # 输入工程量
        self.dr.type_and_enter(
            'xpath-> //*[@id="kdzl_purapply_laborentry"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div/div/input',
            value)

    def click_equitment_num(self):
        # 输入设备数量
        self.dr.click(
            'xpath-> //*[@id="kdzl_purapply_laborentry"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[3]/div')

    def input_equitment_num(self, value):
        self.dr.type_and_enter(
            'xpath-> //*[@id="kdzl_purapply_laborentry"]/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[3]/div/input',
            value)

    def input_part_id(self, value):
        # 输入部位名称ID
        self.dr.type_and_enter(
            "xpath-> //*[@id='kdzl_purapply_laborentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[5]/div/div/div[1]/input",
            value)

    def input_nature_id(self, value):
        # 输入合同性质ID
        self.dr.type_and_enter(
            "xpath-> //*[@id='kdzl_purapply_laborentry']/div/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div/div[6]/div/div/div[1]/input",
            value)

    def move_drop_right(self):
        "滚动条右拉"
        self.dr.js("document.getElementsByClassName('ag-body-horizontal-scroll-viewport')[1].scrollLeft=1000")

    def click_good_sumbit(self):
        "点击提交"
        self.dr.js_click("#bar_submit > span")

    def click_audit_button(self):
        '点击审核'
        self.dr.js_click("#bar_audit > span")

    def click_quit_button(self):
        "点击退出"
        self.dr.js_click("#bar_close > span")

    def move_good_button(self):
        self.dr.move_to_element("xpath-> //*[@id='flexpanelap']/div[3]/div[3]/div")

    def close_good_button(self):
        self.dr.click('xpath-> //*[@id="flexpanelap"]/div[3]/div[3]/div/div[2]/i[1]')
