import unittest
import os
from time import sleep
from selenium import webdriver
from os.path import dirname,abspath
from selenium.common.exceptions import NoSuchElementException

class addNewGoods(unittest.TestCase):
    '''新增商品流程'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'http://192.168.13.129/ecshop/admin'
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(15)
        self.driver.set_script_timeout(10)
        self.driver.maximize_window()
        sleep(5)

    def test_something(self):

        driver = self.driver
        # 打开登陆页面，完成登录
        driver.get(self.base_url)
        driver.find_element_by_name('username').send_keys('admin')
        driver.find_element_by_name('password').send_keys('admin123456')
        driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/input').click()
        sleep(5)
        # 切换到列表框架，增加商品
        driver.switch_to.frame('menu-frame')
        driver.find_element_by_link_text('商品列表').click()
        #先切换到顶层框架。然后切换到需要编辑的框架
        driver.switch_to.default_content()
        driver.switch_to.frame('main-frame')
        #点击新增商品
        driver.find_element_by_link_text('添加新商品').click()
        #由于当前页面会刷新，所以先切回顶层框架
        driver.switch_to.default_content()
        sleep(5)
        driver.switch_to.frame('main-frame')
        #1.输入商品通用基本信息
        #输入商品名称
        driver.find_element_by_name('goods_name').send_keys('洗衣机1')
        # 输入商品货号
        driver.find_element_by_name('goods_sn').send_keys('123456789')
        # 商品分类
        driver.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[3]/td[2]/select').click()
        driver.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[3]/td[2]/select/option[2]').click()
        # 商品品牌
        driver.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[5]/td[2]/select').click()
        driver.find_element_by_xpath('//*[@id="general-table"]/tbody/tr[5]/td[2]/select/option[2]').click()
        # driver.find_element_by_link_text('添加品牌').click()
        # #输入品牌名
        # driver.find_element_by_name('addedBrandName').send_keys('海尔')
        # #点击确定按钮
        # driver.find_element_by_xpath('//*[@id="brand_add"]/a[1]').click()
        sleep(5)
        #清空价格
        send_jiage = driver.find_element_by_name('shop_price')
        send_jiage.clear()
        send_jiage.send_keys('5000')
        sleep(5)
        #2.详细描述
        driver.find_element_by_id('detail-tab').click()
        bianjikuang = driver.find_element_by_id('goods_desc___Frame')
        driver.switch_to.frame(bianjikuang)
        editTextAreaFrame = driver.find_element_by_xpath('//*[@id="xEditingArea"]/iframe')
        driver.switch_to.frame(editTextAreaFrame)
        #输入详细描述
        send_miaoshu=driver.find_element_by_tag_name("body")
        send_miaoshu.click()
        send_miaoshu.send_keys('测试商品描述******')
        #3.设置商品属性，点击“商品属性”选择类型为“家用电器”，并给商品添 两个“颜色”属性 ，分别填写值为 “白色”--属性价格10 , “红色”---属性价格20
        #切回顶层框架
        driver.switch_to.default_content()
        #切换到属性框架
        driver.switch_to.frame('main-frame')
        #点击商品属性
        driver.find_element_by_id('properties-tab').click()
        sleep(1)
        #选择商品类型是家用电器
        driver.find_element_by_xpath('//*[@id="properties-table"]/tbody/tr[1]/td[2]/select/option[11]').click()
        #“白色”--属性价格10
        driver.find_element_by_xpath('//*[@id="attrTable"]/tbody/tr/td[2]/select/option[2]').click()
        driver.find_element_by_xpath('//*[@id="attrTable"]/tbody/tr/td[2]/input[2]').send_keys(10)
        #添加属性
        driver.find_element_by_xpath('//*[@id="attrTable"]/tbody/tr/td[1]/a').click()
        #“红色”---属性价格20
        driver.find_element_by_xpath('//*[@id="attrTable"]/tbody/tr[2]/td[2]/select/option[3]').click()
        driver.find_element_by_xpath('//*[@id="attrTable"]/tbody/tr[2]/td[2]/input[2]').send_keys(20)

        #上传图片
        #点击商品相册，给商品上传前置条件中的照片
        driver.find_element_by_xpath('//*[@id="gallery-tab"]').click()
        #添加图片描述
        driver.find_element_by_xpath('//*[@id="gallery-table"]/tbody/tr[3]/td/input[1]').send_keys('pal1')
        sleep(10)
        img_input = driver.find_element_by_xpath('//*[@id="gallery-table"]/tbody/tr[3]/td/input[2]')
        # TestImgPath = dirname(dirname(abspath(__file__))) + os.sep + 'TestDate' + os.sep + 'goodsimg' + os.sep +'ga.png'
        img_input.send_keys(r'D:\ECshop\TestData\goodsimg\ga.png')
        sleep(5)
        #点击确定
        driver.find_element_by_xpath('//*[@id="tabbody-div"]/form/div/input[2]').click()
        sleep(5)
        # 再次进入商品列表断言该商品 存在于 列表中
        driver.switch_to.default_content()
        driver.switch_to.frame('menu-frame')
        driver.find_element_by_link_text("商品列表").click()
        driver.switch_to.default_content()
        driver.switch_to.frame('main-frame')
        sleep(5)
        # try:
        actualGoodsName = driver.find_element_by_xpath("//*[@id='listDiv']/table[1]/tbody/tr[3]/td[2]/span").text
        self.assertEqual('洗衣机1',actualGoodsName, '添加商品失败。 未出现在商品列表中！！')
        # except NoSuchElementException:
        #     raise AssertionError("添加商品失败。 未出现在商品列表中！！")





    def tearDown(self):
        self.driver.quit()


# if __name__ == '__main__':
#     unittest.main()
