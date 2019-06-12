from allure import MASTER_HELPER as helper
from pages.noticePage import NoticePage
from pages.LoginPage import LoginPage
from selenium import webdriver
import pytest
@helper.feature("快讯通知")
class TestNotice:
    @helper.step('添加公告登陆')
    def setup(self):
        self.driver = webdriver.Chrome()
        login_Page = LoginPage(self.driver)
        login_Page.copa_login('meijin.hou', 'CA888888', '123456')
        self.notice_page = NoticePage(self.driver)
    @helper.testcase("添加公告")
    def test_notice(self):
        self.notice_page.click_menu()
        self.notice_page.add_notice('标题标题标题','内容内容尼尔内容')
        assert self.notice_page.is_add_suc('标题标题标题1')

    @helper.step("公告清除")
    def teardown(self):
        self.driver.quit()
        print("推出")
if __name__ == '__main__':
    pytest.main(['-s', 'test_notice.py'])