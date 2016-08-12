#-*- coding: utf-8 -*-
#/usr/bin/python

#for i in range(10):
#    print "Hello World!"

import math

def add(x, y, f):
    return f(x) + f(y)

#print add(25, 8 , math.sqrt) 

def fun1(x):
    print x.title()

#print map(fun1, ["qiqi", "nanq"])

def fun_reduce(x, y):
    return x + y

# print reduce(fun_reduce, [1, 3, 8, 33])

def fun_filter(x):
    return x % 2 == 0

# print filter(fun_filter, [3, 55, 2, 4, 9, 22, 11, 33])

def reversed_cmp(x, y):
    if x > y:
        return -1
    elif x < y :
        return 1
    else:
        return 0

#print sorted([11, 9 , 3, 13, 2], reversed_cmp)

class Person(object):
    def __init__(self, name, gental, age):
        self.name = name
        self.gental = gental
        self.age = age
        self.__job = "student"

    def printJob(self):
        print self.__job



if __name__ == "__main__":

    print "main of modle is running !"
    xiaoming = Person("xiaoming", "male", 23)
    print xiaoming.name
    print xiaoming.age
    # print xiaoming.__job

    xiaoming.printJob()

else:
    print "module is running by other !"

def fun_test1():
    for i in range(10):
            print i

#fun_test1()


def funip():
	for i in range(100):
		s = "192.168.1.%d\n" %i
		with open ("1.txt", 'a')as f:
			f.write(s)

#测试全局变量

"""
name = "qiqi"
def print_name():
    print name
    global name 
    name = name + "love feifei"
    print name
print_name()
"""
"""
class A():
    x = 1
class B(A):
    pass
class C(A):
    pass
A.x = 2
B.x = 3
print A.x, B.x, C.x
"""

#
def duanlian():
    import time
    for i in range(30):
        time.sleep(1)
        print i
duanlian()

