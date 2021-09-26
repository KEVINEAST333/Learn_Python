# coding=utf-8
# 打开一个文件
# pythonI/O操作
fo = open("/Users/kevinwang/PycharmProjects/pythonProject/file/foo.txt", "a")
# file object = open(file_name [, access_mode][, buffering])
# 各个参数的细节如下：
# file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
# access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。如果将buffering的值设为大于1的整数，
# 表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
print "文件名：", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
# close 方法
# fo.close()
# write方法
fo.write("吃饭\n")
fo.close()
