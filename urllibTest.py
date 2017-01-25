#!/usr/bin/env python
#_*_ coding: utf-8 _*_
__author__ = 'masterShuai'

import urllib.request
import time
import platform
import os

def clear():
    '''该函数用于清屏'''
    print(u'内容过多，显示3秒后翻页')
    time.sleep(3)
    OS = platform.system()
    if(OS == u'Windows'):
        os.system('cls')
        
    else:
        os.sysytem('clear')


def linkBaidu():
    url = 'http://www.baidu.com/'
    try:
        response = urllib.request.urlopen(url, timeout = 3)
    except urllib.request.URLError:
        print(u'地址输入错误')
        exit()
    with open('./data/baidu.txt','w') as fp:
        fp.write(str(response.read()))
    print(u'获取url信息,response.geturl() \n: %s' %response.geturl())
    print(u'获取返回代码,response.getcode() \n: %s' %response.getcode())
    print(u'获取返回的信息,response.info() \n: %s' %response.info())
    print(u'获取的网页内容已存入baidu.txt，请查看')


if __name__ == '__main__':
    linkBaidu()
