# -*- coding: utf-8 -*-
'''
%s 占位，字符串（所有的数据类型都可以传递给%s）
%d 占位整数
%f 占位小数
'''
name = "lily"
num = 2
str1 = "%s每天吃%s个苹果" % (name, num)  # 这种方式的缺点是太长容易串
str2 = f"{name}每天吃{num}个苹果"  # 这种方式只有python3.5以上的版本才会支持
print(str1)
print(str2)
