# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Sat Sep 05 05:50:00 2015
Modified on Sun Jan 10 8:23 2016
    my_module.py 是我自写的模块文件，内包含有可用函数。
一个py文件被引用，会自动创建一个pyc的文件。下次会更
快速的被引用。
    2015-12-09  加入尾递规基本用法和查找英文月份
    2015-12-12  加入固定参数与可变参数
    2015-12-13  加入类的构造、生成随机密码函数
    2016-01-02  根据python最佳实践改写生成随机密码函数
@author: fan
"""
import os, base64

version="my_module `s version is 1.0. By fan"

#读文件函数,dir1为文件路径
#20150914改进读文件函数
def openfile():

#  with open (dir1, "r") as f:
#            for lines in f.readlines():
#                print lines.strip()

    print "==========================================="
    print "input q exit!"
    while True:
        dir1 = raw_input("Please input path of your file:")
        print dir1
        if dir1 == "q":
           break
        try:
            with open (dir1, "r") as f:
                for lines in f.readlines():
                    print lines.strip()
        except Exception:
            print "The path of your input is not exite! Please check your path!"
    print "==========================================="


#递规函数用法（尾递规）
def fun1(n):
    return fun2(n, 1)
def fun2(n, p):
    if n ==1:
        return p
    else:
        return fun2(n-1, n+p)
#print fun1(50)

#写月份与星期英文函数
def  Month(x, y):
    Month_dict={
    1: 'January Jan', 2:'February Feb', 3:'March Mar', \
    4:'Apri Apr', 5:'May May', 6:'June Jun', 7:'July  Jul ', \
    8:'August Aug', 9:'September Sep', 10:'October Oct',\
    11:'Novermber Nov', 12:'December Dec'
    }
    Week_dict={
    1: 'Monday Mon', 2:'Tuesday Tus', 3:'Wednesday Wed', \
    4:'Thursday Thur', 5:'Friday Fri', 6:'Saturday Sat', 7:'Sunday Sun'
    }
    if   x>0 and x <13:
        print  "The English Month is %s"  %Month_dict.get(x)
    else:
        print "The Month  %d  is Error " %x
    if y > 0 and y < 8:
        print  "The English Week x is %s"  %Week_dict.get(y)
    else:
        print "The Week  y  %d  is Error , The  1 < y < 7" %y

    """调用示例
import my_module
x = 5
y = 3
my_module.Month(int (x), int (y))
    """
#传入固定参数与可变参数
def power(x, n=2):
  s = 1
  while n > 0:
    s = s * x
    n-=1
    print (s)
  print (s)

def fun1(*arg):
  sum = 0.0
  if len(arg) == 0:
    return sum
  for i in arg:
    sum+=i
  return sum / len(arg)

#生成列表
def fun3():
  print ([x * (x + 1) for x in range(1, 100, 1)])
  print ([x * x for x in range(1, 11) if x % 2 == 0])
  print ([m + n for m in 'ABC' for n in '123'])

#写ether_ip函数
def write_ip(i1,j1):
    str1 = "00:" * 5 + "00"
    for i in range(1,i1+1):
        for j in range(1,j1+1):
#            print "192.168.%d.%d 00:00:00:00:00:00" %(i,j)
            print "192.168.%d.%d %s" %(i, j, str1)

#


#将你的str1字符串用base64算法加密10次
def base64_jiami(str1):
    for i in range(10):
        str1 = base64.encodestring(str1)
        print str1
    return str1

#尝试用base64解密你的字符串
def base64_jiemi(str1):
    n = 0
    try:
        while True:
            str1 = base64.decodestring(str1)
            n = n + 1
            print str1, n
    except Exception:
        print "jiamihuanyuanwei:%s, jiamicishu:%d" %(str1, n)


#生成随机密码没有空格
def rand_passwd():
    import random
    for a in range(3):
        g = random.sample('abcdefghijkimnopqrstuvwxyz1234567890ABCDEFGHIJKIMNOPQRSTUVWXYZ#%^!&',12)
        g = random.sample('abcdefghijkimnopqrstuvwxyz1234567890ABCDEFGHIJKIMNOPQRSTUVWXYZ',20)
        string1 = [str(n) for n in g ]
        print "".join(string1)
        # print "\n"

#字典取值

def dict_value():
    dict1 = {'hello':'world'}
    if 'hello' in dict1:
        print dict1['hello']
    print dict1.get('hello','default_value')
    print dict1.get('chichi', 'default_value')

#列表练习
def list_test1():
    a = [3, 4, 5]
    b = [i for i in a if i > 4]
    print b
    c = filter(lambda x: x > 4, a)
    print c

#列表练习2
def list_test2():
    a = [7, 8, 9]
    b = [i + 3 for i in a]
    c = map(lambda x: x + 3, a)
    print b,c
    for i, item in enumerate(a):
        print i,item

#超长的行
#Good:    
#受教了....
my_very_big_string = (
    "For a long time I used to go to bed early. Sometimes, "
    "when I had put out my candle, my eyes would close so quickly "
    "that I had not even time to say “I’m going to sleep.”"
)
""" 
from some.deep.module.inside.a.module import (
    a_nice_function, another_nice_function, yet_another_nice_function)
"""

#
def format_name(s):
    return s[0].upper()+s[1:].lower()
# print map(format_name, ['admin', "LiSA", "barT"])

#比较大小函数
"""
但 sorted()也是一个高阶函数，它可以接收一个比较
函数来实现自定义排序，比较函数的定义是，传入
两个待比较的元素 x, y，如果 x 应该排在 y 的前面，
返回 -1，如果 x 应该排在 y 的后面，返回 1。如果
x 和 y 相等，返回 0。
"""
def big():
    list1 = [32, 31, 64, 11, 2,  49]
    def reversed_cmp(x, y):
        if x > y:
            return -1
        elif x < y:
            return 1
        else:
            return 0
    return sorted(list1, reversed_cmp)

def small():
    list1 = [32, 31, 64, 11, 2,  49]
    return sorted(list1)

#写文件函数

def makefile():
    while 1:
        print "============================================="
        print r"Input your pathfile q ,the program is quit !"
        dirfile1 = raw_input("Pleae input your pathfile:")
        yourstr1 = raw_input("Please input your str:")
        if dirfile1 == "q":
            break
        elif os.path.isfile(dirfile1):
            print "your pathfile is exit! it will add to file!"
            with open(dirfile1, "a") as f:
                f.write(yourstr1)
        else:
            with open(dirfile1, "w") as f:
                f.write(yourstr1)
        n = 1
        with open(dirfile1, "r") as f:
            for lines in f.readlines():
                print "num%s  %s" %(n, lines)
                n +=1
    print "================================================"

#文件目录列表

def listmulu():
    dir1 = raw_input("Please input your mulu:")
    if os.path.exists(dir1):
        print "It will make information for  listfile"
        for i in os.listdir(dir1):
             with open("listfile.txt", "a") as f:
                 f.write(i + "\n")
        with open("listfile.txt", "r") as f:
            for lines in f.readlines():
                print lines.strip()
    else:
        print "Your path is not exist."

#递归目录（需要引入os模块）
def listfulldir():
    dir1 = raw_input("Please input your path:")
    def listpath(dir1):
        for name in os.listdir(dir1):
            full_path = os.path.join(dir1, name)
            print full_path
            if os.path.isdir(full_path):
                listpath(full_path)


#建文件练习
def makedir(dir1):
    while True:
        if os.path.exists(dir1):
            print "Your path is exist!,Under it will make 10 file"
            for i in range(10):
                full_path = dir1 + "\\" + str(i) + ".txt"
                print full_path
                with open(full_path, "a") as f:
                    f.write("%d" %i )
            break
        else:
            print "Your path is not exist,Will make it!"
            os.mkdir(dir1)

#倒序输出列表
"""
list1 = ['Adam', 95, 'Lisa', 85, 'Bart', 59]
for i in list1:
     print i
print list1[::-1]
"""

#生成器
def foo():
     g = ( x * x for x in range(10))
     for n in g:
          print n,

def foo1(n):
     for i in fib(n):
          print i,
def fib(max):
     n, a, b = 0, 0, 1
     while n < max:
          yield b
          a, b = b, a+b
          n+=1

"""
调用生成器
for i in fib(10):
    print i
"""



def foo3(n):
     list1 = map(lambda x:x*x, [1, 2, 3, 4])
     print list1

#获得时间
def times():
     import time
     tr1= time.time()
     print tr1
     tr2 = time.localtime(time.time())
     print tr2
     tr3 = time.asctime(time.localtime(time.time()))
     print tr3

#获得时间与昨天
def yestoday():
    import time
    time.strftime('%Y%m%d')
    #获取了当前时间的年月日

    #获取昨天的时间datetime

    import datetime
    now_time = datetime.datetime.now()
    yes_time = now_time + datetime.timedelta(days=-1)
    #格式化输出
    yes_time_nyr = last_time.strftime('%Y%m%d')

#获取某月日历
def months1():
     import calendar
     cal = calendar.month(2015, 12)
     print cal;
"""
sum = lambda arg1, arg2: arg1 + arg2
print sum(10, 20)
"""

#装饰器
#装饰器函数一定要在前面，否则提示未定义
def deco(func):
    def _deco():
        print "before now() called"
        func()
        print "after now() called"
    return _deco

@deco
def now():
    print "2015, now() called"


# now()
# print "======================="
# now()

#带参数装饰器
"""
def deco(func):
    def _deco(a, b):
        print "before now() called"
        ret=func(a, b)
        print "after now() called"
        return ret
    return _deco

@deco
def now(a, b):
    print "2015, now(%s, %s) called" %(a, b )

now(7, 7)
print "======================="

#打印出程序所用时间函数
import time
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %fs' % (f.__name__, (t2 - t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
"""



#性能分析
def foo():
    """
    import time
    for i in range(5000):
        # time.sleep(2)
        print i

    class A():
        x = 1
    class B(A):
        pass
    class C(A):
        pass
    A.x = 2
    B.x = 3
    print  A.x, B.x, C.x 
    """
    import random
    while True:
        s = random.randint(0,100)
        print s
        if s == 50:
            break
"""            
if __name__ == "__main__":
    
    #python 之禅
    import this 

    import cProfile
    cProfile.run("foo()")
"""

# 构造类2015-12-13加入
class Monk(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def play(self, monkey):
        print monkey, "绳命是如此的辉煌....."

#由于Python的动态特性，json.load()并不一定要从一
#个File对象读取内容。任何对象，只要有read()方法，
#就称为File-like Object，都可以传给json.load()。
"""
import json

class con():
    def read(self):
        return r'["Tim", "Nana", "Feifei"]'

s = con()
print json.load(s)
"""
"""
#多重继承
#注意多重继承super()方法
class A(object):
    def __init__(self, a):
        print 'init A...'
        self.a = a
class B(A):
    def __init__(self, a):
        super(B, self).__init__(a)
        print 'init B...'

class C(A):
    def __init__(self, a):
        super(C, self).__init__(a)
        print 'init C...'
class D(B, C):
    def __init__(self, a):
        super(D, self).__init__(a)
        print 'init D...'

dd = D('dd')
"""
"""
#设置多变参数
class Person(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems():
            setattr(self, k, v)

p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course

"""
"""
#特殊方法
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self. gender = gender
        
    def __str__(self):
        return '(Person: %s, %s)' %(self.name, self.gender)
        
p = Person('Bob', 'male')
print p

"""
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student %s, %s, %s)' %(self.name, self.gender, self.score)

s = Student('Bob', 'male', 88)
print s

"""
引入模块中的类
imort my_module
实例化类
YC_Monk = my_moudle.Monk("yancan", 20)
 print YC_Monk.name

#这个引入好
try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python':2.7})

#引入未来模块
from __future__ import unicode_literals

s = 'am I an unicode?'
print isinstance(s, unicode)

"""

if __name__=='__main__':
    Month(1, 6)