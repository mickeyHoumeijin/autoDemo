import pytest
# 一个测试类种创建多个测试用例
from allure import MASTER_HELPER as helper
from pages.web.BaiduPage import BaiduPage
import time
from common.baseTest import BaseTest
@helper.feature("Copa登陆")
class TestBaidu:

    def setup(self):
        print("初始化")
        self.driver = self.driver = BaseTest().get_web_driver()
        self.baidu = BaiduPage(self.driver)

    def test_login(self):
        self.baidu.open_baidu()
        assert True

    def teardown(self):
        self.driver.quit()
        time.sleep(2)
        print("推出")


if __name__ == '__main__':
    pytest.main(['-s', 'test_baidu.py'])
# python3 -m pytest test_login.py
# pytest.main(['-s', '-q', '--alluredir', './reports/xml'])
