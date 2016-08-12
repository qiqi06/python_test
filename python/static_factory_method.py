#-*- coding: utf-8 -*-
"""
练习简单工厂模式
"""


#建立一工厂类，要用是，再实例化它的生产水果方法，
class Factory(object):
    def creatFruit(self, fruit):
        if fruit == "apple":
            return Apple(fruit, "red")
        elif fruit == "banana":
            return Banana(fruit, "yellow")



class Fruit(object):
    def __init__(self, name, color):
        self.color = color
        self.name = name

    def grow(self):
        print "%s is growing" %self.name

class Apple(Fruit):
    def __init__(self, name, color):
        super(Apple, self).__init__(name, color)


class Banana(Fruit):
    def __init__(self, name, color):
        super(Banana, self).__init__(name, color)
        self.name = 'banana'
        self.color = 'yellow'

def test():
    #这里是两个对象， 一个是工厂，一个是我要订的水果
    factory = Factory()
    my_fruit = factory.creatFruit('banana')
    my_fruit.grow()


if __name__ == "__main__":
    print "The main module is running!"
    test()