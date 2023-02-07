from selenium import webdriver
import time
import unittest


class TestSeach(unittest.TestCase):

    def testSeachPage(self):

        # ======测试数据 (含URL，定位元素id的值)===================
        url = "http://www.baidu.com"
        # 搜索输入框
        search_input = {"id": "kw"}
        # 百度一下 按钮
        search_button = {"id": "su"}
        # ======测试数据 (含URL，定位元素id的值)===================

        # ======定位元素以及操作 =================================

        # 启动WebDriver，地址填写本地下载的WebDriver的路径
        driver = webdriver.Chrome("/Users/zhouyueyang/Downloads/chromedriver")

        # 访问百度
        driver.get(url)
        # 定位元素，并进行相应操作
        driver.find_element("id", search_input["id"]).send_keys("测试开发学习路线通关大厂")
        driver.find_element("id", search_button["id"]).get_attribute("title")


        # 断言
        self.assertEqual(url, "http://www.baidu.com", msg="input url error!")

        # 睡眠5秒
        time.sleep(5)
        # 释放资源, 退出浏览器
        driver.quit()

        # ======定位元素以及操作 ============================


if __name__ == '__main__':
    unittest.main()
