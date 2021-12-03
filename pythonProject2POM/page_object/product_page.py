from time import sleep

from selenium.webdriver.common.by import By
from base.base_page import BasePage

class ProductPage(BasePage):
    # 页面url
    url= 'http://www.tianqiapi.com/user/address'
    # 页面关联的核心元素:基于定位方法+定位值进行元素定位

    uname = (By.XPATH, '/html/body/div/div/main/div/div[1]/form/div[1]/div/input')
    telnumbers= (By.XPATH, '//*[@id="tel"]')
    address= (By.XPATH, '//*[@id="city"]')
    savebutton = (By.XPATH, '//*[@id="regform"]/div[4]/div/button')
    # 页面关联的业务

    def savemessage(self, name1, telnumbers2, address3):
        sleep(2)
        self.open(self.url)
        sleep(1)
        self.input(self.uname, name1)
        sleep(1)
        self.input(self.telnumbers, telnumbers2)
        sleep(1)
        self.input(self.address, address3)
        sleep(1)
        self.click(self.savebutton)

# # 调式代码
# if __name__ == '__main__':
#     driver = webdriver.Chrome('D:\Webtest\chromedriver.exe')
#     lp = ProductPage(driver)
#     usr = 'qingyue17@outlook.com'
#     pwd='ASD0421.'
#     lp.login(usr, pwd)
