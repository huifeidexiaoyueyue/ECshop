'''
Created on 2019年6月28日
本模块 实现 需要2次封装的 公共方法
@author: Administrator
'''
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException,NoSuchWindowException
import time

def mySwichToAlert(driver, wait=10,poll=0.5):
    maxcount = wait//poll
    i = 0
    while i < maxcount:
        try:
            myalert = driver.switch_to.alert
        except NoAlertPresentException:
            i += 1
            time.sleep(poll)
            continue
        else:
            return myalert
    else:
         raise  NoAlertPresentException()
# 封装 元素识别的 "显式等待"方法
def myFindElement(driver,BY, value,sec,poll=0.5):
    i = 0
    while i < sec/poll:   # 循环次数为： 等待秒数 除以尝试周期
        try:
            el1 = driver.find_element(BY,value)
        except (NoSuchElementException,NoSuchWindowException) :
            time.sleep(poll)  #每隔  一定时间 再次尝试 定位元素。
            i += 1
            continue
        else:   # 找到元素  没有发生异常 则执行该  else分支。
            return el1
    raise NoSuchElementException()    #  如果超过等待时间  则仍然抛出 "无法识别元素的异常"
        
# 以下将所有find_element方法 二次封装为 支持显示等待的方法
def find_element_by_link_text(driver,value,wait=2,poll=0.5):
    i = 0
    exceptionType = None
    while i<wait//poll:
        try:
            eleobj = driver.find_element_by_link_text(value)
        except  Exception as e:
            i += 1
            time.sleep(poll)
            exceptionType =e
            continue          
        else:
            return eleobj
    else:
        raise exceptionType   
    