from time import sleep

from selenium.webdriver.common.by import By
from base.base_page import BasePage

class Warning(BasePage):
    # 页面url
    url= 'http://www.tianqiapi.com/user/alarm'
    # 页面关联的核心元素:基于定位方法+定位值进行元素定位
    PushUrl = (By.XPATH, '//*[@id="url"]')
    FreeUrl = (By.XPATH, '//*[@id="cancelurl"]')
    SafeCode = (By.XPATH, '//*[@id="safecode"]')
    FegForm = (By.XPATH, '//*[@id="regform"]/div[4]/div/button[1]')

    def savemessage3(self,  PushUrl, FreeUrl, SafeCode):
        sleep(2)
        self.open(self.url)
        sleep(1)
        self.input(self.PushUrl, PushUrl)
        sleep(1)
        self.input(self.FreeUrl, FreeUrl)
        sleep(1)
        self.input(self.SafeCode, SafeCode)
        sleep(1)
        self.click(self.FegForm)






