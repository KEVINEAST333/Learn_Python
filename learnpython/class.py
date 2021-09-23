# coding=utf-8
class MyClass:
    i = j = 0

    def __init__(self, m, n):
        self.i = m
        self.j = n
        pass

    print "is my class"


class People:
    sex = ""
    name = ""

    def __init__(self, sex, name):
        self.sex = sex
        self.name = name
        pass

    def message(self):
        print ("%s : %s" % (self.name, self.sex))


# 单继承
class Student(People):

    def __init__(self, sex, name):
        People.__init__(self, sex, name)


x = MyClass(1, 2)
print x.i, x.j
people = People("man", "wang")
people.message()


# 调用方法
class Parent:
    # 私有变量
    __s = 10

    def __init__(self):
        self.b = None

    def max(self, a, b):
        a = self.a
        b = self.b
        if a > b:
            return a
        else:
            return b

    def myMethod(self):
        print "调用父类方法"


class Son(Parent):

    def __init__(self):
        Parent.__init__(self)

    def myMethod(self):
        # super(Son, self).myMethod()
        # Parent.myMethod(self)
        print "调用子类方法"

    def max(self, a, b):
        return Parent.max(self, a, b)


so = Son()
so.myMethod()
pa = Parent()
n1 = 12
n2 = 3
max2 = so.max(n1, n2)
print max2
