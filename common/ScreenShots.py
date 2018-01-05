# coding:utf-8
#from selenium import webdriver
import time
class ScreenShots(object):
    u'''截图装饰器'''
    def __init__(self, driver):
        self.driver = driver
    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
                raise
        return inner
        
    
