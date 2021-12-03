from time import sleep
from selenium.webdriver.common.by import By
from base.base_page import BasePage
class Message_page(BasePage):
    # 页面url
    url= 'http://www.tianqiapi.com/user/fapiao'
    # 页面关联的核心元素:基于定位方法+定位值进行元素定位
    title = (By.XPATH, '//*[@id="company"]')
    taxid = (By.XPATH, '//*[@id="num"]')
    address= (By.XPATH, '//*[@id="address"]')
    bankname = (By.XPATH, '//*[@id="bankname"]')
    bankno = (By.XPATH, '//*[@id="bankno"]')
    telnumbers = (By.XPATH, '//*[@id="email"]')
    savebutton = (By.XPATH, '//*[@id="regform"]/div[7]/div/button')
    # 页面关联的业务

    def savemessage2(self, title, taxid,  address, bankname, bankno, telnumbers):
        sleep(2)
        self.open(self.url)
        sleep(1)
        self.input(self.title, title)
        sleep(1)
        self.input(self.taxid, taxid)
        sleep(1)
        self.input(self.address, address)
        sleep(1)
        self.input(self.bankname, bankname)
        sleep(1)
        self.input(self.bankno, bankno)
        sleep(1)
        self.input(self.telnumbers, telnumbers)
        sleep(1)
        self.click(self.savebutton)

