
class BasePage:
    # 构造函数
    def __init__(self, driver):
        self.driver = driver
    # 访问url
    def open(self, url):
        self.driver.get(url)
    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)
    # 输入
    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 点击
    def click(self, loc):
        self.locator(loc).click()