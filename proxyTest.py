#!/usr/bin/env python
#-*- coding: utf-8 -*-
import socket
import urllib
import urllib.error
import urllib.request
import sys
import re

__author__ = 'masterShuai'

def testArgument():
        
    '''测试输入参数，只需要一个参数 '''
    """if len(sys.argv) != 2:
        print(u'只需要一个参数就够了')
        tipUse()
        exit()
    else:
        TP = TestProxy(sys.argv[1])
        """
    TP = TestProxy(['http://117.135.196.197:55336', 'http://117.158.98.214:80', 'http://117.177.243.42:84', 'http://117.177.243.42:85'])

def tipUse():
    '''显示提示信息 '''
    print(u'该程序只能输入一个参数，这个参数必须是一个可用的proxy')
    print(u'usage: python testUrllib2WithProxy.py http://1.2.3.4:5')
    print(u'usage: python testUrllib2WithProxy.py https://1.2.3.4:5')


class TestProxy(object):
    '''这个类的作用是测试proxy是否有效 '''
    def __init__(self,proxyList):
        self.proxyIpList = proxyList;
        self.url = 'https://www.baidu.com'
        self.userAgent = self.getUserAgent();
        self.timeout = 5
        self.flagWord = 'baidu' #在网页返回的数据中查找这个关键词
        for proxyIp in self.proxyIpList:
                self.checkProxyFormat(proxyIp)
                self.useProxy(proxyIp)

    def checkProxyFormat(self,proxy):
        try:
            proxyMatch = re.compile('http[s]?://[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}\.[\d]{1,3}:[\d]{1,5}$')
            re.search(proxyMatch,proxy).group()
        except AttributeError:
            tipUse()
            exit()
        flag = 1
        proxy = proxy.replace('//','')
        try:
            protocol = proxy.split(':')[0]
            ip = proxy.split(':')[1]
            port = proxy.split(':')[2]
        except IndexError:
            print(u'下标出界')
            tipUse()
            exit()
        flag = flag and len(proxy.split(':')) == 3 and len(ip.split('.')) == 4
        flag = ip.split('.')[0] in map(str,range(1,256)) and flag
        flag = ip.split('.')[1] in map(str,range(256)) and flag
        flag = ip.split('.')[2] in map(str,range(256)) and flag
        flag = ip.split('.')[3] in map(str,range(1,255)) and flag
        flag = protocol in [u'http',u'https'] and flag
        flag = port in map(str,range(1,65535)) and flag
        '''这里是在检查proxy的格式 '''
        if flag:
            print(u'输入的http代理服务器符合标准')
        else:
            tipUse()
            exit()

    # 进行数据提交
    def useProxy(self,proxy):
        '''利用代理访问百度，并查找关键词 '''
        protocol = proxy.split('//')[0].replace(':','')
        ip = proxy.split('//')[1]

        '''
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({protocol:ip}))
        urllib.request.install_opener(opener)
        proxy_support = urllib.request.ProxyHandler({'sock5': 'localhost:1080'})
                opener = urllib.request.build_opener(proxy_support)
                urllib.request.install_opener(opener)
        try:
            response = urllib.request.urlopen(self.url,timeout = self.timeout)
        except:
            print(u'连接错误，退出程序')
            print(self.url + '  ' + str(self.timeout))
            exit()
       '''

        socket.setdefaulttimeout(3);  # 3秒未响应则为超时，跳过执行下一条
        try:
            # 添加代理
            proxy_handler = urllib.request.ProxyHandler({'http': ip});
            proxy_auth_handler = urllib.request.ProxyBasicAuthHandler();
            opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler);

            # 添加头信息
            opener.addheaders = [
                ('User-Agent', self.userAgent)
            ]
            # 数据请求
            response = opener.open(self.url);
            # 获取请求返还数据
            response_data = response.read().decode("utf8")
            print(ip, "正确：" + response_data)
        except urllib.error.HTTPError as e:
            print(ip, "错误：错误代码：", e.code);
            print("错误内容：", e.read().decode("utf8"));
            return
        except urllib.error.URLError as e:
            print(ip, '错误：未能获取服务器信息.')
            print('错误原因: ', e.reason)
            return
        except Exception as e:
            print(ip, "错误：其他未知错误！")
            print('错误原因: ', e.args)
            return

        # str = response.read().decode("utf8")
        # if re.search(self.flagWord,str):
        #     print(u'已取得特征词，该代理可用')
        # else:
        #     print(u'该代理不可用')

    # 获取用户浏览器信息
    def getUserAgent(self):
        userAgent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0';
        return userAgent;

if __name__ == '__main__':
    testArgument()
