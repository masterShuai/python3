#!/usr/bin/env python
#-*- coding: GBK -*-
__author__ = 'hstking hstking@hotmail.com'

def strCase():
    "�ַ�����Сдת��"
    print "��ʾ�ַ�����Сдת��"
    print "��ʾ�ַ���S��ֵΪ��'  ThIs is a PYTHON  '"
    S = '  ThIs is a PYTHON  '
    print "��дת����Сд��\tS.lower() \t= %s"%(S.lower())
    print "Сдת���ɴ�д��\tS.upper() \t= %s"%(S.upper())
    print "��Сдת����\t\tS.swapcase() \t= %s"%(S.swapcase())
    print "����ĸ��д��\t\tS.title() \t= %s"%(S.title())
    print '\n'

def strFind():
    "�ַ����������滻"
    print "��ʾ�ַ����������滻��"
    print "��ʾ�ַ���S��ֵΪ��'  ThIs is a PYTHON  '"
    S = '  ThIs is a PYTHON  '
    print "�ַ���������\t\tS.find('is') \t= %s"%(S.find('is'))
    print "�ַ���ͳ�ƣ�\t\tS.count('s') \t= %s"%(S.count('s'))
    print "�ַ����滻��\t\tS.replace('Is','is') = %s"%(S.replace('Is','is'))
    print "ȥ���ҿո�\t\tS.strip() \t=#%s#"%(S.strip())
    print "ȥ��߿ո�\t\tS.lstrip() \t=#%s#"%(S.lstrip())
    print "ȥ�ұ߿ո�\t\tS.rstrip() \t=#%s#"%(S.rstrip())
    print '\n'
    
def strSplit():
    "�ַ����ָ���"
    print "��ʾ�ַ����ָ���"
    print "��ʾ�ַ���S��ֵΪ��'  ThIs is a PYTHON  '"
    S = '  ThIs is a PYTHON  '
    print "�ַ����ָ\t\tS.split() \t= %s"%(S.split())
    print "�ַ������1�� '#'.join(['this','is','a','python']) \t= %s"%('#'.join(['this','is','a','python']))
    print "�ַ������2�� '$'.join(['this','is','a','python']) \t= %s"%('$'.join(['this','is','a','python']))
    print "�ַ������3�� ' '.join(['this','is','a','python']) \t= %s"%(' '.join(['this','is','a','python']))
    print '\n'

def strCode():
    "�ַ������롢����"
    print "��ʾ�ַ������롢����"
    print "��ʾ�ַ���S��ֵΪ��'����������'"
    S = '����������'
    print "GBK�����S \t = %s"%(S)
    print "GBK�����Sת��unicode����"
    print "S.decode('GBK')= %s"%(S.decode("GBK"))
    print "GBK�����Sת����utf8"
    print "S.decode('GBK').encode('utf8') = %s"%(S.decode("GBK").encode("utf8"))
    print "ע�⣺�����Ǳ��뻹�ǽ�����ԵĶ���unicode�ַ����룬\n����Ҫ������߽���ǰ�����Ƚ�Դ�ַ���ת����unicode�����ʽ"
    print '\n'

def strTest():
    "�ַ�������"
    print "��ʾ�ַ�������"
    print "��ʾ�ַ���S��ֵΪ��'abcd'"
    S1 = 'abcd'
    print "����S.isalpha() = %s"%(S1.isalpha())
    print "����S.isdigit() = %s"%(S1.isdigit())
    print "����S.isspace() = %s"%(S1.isspace())
    print "����S.islower() = %s"%(S1.islower())
    print "����S.isupper() = %s"%(S1.isupper())
    print "����S.istitle() = %s"%(S1.istitle())


if __name__ == '__main__':
        strCase()
        strFind()
        strSplit()
        strCode()
        strTest()
