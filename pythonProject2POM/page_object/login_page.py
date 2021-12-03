
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    # 页面url
    url= 'http://www.tianqiapi.com/user/login'
    # 页面关联的核心元素:基于定位方法+定位值进行元素定位
    username = (By.NAME, 'username')
    password = (By.NAME, 'password')
    button = (By.XPATH, '/html/body/div[1]/div/table/tbody/tr/td[1]/div[2]/form/div[3]/button')
    # 页面关联的业务

    def login(self, usr, pwd):
        self.open(self.url)
        self.input(self.username, usr)
        self.input(self.password, pwd)
        self.click(self.button)

# 调式代码
# if __name__ == '__main__':
#     driver = webdriver.Chrome('D:\Webtest\chromedriver.exe')
#     lp = LoginPage(driver)
#     usr = 'qingyue17@outlook.com'
#     pwd='ASD0421.'
#     lp.login(usr, pwd)
