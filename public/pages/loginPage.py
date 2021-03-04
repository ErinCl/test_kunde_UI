# coding=utf-8

import allure
from public.pages import basepage
from config import globalparam


class LoginPage(basepage.Page):

    @allure.step("打开苍穹登录页面")
    def into_cmp_page(self):
        """打开苍穹首页"""
        self.log.debug("打开苍穹登录页面")
        self.dr.open(globalparam.url)

    def input_username(self, values):
        """输入用户名"""
        self.log.debug("输入用户名")
        self.dr.clear_type("xpath -> //*[@id='root']/div/div[2]/div[4]/div/div[3]/div[2]/div[2]/input", values)

    def input_password(self, values):
        """输入密码"""
        self.log.debug("输入密码")
        self.dr.clear_type("xpath -> //*[@id='root']/div/div[2]/div[4]/div/div[3]/div[3]/div[2]/input", values)

    def input_code(self, valuses):
        """
        输入验证码
        :param valuses:
        :return:
        """
        self.log.debug("输入验证码")
        self.dr.clear_type("xpath -> //input[@name='captcha']", valuses)

    def click_loginbutton(self):
        '''
        单击登录按钮
        :return:
        '''''
        self.log.debug("单击登录按钮")
        self.dr.click("xpath -> //*[@id='root']/div/div[2]/div[4]/div/div[4]/button")

    def click_usenbutton(self):
        '''
        单击应用按钮
        :return:
        '''
        self.log.debug("单击应用按钮")
        self.dr.click("xpath -> //*[@id='flexpanelap']/div[3]/div[1]/div[2]/div[1]")

    def click_materialsbutton(self):
        '''
        单击物资管理
        :return:
        '''
        self.log.debug("单击物资管理")
        self.dr.click(
            "xpath -> //*[@id='b4b7736667d142c7990a93a48b1dd7e8']/div/div/div/div[2]/div/div/div[14]/div/div[2]/div[12]/div[4]/div[1]")

    def click_applybutton(self):
        '''
        单击采购申请
        :return:
        '''
        self.log.debug('单击采购申请')
        self.dr.click("xpath -> //*[@id='kd-theme']/ul/li/div/span")
