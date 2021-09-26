# coding=utf-8
# 导入 support 模块
import support
# 导入 math 模块
import math


class math2:

    def __init__(self):
        pass

    def max(self, a, b):
        if a >= b:
            return a
        else:
            return b


ma = math2()
print ma.max(12, 3)
support.print_func("wangdong")
content = dir(support)
print content
# 读取键盘输入
# 1.raw_input
string = raw_input("please enter :")
print "enter message is :", string
# input函数
# input 函数和 raw_input 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
string3 = input("please enter :")
print "enter is", string3

