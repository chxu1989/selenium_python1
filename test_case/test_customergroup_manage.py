# -*- coding: utf-8 -*-
import unittest,time
import os
from WebPage import CustomerGroupManagePage
from common import Configuration as cc
from common.LoginAction import LoginAction
from common.ScreenShots import ScreenShots as ss
import sre
from __builtin__ import str
from selenium.webdriver.common.action_chains import ActionChains   

class CustomerGroupManage(unittest.TestCase):
    u"""客户分组管理测试"""
      
    @classmethod
    def setUpClass(cls):
        cls.am=CustomerGroupManagePage.AddCuGroupPage()
        cls.driver=cls.am.get_driver()
        cls.loginmanager=LoginAction()
        cls.loginmanager.login_manager(cls.driver)                            
        cls.url=cc.baseUrl()+cls.am.url1
        
          
    @classmethod
    def tearDownClass(cls):
        cls.am.close_driver()    

    def test_01(self):
          
        u"""打开客户分组页面"""       
        self.am.openMMPage(self.url)
        time.sleep(2)
        assert (u"客户分组管理" in self.am.page_title())    
        
        
    def test_02(self):
       
        u"""新增客户分组""" 
        self.am.click_add()
        time.sleep(0.5)        
        self.am.set_name()
        self.am.select_pricetype()
        self.am.select_cutmargin()
        self.am.select_margintype()
        self.am.select_allow()
        #self.am.mouse_move()
        time.sleep(2)
        self.am.click_submit()
        
        #assert self.am.confirm()==u'新增成功'
        #print (u'客户分组名称:%'%name) 
             
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()