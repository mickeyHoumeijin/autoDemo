"""公告页面"""
from common.basePage import BasePage
import time


class NoticePage(BasePage):
    notice_title = ('id', 'id_title')
    notice_content = ('id', 'id_content')
    notice_from_time = ('id', 'id_display_start_date')
    notice_end_time = ('id', 'id_display_end_date')
    # now按钮
    now_from_btn = ('xpath', '//*[@id="ui-datepicker-div"]/div[3]/button[1]')
    now_end_btn = ('xpath', '//*[@id="ui-datepicker-div"]/div[3]/button[1]')
    submit_btn = ('xpath', '/html/body/div[1]/div[1]/section[2]/div/div/div/div/div/form/button')

    # 列表第一个记录的title
    first_title = ('xpath', '//*[@id="notification_list"]/tbody/tr[1]/td[2]')

    # 菜单-营销管理
    menu_marketing = ('id', 'mb_marketing')
    # 公告管理菜单
    menu_notice = ('xpath', '/html/body/div/aside/section/ul/li[6]/ul/li[2]/a')
    # 添加公告按钮
    add_notice_btn = ('xpath', '/html/body/div/div[1]/section[2]/div/div/div/div/div/a')

    # 点击菜单操作等
    def click_menu(self):
        self.click(self.menu_marketing)
        time.sleep(2)
        self.click(self.menu_notice)

    def add_notice(self, title, content):
        self.click(self.add_notice_btn)
        self.sendKeys(self.notice_title, title)
        self.sendKeys(self.notice_content, content)

        self.click(self.notice_from_time)
        self.click(self.now_from_btn)
        # 点击结束时间，选择当前时间
        self.click(self.notice_end_time)
        self.click(self.now_end_btn)
        self.click(self.submit_btn)

    # 添加公告
    def is_add_suc(self, title):
        # 等待加载列表
        time.sleep(2)
        title_txt = self.get_text(self.first_title)
        if title_txt == title:
            return True
        else:
            return False
