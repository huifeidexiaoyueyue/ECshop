import unittest
from time import sleep
from selenium import webdriver


class addDemo(unittest.TestCase):
    '''登录流程测试'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.base_url='https://www.baidu.com/'

    def test_something(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("51testing")
        driver.find_element_by_id("su").click()
        sleep(5)
        self.assertEqual("51testing_百度搜索", driver.title)
        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
