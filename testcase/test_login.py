import pytest
# 一个测试类种创建多个测试用例
from allure import MASTER_HELPER as helper
from pages.LoginPage import LoginPage
from selenium import webdriver
import csv

@helper.feature("Copa登陆")
class TestLogin:

    @helper.step("初始化操作")
    def setup(self):
        print("初始化")
        self.driver = webdriver.Chrome()
        self.loginPage = LoginPage(self.driver)
    @helper.testcase("测试用例1")
    def test_login(self):
        list = []
        my_file = csv.reader(open('/Users/houmj/Documents/py_workplace/data/login_data.csv', 'r', encoding='utf-8'))
        for data in my_file:
            list.append(data)
        print(list[1][0]+list[1][1]+list[1][2])
        self.loginPage.copa_login(list[1][0], list[1][1], list[1][2])
        assert self.loginPage.is_login_suc()

    @helper.step("清除")
    def teardown(self):
        self.driver.quit()
        print("推出")


if __name__ == '__main__':
    # pytest.main(['-s', 'test_login.py'])
    # python3 -m pytest test_login.py
    pytest.main(['-s', '-q', '--alluredir', './reports/xml'])
