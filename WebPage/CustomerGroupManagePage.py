#Embedded file name: C:\Users\Administrator\eclipse-workspace\selenium_use_case\test_case\WebPages\LoginPage.py
#-*- coding:utf-8 -*-  
from BasePage import BasePage
from common.OperationFile import OperationXml
from LoginPage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains


class CustomerGroupManagePage(BasePage):
    readXml=OperationXml()
    #管理员登录页面elements
    username1=readXml.ReadXml('login', 'useraccount')
    password1=readXml.ReadXml('login', 'password')
    login_btn1=readXml.ReadXml('login', 'login_btn')
    error_info1=readXml.ReadXml('login', 'err_info')
    #管理员登录url
    url1=username1[0]
    
    def __init__(self):
        self.driver=BasePage.__init__(self, 'ff')            

class AddCuGroupPage(BasePage):
    
    readXml=OperationXml()
    clickAdd=readXml.ReadXml('customer_group_manage', 'add_btn')
    
    setGroupname=readXml.ReadXml('customer_group_manage', 'customer_group_name')
    #print('setGroupname:%s' %setGroupname)
    selectPricetype=readXml.ReadXml('customer_group_manage', 'customer_group_pricetype')
    
    selectCutmargin=readXml.ReadXml('customer_group_manage', 'customer_group_cutmargin')
        
    selectMargintype=readXml.ReadXml('customer_group_manage', 'customer_group_margintype')
    
    selectGroupallow=readXml.ReadXml('customer_group_manage', 'customer_group_allow')
    
    submitBtn=readXml.ReadXml('customer_group_manage', 'submit_btn')
    
    suc_info=readXml.ReadXml('customer_group_manage', 'suc_info')
    
    Mousemove=readXml.ReadXml('customer_group_manage', 'customer_group_product')
    
    selectProduct=readXml.ReadXml('customer_group_manage', 'customer_group_sproduct')
    print ("selectProduct：%s"%selectProduct)
        
    url1=clickAdd[0]        
    
    #初始化
    def __init__(self):
        self.driver = BasePage.__init__(self,'ff')
        
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
            
    def mouse_move(self):
        menu=self.findElement((self.Mousemove[1],self.Mousemove[2]))
        product=self.findElement((self.selectProduct[1],self.selectProduct[2]))
        ActionChains(self.am).move_to_element(menu).click(product).perform()
    
    def select_product(self):
        #ActionChains(self).move_to_element(self.findElement((self.Mousemove[1],self.Mousemove[2]))).perform()
        self.click(self.findElement((self.selectProduct[1],self.selectProduct[2])))
    
    #输入客户分组名称      
    def set_name(self,value=setGroupname[3]):
        self.type(self.findElement((self.setGroupname[1],self.setGroupname[2])), value) 
            
    #选择客户动态差价类型    
    def select_pricetype(self,value=selectPricetype[3]):
        elem=self.findElement((self.selectPricetype[1],self.selectPricetype[2]))
        self.select_index(elem, value)
    
    #选择斩锁仓类型    
    def select_cutmargin(self,value=selectCutmargin[3]):
        elem=self.findElement((self.selectCutmargin[1],self.selectCutmargin[2]))
        self.select_index(elem, value)
        
    #选择保证金类型    
    def select_margintype(self,value=selectMargintype[3]):
        elem=self.findElement((self.selectMargintype[1],self.selectMargintype[2]))
        self.select_index(elem, value)
        
    #选择是否允许追加单    
    def select_allow(self,value=selectGroupallow[3]): 
        elem=self.findElement((self.selectGroupallow[1],self.selectGroupallow[2]))
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
    test1=AddCuGroupPage()    
    test1.openPage('https://trade.iwisetrader.com/Manager/Manager/CustomerGroupsList') 
        