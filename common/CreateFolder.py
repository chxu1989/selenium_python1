# coding:utf-8
'''
Created on 2018Äê1ÔÂ4ÈÕ

@author: Administrator
'''
import Configuration as cc
import os



def CreateRunFolder(self,path):
    now=cc.getCurrentTime()
    newpath=path+now
    os.mkdir(newpath)
    return newpath