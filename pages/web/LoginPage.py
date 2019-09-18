"""登陆页面"""
from common.basePage import BasePage
from common.baseTest import BaseTest

class LoginPage(BasePage):
    # 封装的方法传的时候 元组
    username = ('id', 'login-username')

    pwd = ('id', 'login-password')
    # 获取验证码
    getCodeBtn = ('id', 'login-code')

    verfiy_code = ('id', 'login-verification-code')

    loginBtn = ('id', 'login-submit')

    sucText = ('xpath', '/html/body/div/div[1]/section[1]/h1')

    def copa_login(self, usname, passwd, code):
        baseTest = BaseTest()
        self.get(baseTest.get_copa_url())
        self.sendKeys(self.username, usname)
        self.sendKeys(self.pwd, passwd)
        self.click(self.getCodeBtn)
        self.sendKeys(self.verfiy_code, code)
        self.click(self.pwd)
        self.click(self.loginBtn)

    def is_login_suc(self):
        if self.get_text(self.sucText) == "首页":
            return True
        else:
            return False
