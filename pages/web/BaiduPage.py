"""登陆页面"""
from common.basePage import BasePage
from common.baseTest import BaseTest

class BaiduPage(BasePage):
    def open_baidu(self):
        baseTest = BaseTest()
        self.get(baseTest.get_baidu_url())
