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
        sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
