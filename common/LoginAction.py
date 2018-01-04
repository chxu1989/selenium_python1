# -*- coding: utf-8 -*-

from WebPage import LoginPage
from WebPage import ManagerManagePage
from common.OperationFile import OperationXml

class LoginAction(object):
    
    readXml=OperationXml()
    
    #管理员登录页面elements
    username1=readXml.ReadXml('login', 'useraccount')
    password1=readXml.ReadXml('login', 'password')
    login_btn1=readXml.ReadXml('login', 'login_btn')
    error_info1=readXml.ReadXml('login', 'err_info')
    #管理员登录url
    url_wt1=username1[0]
    url_mt1=url_wt1.replace('/Login/','/Login1/')
    
    #客户登录url    
    url_wt2=url_wt1.replace('Manager','Client')
    url_mt2=url_wt2.replace('/Login/','/Login1/')
    
    #经纪人登录url
    url_wt3=url_wt1.replace('Manager','Sales')
    url_mt3=url_wt3.replace('/Login/','/Login1/')
    
    
    

    def findElement(self,element):
        '''
        Find element
        element is a set with format (identifier type, value), e.g. ('id','username')
        Usage:
        self.findElement(element)
        '''
        try:
            type = element[0]
            value = element[1]
            print 'find=',self.driver
            if type == "id" or type == "ID" or type=="Id":
                elem = self.driver.find_element_by_id(value)

            elif type == "name" or type == "NAME" or type=="Name":
                elem = self.driver.find_element_by_name(value)

            elif type == "class" or type == "CLASS" or type=="Class":
                elem = self.driver.find_element_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type=="Link_text":
                elem = self.driver.find_element_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type=="Xpath":
                elem = self.driver.find_element_by_xpath(value)

            elif type == "css" or type == "CSS" or type=="Css":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found"+ str(element))
        return elem
    
    #登录管理员操作,需要传入driver   
    def login_manager(self,driver):
         
        self.driver=driver         
                            
        self.driver.get(self.url_wt1)      
        self.driver.implicitly_wait(30)
       
        self.findElement((self.username1[1],self.username1[2])).send_keys(self.username1[3])
        self.findElement((self.password1[1],self.password1[2])).send_keys(self.password1[3])
        self.findElement((self.login_btn1[1],self.login_btn1[2])).click()
 
         
        self.driver.implicitly_wait(30)
    
    
    #登录客户    
    def login_client(self,driver):
        
        self.driver=driver         
                            
        self.driver.get(self.url_wt2)      
        self.driver.implicitly_wait(30)
       
        self.findElement((self.username1[1],self.username1[2])).send_keys(self.username1[3])
        self.findElement((self.password1[1],self.password1[2])).send_keys(self.password1[3])
        self.findElement((self.login_btn1[1],self.login_btn1[2])).click()
 
         
        self.driver.implicitly_wait(30)
        
    #登录经纪平台
    def login_sales(self,driver):
        
        self.driver=driver         
                            
        self.driver.get(self.url_wt3)      
        self.driver.implicitly_wait(30)
       
        self.findElement((self.username1[1],self.username1[2])).send_keys(self.username1[3])
        self.findElement((self.password1[1],self.password1[2])).send_keys(self.password1[3])
        self.findElement((self.login_btn1[1],self.login_btn1[2])).click()
 
         
        self.driver.implicitly_wait(30)          
        
if __name__=='__main__':
    newtest=LoginAction()
    newtest.login_manager()
