import pytest
# 一个测试类种创建多个测试用例
from allure import MASTER_HELPER as helper
from pages.web.LoginPage import LoginPage
import time
from common.baseTest import BaseTest
@helper.feature("Copa登陆")
class TestLogin:

    def setup(self):
        print("初始化")
        # Linux上运行必须加
        '''chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome("/root/chromedriver",chrome_options=chrome_options)'''
        self.driver = BaseTest().get_web_driver()
        self.loginPage = LoginPage(self.driver)

    @helper.testcase("copa-login")
    def test_login(self):
        list = []
        # my_file = csv.reader(open('/Users/houmj/Documents/py_workplace/data/login_data.csv', 'r', encoding='utf-8'))
        # for data in my_file:
        #     list.append(data)
        # print(list[1][0]+list[1][1]+list[1][2])
        # self.loginPage.copa_login(list[1][0], list[1][1], list[1][2])
        self.loginPage.copa_login("meijin.hou", "CA888888", "123456")
        assert self.loginPage.is_login_suc()

    @helper.step("login quit")
    def teardown(self):
        self.driver.quit()
        time.sleep(2)
        print("推出")


if __name__ == '__main__':
     pytest.main(['-s', 'test_login.py'])
    # python3 -m pytest test_login.py
    #pytest.main(['-s', '-q', '--alluredir', './reports/xml'])
