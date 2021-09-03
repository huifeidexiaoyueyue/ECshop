# 定义静态元素 定位信息
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username_input_loc=(By.XPATH,"//form[@id='registerForm']//input[@id='username']")
email_input_loc=(By.ID,"email")
passwd_input_loc=(By.ID,"password1")
compasswd_input_loc=(By.ID,"confirm_password")
submitRegInfo_bnt_loc=(By.NAME,"Submit")

def registInfoInput_Buyflow (driver, **kwargs):
    ''' 用户名参数名：username;
        密码参数名： passwd
        email参数名  email
    '''
    driver.find_element(*username_input_loc).send_keys(kwargs["username"])
    driver.find_element(*email_input_loc).send_keys(kwargs["email"])
    driver.find_element(*passwd_input_loc).send_keys(kwargs["passwd"])
    driver.find_element(*compasswd_input_loc).send_keys(kwargs["passwd"]+Keys.TAB)
    driver.find_element(*submitRegInfo_bnt_loc).click()


if __name__ == "__main__":
    from selenium import webdriver
    dri = webdriver.Chrome()
    input("请手动操作到 购物注册界面，再回车！！！！")
    registInfoInput_Buyflow(dri,username="张三",passwd="123456",email="1234qq.com")
    time.sleep(3)
    dri.quit()