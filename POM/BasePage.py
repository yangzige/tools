# page基类
class Page(object):
    """
        Page基类，所有页面page都应该继承该类
    """

    def __init__(self, driver, base_url="http://www.baidu.com"):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def get_attribute(self, attribute, loc):
        return self.find_element(*loc).get_attribute(attribute)

    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        self.find_element(*loc).click()
