import unittest
from selenium import webdriver
from AutomationTest.POM.SearchPage import SearchPage


# 百度搜索测试
class TestSearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/zhouyueyang/Downloads/chromedriver")

    def testSearch(self):
        driver = self.driver
        driver.implicitly_wait(10)
        # 百度网址
        url = "https://www.baidu.com"
        # 搜索文本
        text = "测试开发进大厂"

        # 断言，期望验证的标题
        assert_title = "百度热搜"

        search_Page = SearchPage(driver, url)

        # 启动浏览器，访问百度首页
        search_Page.openBaiduHomePage()

        # 输入 搜索词
        search_Page.input_search_text(text)

        # 单击 百度一下 按钮进行搜索
        search_Page.click_search_btn()

        # 验证标题
        self.assertEqual(search_Page.get_hot_search_title(), assert_title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
