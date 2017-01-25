#!/usr/bin/env python
# -*- coding:utf-8 -*-

from codes.myLog import MyLog
import time

__author__ = 'masterShuai'
__filePath__ = './logging/'


if __name__ == '__main__':
    log = MyLog(__filePath__ + time.strftime("%Y%m%d"))
    log.debug('test debug')
    log.info('test info')
    log.warn('test worn')
    log.error('test error')
    log.critical('test critical')

