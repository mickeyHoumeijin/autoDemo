from selenium import webdriver
import pytest
from common import logger
from common import readYaml


class BaseTest(object):
    def __init__(self):
        self.logger = logger.Logger().getLogger()

    def get_web_driver(self):
        with pytest.allure.step("Launch site"):
            # 读取配置文件，browser
            dit = readYaml.read("testcase.yaml")
            browser = dit['browser']
            if browser == "firefox" or browser == "Firefox":
                self.driver = webdriver.Firefox()
            elif browser == "chrome" or browser == "Chrome":
                # options = webdriver.ChromeOptions()
                # options.add_extension('./uBlock_1_22_2_0.crx')
                # self.driver = webdriver.Chrome(chrome_options=options)
                self.driver = webdriver.Chrome()

            else:
                self.logger.error("Wrong browser arguement.")

            self.logger.info("new browser driver ")
            return self.driver

    def get_wap_driver(self):
        with pytest.allure.step("Launch site"):
            # 读取配置文件，browser
            dit = readYaml.read("testcase.yaml")
            browser = dit['browser']
            if browser == "firefox" or browser == "Firefox":
                # mobileEmulation = {'deviceName': 'Apple iPhone 6s'}
                # options = webdriver.FirefoxOptions()
                # options.add_argument('mobileEmulation', mobileEmulation)
                self.driver = webdriver.Firefox()
                return self.driver
            elif browser == "chrome" or browser == "Chrome":
                mobileEmulation = {'deviceName': 'Galaxy S5'}
                options = webdriver.ChromeOptions()
                options.add_experimental_option('mobileEmulation', mobileEmulation)
                self.driver = webdriver.Chrome(chrome_options=options)
                return self.driver
            self.logger.info("new wap driver ")

    def get_copa_url(self):
        # 读取配置文件，url
        dit = readYaml.read("urls.yaml")
        copaUrl = dit['copaUrl']
        return copaUrl

    def get_baidu_url(self):
        # 读取配置文件，url
        dit = readYaml.read("urls.yaml")
        baiduUrl = dit['baiduUrl']
        return baiduUrl

    def get_mobile_url(self):
        # 读取配置文件，url
        dit = readYaml.read("urls.yaml")
        mobileUrl = dit['mobileUrl']
        return mobileUrl
