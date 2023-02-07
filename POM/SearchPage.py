from selenium.webdriver.common.by import By
from AutomationTest.POM.BasePage import Page


# 百度搜索page
class SearchPage(Page):
    # 百度搜索页面的元素信息(定位元素的方式，以及对应的值)

    # 搜索输入框 元素
    search_input = (By.ID, 'kw')
    # 百度一下按钮 元素
    search_button = (By.ID, 'su')
    # 百度热搜 元素
    hot_search = (By.XPATH, '//*[@id="1"]/div/div/div[1]')

    def __init__(self, driver, base_url="https://www.baidu.com"):
        Page.__init__(self, driver, base_url)

    def openBaiduHomePage(self):
        print("打开首页: ", self.base_url)
        self.driver.get(self.base_url)

    def input_search_text(self, text="testerGuie"):
        print("输入搜索关键字：测试开发Guide")
        self.input_text(self.search_input, text)

    def click_search_btn(self):
        print("点击 百度一下  按钮")
        self.click(self.search_button)

    def get_hot_search_title(self):
        return self.get_attribute("title",self.hot_search)

    def search_keyword(self,text):

        self.openBaiduHomePage()
        self.input_search_text(text)
        self.click_search_btn()
