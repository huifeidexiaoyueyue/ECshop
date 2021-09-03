import unittest
from selenium import webdriver


class addNew(unittest.TestCase):
    '''登录流程测试'''
    def setUp(self):
        self.driver = webdriver.Chrom()

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
