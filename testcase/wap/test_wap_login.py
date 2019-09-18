import pytest
# 一个测试类种创建多个测试用例
from allure import MASTER_HELPER as helper
from pages.wap.WapLoginPage import WapLoginPage
from selenium import webdriver
import csv
import time
from selenium.webdriver.chrome.options import Options
from common.baseTest import BaseTest


@helper.feature("Copa登陆")
class TestWapLogin:

    def setup(self):
        print("初始化")
        self.driver = self.driver = BaseTest().get_wap_driver()
        self.waplogin = WapLoginPage(self.driver)

    def test_login(self):
        self.waplogin.open_wap()
        assert True

    def teardown(self):
        self.driver.quit()
        time.sleep(2)
        print("推出")


if __name__ == '__main__':
    pytest.main(['-s', 'test_baidu.py'])
# python3 -m pytest test_login.py
# pytest.main(['-s', '-q', '--alluredir', './reports/xml'])
