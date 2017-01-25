counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串
 
print (counter)
print (miles)
print (name)


print ("\n\n==============================================================\n\n")


a, b, c = 1, 2, "runoob"
print(a);
print(b);
print(c);

print ("\n\n==============================================================\n\n")


a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print ("\n\n==============================================================\n\n")

var1 = 1
var2 = 10
del var1, var2
'''
print(var1)
Traceback (most recent call last):
  File "G:\profession\python\baseDataType.py", line 29, in <module>
    print(var1)
NameError: name 'var1' is not defined
'''
print ("\n\n==============================================================\n\n")

print(2/4, 2//4, 2**5); #除法得到一个浮点数, 得到一个整数, 乘方


print ("\n\n==============================================================\n\n")
str = 'Runoob'

#-1 为从末尾的开始位置。

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个个到倒数第二个的所有字符[0:-1)
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串

word = 'Python'
print(word[-1], word[-6])

'''
word[0]='h'
Traceback (most recent call last):
  File "G:\profession\python\baseDataType.py", line 57, in <module>
    word[0]='h'
TypeError: 'str' object does not support item assignment

'''

print ("\n\n==============================================================\n\n")


list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

#-1 为从末尾的开始位置。

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素[0:3)
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

a = [1, 2, 3, 4, 5, 6]
a[0] = 666 #列表元素值可修改
a[2:5] = []   # 删除[2,5)
print(a)
print ("\n\n==============================================================\n\n")


#元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')

print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素 索引
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素 切片
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

'''
tup[0] = 11  # 修改元组元素的操作是非法的
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
'''

tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号

print ("\n\n==============================================================\n\n")
#集合（set）是一个无序不重复元素的序列。
#可以使用大括号({})或者 set()函数创建集合
#注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

student = ({'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'})

print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
    
print ("\n")

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a) #输出：{'r', 'c', 'b', 'a', 'd'} 因为set不允许重复
print(b)

print('\n');

print(a - b)     # a和b的差集 

print(a | b)     # a和b的并集

print(a & b)     # a和b的交集

print(a ^ b)     # a和b中不同时存在的元素


print ("\n\n==============================================================\n\n")

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

#字典是无序的对象集合。
#与list区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#键(key)必须是唯一的。 

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

print ("\n\n==============================================================\n\n")

