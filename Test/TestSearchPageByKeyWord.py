import unittest
from selenium import webdriver
from AutomationTest.POM.SearchPage import SearchPage

from AutomationTest.Utils.readJson import readJSON

# 百度搜索测试



class TestSearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/zhouyueyang/Downloads/chromedriver")

    def testSearch(self):
        driver = self.driver
        driver.implicitly_wait(10)

        searchPageTestData = readJSON("../Case/searchPage.json")

        # 百度网址
        url = searchPageTestData["search"]["search_url"]
        # 搜索文本
        text = searchPageTestData["search"]["search_text"]

        # 断言，期望验证的标题
        assert_title = searchPageTestData["search"]["assert_title"]

        search_Page = SearchPage(driver, url)

        # 调用搜索关键字，完成搜索功能
        search_Page.search_keyword(text)

        # 验证标题
        self.assertEqual(search_Page.get_hot_search_title(), assert_title)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
