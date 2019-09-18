from allure import MASTER_HELPER as helper
from pages.web.noticePage import NoticePage
from pages.web.LoginPage import LoginPage
import pytest
import time
from common.baseTest import BaseTest
@helper.feature("快讯通知")
class TestNotice:
    @helper.step('添加公告登陆')
    def setup(self):
        self.driver = self.driver = BaseTest().get_web_driver()
        login_Page = LoginPage(self.driver)
        login_Page.copa_login('meijin.hou', 'CA888888', '123456')
        self.notice_page = NoticePage(self.driver)
    @helper.testcase("添加公告")
    def test_notice(self):
        time.sleep(3)
        self.notice_page.click_menu()
        self.notice_page.add_notice('标题标题标题','内容内容尼尔内容')
        assert self.notice_page.is_add_suc('标题标题标题')

    @helper.step("公告清除")
    def teardown(self):
        self.driver.quit()
        time.sleep(2)
        print("推出")
if __name__ == '__main__':
    pytest.main(['-s', 'test_notice.py'])