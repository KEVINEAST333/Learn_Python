# coding=utf-8
# while循环
count = 0
while count < 10:
    print count,
    count += 1
# continue 和 break
i = j = 1
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # continue跳到循环判定处
    print i,
while j < 10:
    j += 1
    if j == 7:
        break
# for循环可以遍历任何序列的项目，如一个列表或者一个字符串
for char in "I LOVE YOU":
    print ("当前字母：%s" % char)
arr = ["a", "b", "c", "d"]
for c in arr:
    print c
for index in range(len(arr)):
    print arr[index],
# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
for i in range(1, 10):
    print i,
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式
# 迭代器有两个基本的方法：iter() 和 next()。
list333 = ["z", "x", "c", "v"]
it = iter(list333)
print (next(it))
