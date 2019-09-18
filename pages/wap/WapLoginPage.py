"""登陆页面"""
from common.basePage import BasePage
from common.baseTest import BaseTest

class WapLoginPage(BasePage):
    """登陆地址"""
    url = 'http://101.200.149.181:8080/'

    def open_wap(self):
        baseTest = BaseTest()
        self.get(baseTest.get_mobile_url())
