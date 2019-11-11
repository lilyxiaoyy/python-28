# -*- coding: utf-8 -*-
'''
在python中，所有空的东西都可以表示False, 空字符串、空列表、空字典、空集合、空元组
数字中只有0是False，其他都是True
'''
print(bool(""))	 # False
print(bool(" "))  # True
print(bool(list()))  # False
print(bool(tuple()))  # False
print(bool(0))  # False
print(bool(-1))  # True