# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
Created on Sat Sep 05 05:50:00 2015
Modified on Sun Jan 10 8:23 2016
    my_module.py 是我自写的模块文件，内包含有可用函数。
一个py文件被引用，会自动创建一个pyc的文件。下次会更快速
的被引用。
    2015-12-09  加入尾递规基本用法和查找英文月份
    2015-12-12  加入固定参数与可变参数
    2015-12-13  加入类的构造、生成随机密码函数
    2016-01-02  根据python最佳实践改写生成随机密码函数
    2016-03-23  由零散的函数形式改写成类的型式
@author: fan
"""
import os, base64
import time, datetime

class My_module(object):

    def zen(self):
        import this
        s=this.s
        d = {}
        for c in (65, 97):
            for i in range(26):
                d[chr(i+c)] = chr((i+13) % 26 + c)

        print 'python 之禅'
        print "".join([d.get(c, c) for c in s])

    #获得时间
    def times(self):
         # import time
         tr1= time.time()
         print tr1
         tr2 = time.localtime(time.time())
         print tr2
         tr3 = time.asctime(time.localtime(time.time()))
         print tr3

    #获得时间与昨天
    def yestoday():
        # import time
        time.strftime('%Y%m%d')
        #获取了当前时间的年月日

        #获取昨天的时间datetime

        # import datetime
        now_time = datetime.datetime.now()
        yes_time = now_time + datetime.timedelta(days=-1)
        #格式化输出
        yes_time_nyr = last_time.strftime('%Y%m%d')

    #获取某月日历
    def months1(self):
         import calendar
         cal = calendar.month(2015, 12)
         print cal;
    """
    sum = lambda arg1, arg2: arg1 + arg2
    print sum(10, 20)
    """

    #显示关键字
    def show_keyword(self):
        import keyword
        print keyword.kwlist


    #读文件函数,dir1为文件路径
    #20150914改进读文件函数
    def openfile(self):

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
                # with open (dir1, "r") as f:
                #     for lines in f.readlines():
                #         print lines.strip()

            #2016年8月3日改成
                with open(dir1, 'r') as f:
                    lines = (line.strip() for line in f)
                    for line in lines:
                        print line

            # 应用了生成器？
            # def test4112():
            #     with open('test2.py') as f:
            #         lines = (line.strip() for line in f)
            #         for line in lines:
            #             print line

            except Exception:
                print "The path of your input is not exite! Please check your path!"
        print "==========================================="

    #写文件函数

    def makefile(self):
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

    def listmulu(self):
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
    def listfulldir(self):
        dir1 = raw_input("Please input your path:")
        def listpath(dir1):
            for name in os.listdir(dir1):
                full_path = os.path.join(dir1, name)
                print full_path
                if os.path.isdir(full_path):
                    listpath(full_path)


    #建文件练习
    def makedir(self, dir1):
        while True:
            #判断目录是否存在， 也可判断文件
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




    #递规函数用法（尾递规）
    def tailRecursive(self, n):
        return tailRecursiveFun(n, 1)

    def tailRecursiveFun(self, n, p):
        if n ==1:
            return p
        else:
            return fun2(n-1, n+p)
    #print fun1(50)

    #生成器,斐波那契数列
    def fun_1():
        x = 1000
        for i in list_test(x):
            print i,

    def list_test(x):
        a = b = 1
        for i in xrange(1000):
            yield a
            a , b = b, a + b



    #写月份与星期英文函数
    def  monthFun(self, x, y):
        month_dict={
        1: 'January Jan', 2:'February Feb', 3:'March Mar', \
        4:'Apri Apr', 5:'May May', 6:'June Jun', 7:'July  Jul ', \
        8:'August Aug', 9:'September Sep', 10:'October Oct',\
        11:'Novermber Nov', 12:'December Dec'
        }
        week_dict={
        1: 'Monday Mon', 2:'Tuesday Tus', 3:'Wednesday Wed', \
        4:'Thursday Thur', 5:'Friday Fri', 6:'Saturday Sat', 7:'Sunday Sun'
        }
        if   x>0 and x <13:
            print  "The English Month is %s"  %month_dict.get(x)
        else:
            print "The Month  %d  is Error " %x
        if y > 0 and y < 8:
            print  "The English Week  is %s"  %week_dict.get(y)
        else:
            print "The Week  y  %d  is Error , The  1 < y < 7" %y


    #写ether_ip函数
    def writeIp(self, i1, j1):
        str1 = "00:" * 5 + "00"
        for i in range(1,i1+1):
            for j in range(1,j1+1):
    #            print "192.168.%d.%d 00:00:00:00:00:00" %(i,j)
                print "192.168.%d.%d %s" %(i, j, str1)

    #将你的str1字符串用base64算法加密10次
    def base64_encode(self, str1):
        for i in range(10):
            str1 = base64.encodestring(str1)
            print str1
        return str1

    #尝试用base64解密你的字符串
    def base64_decode(self, str1):
        n = 0
        try:
            while True:
                str1 = base64.decodestring(str1)
                n = n + 1
                print str1, n

        except Exception:
            print "jiamihuanyuanwei:%s, jiamicishu:%d" %(str1, n)

    #生成随机密码没有空格
    def rand_passwd(self):
        import random
        for a in range(3):
            # g = random.sample('abcdefghijkimnopqrstuvwxyz1234567890ABCDEFGHIJKIMNOPQRSTUVWXYZ#%^!&',12)
            # g = random.sample('abcdefghijkimnopqrstuvwxyz1234567890ABCDEFGHIJKIMNOPQRSTUVWXYZ',20)
            g = random.sample('1234567890',8)
            string1 = [str(n) for n in g ]
            print "".join(string1)
            # print "\n"

    #生成10个随机数
    def randint10():
        import random
        date = [random.randint(-10, 10) for _ in xrange(10)]
        print date

    #字母变小写
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
    def big(self):
        list1 = [32, 31, 64, 11, 2,  49]
        def reversed_cmp(x, y):
            if x > y:
                return -1
            elif x < y:
                return 1
            else:
                return 0
        return sorted(list1, reversed_cmp)
'''
#实现忽略大小写排序的算法。

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    elif u1 > u2:
        return 1
    else:
        return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

'''




    def small(self):
        list1 = [32, 31, 64, 11, 2,  49]
        return sorted(list1)

    #debug调试
    def make_bread(self):
        """
        你可以在命令行使用Python debugger运行一个脚本， 举个例子：

        $ python -m pdb my_script.py

        命令列表：
        c: 继续执行
        w: 显示当前正在执行的代码行的上下文信息
        a: 打印当前函数的参数列表
        s: 执行当前代码行，并停在第一个能停的地方（相当于单步进入）
        n: 继续执行到当前函数的下一行，或者当前行直接返回（单步跳过）

        """
        pdb.set_trace()
        return 'I do not have time'




    #多条件判断
    #all(True, False, True),结果为False
    #any(True, False, True), 结果为True
    def my_if(self):
        filter_list = ['yahoo', 'sina', 'baidu']
        string2 = ['21.com', 'sina.com.cn', 'www.baidu.com', 'hao123.com', 'yahoo.com.cn', 'chacha']
        for content in string2:
            if any(t in content for t in filter_list):
                continue
            print content
        print 'if all **********'

    """
    #很好的例子
    def add(x):
        return x + x
    
    def multiply(x):
        return x * x

    def my_test():
        func = [add, multiply]
        for i in range(5):
            value = map(lambda x: x(i), func)
            print value

    #函数中定义函数
    def hi(name = "qiqi"):
        print "Now you are in hi()"

        def greet():
            return "Now you are in greet() "

        def hello():
            return "Now you are in hello()"

        if name == "qiqi":
            return greet
        else:
            return hello

    a = hi
    print a()

    #switch 语句的代替用法
    def testSwich(x, o, y):
        def jia(x, y):
            return  x + y

        def jian(x, y):
            return x - y

        def cheng(x, y):
            return x * y

        def chu(x, y):
            return x / y

        operation = {'+':jia, '-':jian, '*':cheng, '/': chu}
        print operation.get(o)(x, y)


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

    #enumerate用法
    print list(enumerate('abc', 1))

    #字典
    print {i: i * 3 for i in xrange(10)}
    #集合
    print {i * 15 for i in range(3, 9)}



    #计数
    def testCounter():
        from collections import Counter
        c = Counter('Hello World')
        print c
        print c.most_common(4)


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

    #列表练习2  , 可获取索引和值
    def list_test2():
        a = [7, 8, 9]
        b = [i + 3 for i in a]
        c = map(lambda x: x + 3, a)
        print b,c
        for i, item in enumerate(a):
            print i,item

    #倒序输出列表
    list1 = ['Adam', 95, 'Lisa', 85, 'Bart', 59]
    for i in list1:
        print i
    print list1[::-1]


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

    #调用生成器
    for i in fib(10):
        print i

    #lambda
    def foo3(n):
        list1 = map(lambda x:x*x, [1, 2, 3, 4])
        print list1


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

    #装饰器  计算函数所用时间
    def performace(f):
        def fn(*arg, **kw):
            t1 = time.time() * 100
            result = f(*arg, **kw)
            t2 = time.time() * 100
            print 'call' + f.__name__ + '() in' + str(t2 - t1) + 's'
            return result
        return fn

    @performace
    def factorial(n):
        return reduce(lambda x, y: x + y, range(1, n+1))

    print factorial(100000)


    #返回函数
    def f():
        print 'call f()'

        def g():
            print 'call g()'
        return g
    x
    x()


    def cal_prod(lst):

        def mydef():
            s = 1
            for i in lst:
                s *= i
            return s
        return mydef
    f = cal_prod([1, 2, 3, 5])
    print f()

#闭包
def count():
    fs = []
    for i in range(1, 4):

        def f(j):

            def g():
                return j * j
            return g
        r = f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()

#lambda函数
def testlambda():
    list1 = range(10)
    print map(lambda x: x * x, list1)
    print sorted(list1, lambda x,y: -cmp(x, y))
    myabs = lambda x: -x if x < 0 else x
    print myabs(-2)
    print myabs(90)



    #json练习

    def testJson():
        import json

        data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
        print json.dumps(data)
        print json.dumps(data, indent=2)


    # 构造类2015-12-13加入
    class Monk(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def play(self, monkey):
            print monkey, "绳命是如此的辉煌....."

    #Counter用法示例
    #20160211加入
    def testCounter():
        from collections import Counter
        c = Counter("Hello")
        print c
        # print help(Counter)
        print c.most_common()


    #由于Python的动态特性，json.load()并不一定要从一
    #个File对象读取内容。任何对象，只要有read()方法，
    #就称为File-like Object，都可以传给json.load()。

    import json

    class con():
        def read(self):
            return r'["Tim", "Nana", "Feifei"]'

    s = con()
    print json.load(s)


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


    #特殊方法
    class Person(object):
        def __init__(self, name, gender):
            self.name = name
            self. gender = gender

        def __str__(self):
            return '(Person: %s, %s)' %(self.name, self.gender)

    p = Person('Bob', 'male')
    print p


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



def test():

    #python 之禅
    import this

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



if __name__ == "__main__":

    print __doc__
    a = My_module()
    a.rand_passwd()
