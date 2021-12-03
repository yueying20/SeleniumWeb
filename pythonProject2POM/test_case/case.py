import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt, file_data

from page_object.Warning import Warning
from page_object.login_page import LoginPage
from page_object.product_page import ProductPage
from page_object.Message_page import Message_page

@ddt
# 调用unitTest
class Case(unittest.TestCase):
    # 定义测试用例:必须以Test开头函数才能够被识别为测试用例
    # 使得测试用例能够在连续的执行
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('D:\Webtest\chromedriver.exe')
        cls.lp = LoginPage(cls.driver)
        cls.pp = ProductPage(cls.driver)
        cls.mp = Message_page(cls.driver)
        cls.wp = Warning(cls.driver)

    # 使得测试用例能够在连续的执行 管理测试用例
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
    @file_data('../data/login.yaml')
    def test_01(self, usr, pwd):
        self.lp.login(usr, pwd)
        sleep(2)
    def test_02(self):
        name1 = '你好'
        telnumbers2 = '100'
        address3 = '北京'
        self.pp.savemessage(name1, telnumbers2, address3)
        sleep(3)
    def test_3(self):
        title = '世界'
        taxid = '123456'
        address = '北京'
        bankname = '建设银行'
        bankno = '123'
        telnumbers = '10086'
        self.mp.savemessage2(title, taxid,  address, bankname, bankno, telnumbers)
        sleep(3)
    def test_4(self):
        PushUrl = '123'
        FreeUrl = '123'
        SafeCode = '10'
        self.wp.savemessage3(PushUrl, FreeUrl, SafeCode)
        sleep(5)



if __name__=='__main__':
    unittest.main()