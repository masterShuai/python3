#!/usr/bin/env python
#-*- coding:GBK -*-

def fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fac(n-1)

def main():
    print('����һ����׳˵ĳ���\n')
    n = raw_input('������һ��������:')
    try:
        n = int(n)
    except ValueError:
        print('�������Ҫ������һ�����������˳������ɡ�')
    print('%d! = %d' %(n,fac(n)))


if __name__ == '__main__':
    main()
