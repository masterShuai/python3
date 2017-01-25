#-*- coding: utf-8 -*-
__author__ = 'masterShuai'


import os

#创建文件
def operaFile():
    print(u'创建一个名字为test.txt的文件，并写入hello world ')

    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'data', 'test.txt')

    print(u'验证文件是否存在')
    os.system('rm ' + file_path)
    os.system('ls -l ' + file_path)
    
    print(u'创建文件并写入')
    fp = open(file_path, 'w')
    fp.write('hello world')
    fp.close

    print(u'再次验证文件是否存在')
    os.system('ls -l ' + file_path)
    os.system('cat ' + file_path)
    print("\n")

    print('避免open失败')

    with open(file_path, 'r') as fp:
        st = fp.read()
    print('文件内容为：%s'%st)

if __name__ ==  '__main__':
    operaFile()
