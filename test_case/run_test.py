#-*- coding:utf-8 -*- 
import unittest
import HTMLTestRunnerCNbak
from common import CreateFolder as cf
from common import MySuit


listaa='C:\\Users\\selenium_python1\\test_case'
def creatsuite():
    
    testunit=MySuit.Suit()
    discover=unittest.defaultTestLoader.discover(listaa, pattern='test_*.py', top_level_dir=None)
    for test_suit in discover:
        for test_case in test_suit:
            testunit.addTest(test_case)
    return testunit
alltestname=creatsuite()


report_path=cf.CreateRunFolder('C:\\Users\\selenium_python1\\TestReport')
filename=report_path()+'\\result.html'
fp=file(filename,'wb')
runner=HTMLTestRunnerCNbak.HTMLTestRunner(
        stream = fp,
        title=u'自动化测试报告', 
        #description='详细测试用例结果',    #不传默认为空
        tester=u"cx",                    #测试人员名字，不传默认为QA
        verbosity=2           
        #retry=1                
        )
    #运行测试用例
runner.run(alltestname)