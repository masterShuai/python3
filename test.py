#!/usr/bin/python
# -*- coding: UTF-8 -*-

print("你好，世界");


#1.1
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

if True:
    print("True")
else:
    print("False")


#1.2
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
    
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
#  print ("False")    # 缩进不一致，会导致运行错误


#1.3
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

total = 'item_one' + \
        'item_two' + \
        'item_three'

print(total)

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']

print(total)

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

print(word)
print(sentence)
print(paragraph)

#1.4
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

input("\n\n按下 enter 键后退出。")

#1.5
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
