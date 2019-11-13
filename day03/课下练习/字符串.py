'''
一、字符串
字符串是不可变的对象，所以任何操作对原字符串是不会有任何影响的。
不可变的对象一共有四种：str、int、bool、tuple
1、切片和索引
1.1.索引，索引就是下标，下标从0开始
'''
# s1 = "中国"
# print(len(s1))  # 字符串的长度2
# print(s1[0])  # 中
# print(s1[1])  # 国
# print(s1[-1])  # 国，表示倒数
# print(s1[-2])  # 中，倒数第二个

'''
1.2.切片，可以使用下标来截取部分字符串的内容
语法：str[start: end]
规则：顾头不顾尾，从start开始截取，截取到end位置，但不包括end
'''
s2 = "我要学Python"
print(s2[0:3])  # 从0获取到3，不包括3. 结果：我要学
print(s2[2:5])  # 从2获取到5，不包括5，结果：学Py
print(s2[4:])  # 从4到最后，结果为：ython
print(s2[:])  # 从头获取到最后，结果：我要学Python

print(s2[-1:-5])  # 从-1获取到-5 这样是获取不到任何结果的
print(s2[-5:-1])  # 从-5获取到-1，结果：ytho
print(s2[-5:])  # 从-5获取到最后，结果：ython
print(s2[:-1])  # 这是获取到倒数第一个，结果：我要学Pytho

print(s2[1:5:2])  # 从第一个开始取，取到第5个，每2个取1个，结果：要P
print(s2[:5:2])  # 从头开始到第五个，每两个取一个，结果：我学y
print(s2[4::2])  # 从第4个开始取到最后，每两个取一个，结果：yhn
print(s2[-5::2])  # 从倒数第5个开始取，取到最后，每两个取一个，结果：yhn

print(s2[-1:-5:-1])  # 从倒数第一个取到倒数第五个，从右向左取值，结果：noht
print(s2[-5::-3])  # 从倒数第5个取到开头，每3个取一个，结果为：y要
'''
步长：如果是正数，则从左往右取。如果是负数，则从右往左取，默认是1。
切片语法：
str[start:end:step]
start：起始位置
end：结束位置
step：步长
'''

'''
2、大小写转来转去
'''
s1 = "hello world!"
ret = s1.capitalize()  # 首字母大写
print(s1)  # hello world!
print(ret)  # Hello world!

ret = s1.lower()  # 全部转换成小写
print(ret)  # hello world!

ret = s1.upper()  # 全部转换成大写
print(ret)  # HELLO WORLD!

ret = s1.swapcase()  # 大小写互相转换
print(ret)  # HELLO WORLD!

s1 = "hello, world"
ret = s1.title()  # 每个被特殊字符隔开的字母首字母大写
print(ret)  # Hello, World

'''
3、切来切去
'''
s1 = "中国"
ret = s1.center(10, "*")  # 拉长成10，把原字符串放中间，其余位置补*
print(ret)  # ****中国****

s1 = "中国\t好"
print(s1)  # 中国	好
print(s1.expandtabs())  # 可以改变\t的长度，默认长度更改为8，结果：中国      好

s1 = " hello world "
ret = s1.strip()  # 去掉左右两端的空格
print(ret)  # hello world

ret = s1.lstrip()  # 去掉左边的空格
print(ret)  # hello world

ret = s1.rstrip()  # 去掉右边的空格
print(ret)  #  hello world

'''
4、字符串替换replace()
'''
s1 = "apple_banana_orange_strawberry"
ret = s1.replace("orange", "桔子")
print(ret)  # apple_banana_桔子_strawberry

ret = s1.replace("_", "#", 2)  # 把_替换成#，替换2个
print(ret)  # apple#banana#orange_strawberry

'''
5、字符串切割split()
'''
s1 = "apple_banana_orange_strawberry"
ret = s1.split("_")
print(ret)  # ['apple', 'banana', 'orange', 'strawberry']

'''
6、字符串拼接join()
'''
lst = ['apple', 'banana', 'orange', 'strawberry']
ret = ','.join(lst)
print(ret)  # apple,banana,orange,strawberry

'''
7、startswith()判断是否以...开头
'''
s1 = "apple"
ret = s1.startswith('a')  # 判断是否以a开头
print(ret)  # True

ret = s1.endswith('e')  # 判断是否以h结尾
print(ret)  # True

'''
8、计数count()
'''
s1 = "banana"
ret = s1.count("a")  # 查找a出现的次数
print(ret)  # 3

'''
9、查找索引find()和index()
'''
s1 = "banana"
ret = s1.find("a")  # 查找a的索引号
print(ret)  # 1
ret = s1.find("m")  # 找不到，返回-1
print(ret)  # -1

ret = s1.index("a")  # 查找a的索引号
print(ret)  # 1
# ret = s1.index("m")  # 找不到报错：ValueError: substring not found

'''
10、isdigit()判断是否是数字
'''
s1 = "1234"
ret = s1.isdigit()
print(ret)  # True

'''
11、字符串的长度len()
'''
s1 = "hello world"
ret = len(s1)
print(ret)  # 11

'''
12、字符串是可迭代对象
'''
s1 = "hello world"
for i in s1:
	print(i)
'''
打印结果：
h
e
l
l
o
 
w
o
r
l
d
'''



