# -*- coding: utf-8 -*-
import unittest,time
import os
from WebPage import RateManagePage
from common import Configuration as cc
from common.LoginAction import LoginAction
from common.ScreenShots import ScreenShots as ss
import sre
from __builtin__ import str
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

class RateManage(unittest.TestCase):
    u"""汇率管理测试"""
      
    @classmethod
    def setUpClass(cls):
        cls.am=RateManagePage.AddRatePage()
        cls.driver=cls.am.get_driver()
        cls.loginmanager=LoginAction()
        cls.loginmanager.login_manager(cls.driver)                            
        cls.url=cc.baseUrl()+cls.am.url1
        
        
          
    @classmethod
    def tearDownClass(cls):
        cls.am.close_driver()    

    def test_01(self):
          
        u"""打开汇率页面"""       
        self.am.openMMPage(self.url)
        time.sleep(2)
        assert (u"汇率管理" in self.am.page_title())
        
    
    def test_02(self):
         
        u"""新增汇率""" 
        self.am.click_add()
        time.sleep(2)       
        '''for currencytype in currency_list:
            self.am.setCurrency()
            self.am.click_submit()
            time.sleep(0.5)                    
            if self.am.currency_dup().decode('utf-8')== u'货币已存在':
                currencytype=currencytype+1
            else:break'''
        str1=self.am.select_currency()
        self.am.click_submit()
        time.sleep(0.5)           
        if self.am.currency_dup()== u'该货币已存在':
            print (u'该货币已存在，不可再次添加') 
        else:
            self.am.select_enable()
            self.am.set_currency_rate()
            self.am.select_update_type()
            self.am.click_submit()
            #assert self.am.confirm().decode('utf-8')==u'添加成功'
        #WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(locator))
        
                  
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()