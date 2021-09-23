# coding=utf-8
# hello word
print ("hello word")
list = [1, 2, 3]  # type: List[int]
print list
i = 0
if i == 1:
    print ("你好")
elif i == 2:
    print ("2")
else:
    print ("0")
# Python 中的变量赋值不需要类型声明。
# 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
# 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
count1 = count2 = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
str1 = "abcdef"
# Python列表
list2 = ["abc", 123, "efg", 456]
list3 = ["hij", 789, "lmn", "ABC"]
# Python 元组
# 元组是另一个数据类型，类似于 List（列表）。
# 元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple1 = ('runoob', 786, 2.23, 'john', 70.2)
print str1[1:3]
print count1, count2
print miles
print name
# [0,2)
print list2[0:2]
# [2,
print list2[2:]
# 打印两次
print list2 * 2
# 打印组合结果
print list2 + list3
a = 10
b = 20
# 条件语句
if a and b:
    print ("a and b 都为真")
else:
    print ("a and b 有一个不为真")
num = 3
if num == 0:
    print ("0")
elif num == 1:
    print ("1")
else:
    print(">3")



