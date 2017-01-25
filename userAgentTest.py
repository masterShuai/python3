#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib.request
import userAgents

class UrllibModifyHearder(object):
    '''使用urllib模块修改hearder'''
    def __init__(self):
        #这个是PC + IE 的 User-Agent
        PIUA = userAgents.pcUserAgent.get('Chrome 17.0 – MAC')
        # 这个是Mobile + UC 的 User-Agent
        MUUA =  userAgents.mobileUserAgent.get('UC standard')
        # 测试网站用的是 趣医挂号网
        self.url = 'https://fanyi.youdao.com'

        self.useUserAgent(PIUA,'youdao-web')
        self.useUserAgent(MUUA,'youdao-m')

    def useUserAgent(self,userAgent,name):
        request = urllib.request.Request(self.url)
        request.add_header(userAgent.split(':')[0],userAgent.split(':')[1])
        response = urllib.request.urlopen(request)
        fileName = './data/' + str(name) + '.html'
        with open(fileName,'w',encoding="utf-8")as fp:
            fp.write("%s\n\n" %userAgent)
            fp.write(response.read().decode('utf-8'))

if __name__ == '__main__':
    umh = UrllibModifyHearder()