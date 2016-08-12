#-*- coding:utf-8 -*-
#!/usr/bin/python

"""
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def printScore(self):
        print  '%s: %s ' %(self.name, self.score)


#实例化类
mili = Student('mili', 98)
print mili.name
mili.printScore()


#实例化类和限制访问
class Person(object):

    #限制访问加双_
    __count = 0

    def __init__(self, name):
        Person.__count += 1
        self.name = name
        print Person.__count

p1 = Person('Bob')
p2 = Person('Alice')

#这个限制访问
# print Person.__count


class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

#定义方法可以访问类的私有属性
    def get_grade(self):
        if self.__score >= 80:
            return "A"
        elif 80 > self.__score >= 60:
            return "B"
        else:
            return "C"

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()

import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

p1 = Person('Bob', 90)

#因为方法也是一个属性，所以，它也可以动态地添加到实例上，只是需要用 types.MethodType() 把一个函数变为一个方法
p1.get_grade = types.MethodType(fn_get_grade, p1, Person)
print p1.get_grade()
# => A
# p2 = Person('Alice', 65)
# print p2.get_grade()
# ERROR: AttributeError: 'Person' object has no attribute 'get_grade'
# 因为p2实例并没有绑定get_grade


#定义类方法

class Person2(object):
    count = 0
    #定义类方法
    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self, name):
        self.name = name
        Person2.count = Person2.count + 1

print Person2.how_many()
p1 = Person2("NaNa")
print Person2.how_many()
print p1.count

"""

class Person(object):
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return "I am a Person, My name is %s" % self.name


class Student(Person):
    
    #一定要用 super(Student, self).__init__(name, gender) 
    #去初始化父类，否则，继承自 Person 的 Student 将没有 name 和 gender。
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return "I am a student, My name is %s" % self.name

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def whoAmI(self):
        return "I am a Teacher, my name is %s" % self.name

meimei = Person("meimei", "Female")
qiqi = Student("qiqi", "Female", 89)
lili = Teacher("lili", "Female", "English")

def printWho(x):
    print x.whoAmI()

printWho(meimei)
printWho(qiqi)
printWho(lili)



