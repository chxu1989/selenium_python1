#Embedded file name: C:\Users\Administrator\eclipse-workspace\selenium_use_case\test_case\WebPages\LoginPage.py
#-*- coding:utf-8 -*-  
from BasePage import BasePage
from common.OperationFile import OperationXml
from LoginPage import LoginPage


class RateManagePage(BasePage):
    readXml=OperationXml()
    #管理员登录页面elements
    username1=readXml.ReadXml('login', 'useraccount')
    password1=readXml.ReadXml('login', 'password')
    login_btn1=readXml.ReadXml('login', 'login_btn')
    error_info1=readXml.ReadXml('login', 'err_info')
    #管理员登录url
    url1=username1[0]
    
    def __init__(self,ff):
        self.driver=BasePage.__init__(self, 'ff')            

class AddRatePage(BasePage):
    
    readXml=OperationXml()
    clickAdd=readXml.ReadXml('rate_manage', 'add_btn')
    
    setCurrency=readXml.ReadXml('rate_manage', 'rate_currency')
    
    currencyErr=readXml.ReadXml('rate_manage', 'rate_cur_err')
    #print('currencyErr:%s' %currencyErr)
    
    setEnable=readXml.ReadXml('rate_manage', 'rate_enable')
    
    setRateTo=readXml.ReadXml('rate_manage', 'rate_to')
    
    setUpdateType=readXml.ReadXml('rate_manage', 'rate_up')
    
    submitBtn=readXml.ReadXml('rate_manage', 'submit_btn')
    
    suc_info=readXml.ReadXml('manager_manage', 'suc_info')
        
    url1=clickAdd[0]
    
    
    #初始化
    def __init__(self):
        self.driver=BasePage.__init__(self,'ff')
        
    #返回当前webdriver    
    def get_driver(self):
        self.driver=self.driver
        return self.driver 
    
           
    #在新的标签页中打开地址为url的页面
    def openMMPage(self,url):
        self.openPage(url)
    
          
    #点击【新增】按钮      
    def click_add(self):
        self.click(self.findElement((self.clickAdd[1],self.clickAdd[2])))
        self.switch_to_latestWindow()
        
    def click_revise(self,Currency):
        tup=self.get_firstcols(Currency)
        if tup[1]==None:
            print 'Cannot find '+Currency+' in the table!'
        else:
            tup[1].click()
            
    #选择货币    
    def select_currency(self,value=setCurrency[3]):
        
        elem=self.findElement((self.setCurrency[1],self.setCurrency[2]))
        self.select_index(elem, value)
        return value 
        
     #获取重复货币信息
    def currency_dup(self):
        tup=self.isElementExist((self.currencyErr[1],self.currencyErr[2]))
        if  isinstance(tup, tuple):
            return tup[1]
        else:return None
    
    #选择启用类型    
    def select_enable(self,value=setEnable[0]):
        
        elem=self.findElement((self.selectLangue[1],self.selectLangue[2]))
        self.select_index(elem, value)  
        
    #输入汇率，默认为1       
    def set_currency_rate(self,c_rate=setRateTo):
                
        self.type(self.findElement(self.setRateTo), c_rate)
          
    #选择更新类型    
    def select_update_type(self,value=setUpdateType[0]):
        
        elem=self.findElement((self.selectLangue[1],self.selectLangue[2]))
        self.select_index(elem, value)
      
    #点击提交   
    def click_submit(self):
          
        self.click(self.findElement((self.submitBtn[1],self.submitBtn[2])))
        self.driver.implicitly_wait(30)
        self.switch_to_latestWindow()
        
    #确认添加成功
    def confirm(self):
                
        return self.findElement((self.suc_info[1],self.suc_info[2])).text        
            
    # 获取标题
    def page_title(self):
        return self.getTitle()
    
    #关闭driver
    def close_driver(self):
        self.close()
                                           
if __name__==('__main__'):
    test1=AddRatePage()
    test1.openPage('https://trade.iwisetrader.com/Manager/System/CurrencyRate')      
        