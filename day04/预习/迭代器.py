'''
迭代器
str, list, tuple, dict, set.他们都遵循了可迭代协议。
int, bool是不可迭代对象。
'''
s = "abc"
for item in s:  # 正确的
	print(item)  # a b c

'''错误的'''
# for item in 123:  # TypeError: 'int' object is not iterable
# 	print(item)

'''注意看报错信息TypeError: 'int' object is not iterable.翻译过来就是整数类型对象是不可迭代的。iterable表示可迭代的。
表示可迭代协议。'''

s = "hello world!"
print(dir(s))  # 可以打印对象中的方法和函数
print(dir(str))  # 也可以打印类中声明的方法和函数
'''
打印结果：
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
 '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
 '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center',
  'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 
  'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
  'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 
  'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

'''在打印的结果中，寻找__iter__如果能找到，那么这个类的对象就是一个可迭代对象。'''
print("__iter__" in dir(s))  # True
print("__iter__" in dir(str))  # True
print("__iter__" in dir(tuple))  # True
print("__iter__" in dir(list))  # True
print("__iter__" in dir(dict))  # True
print("__iter__" in dir(set))  # True
print("__iter__" in dir(int))  # False
print("__iter__" in dir(bool))  # False

'''这是我们查看对象是不是可迭代对象的第一种办法，我们还可以通过isinstance()函数来查看一个对象是什么类型的。'''
from collections import Iterable, Iterator

lst = ["apple", "orange", "banana"]
lst_iter = lst.__iter__()
print(isinstance(lst, Iterable))  # True
print(isinstance(lst, Iterator))  # False
print(isinstance(lst_iter, Iterable))  # True
print(isinstance(lst_iter, Iterator))  # True

'''如果对象中有__iter__函数，那么我们认为这个对象遵守了可迭代协议。就可以获取到相应的迭代器。这里的__iter__是帮助我们获
取到对象的迭代器，使用迭代器中的__next__()来获取到一个迭代器中的元素。
for循环的工作原理到底是什么呢？
'''
str1 = "apple"
str_iter = str1.__iter__()  # 获取迭代器
print(str_iter.__next__())  # a
print(str_iter.__next__())  # p
print(str_iter.__next__())  # p
print(str_iter.__next__())  # l
print(str_iter.__next__())  # e
# print(str_iter.__next__())  # StopIteration

'''for循环的机制'''
for i in [1, 2, 3]:
	print(i)  # 1 2 3

'''使用while循环+迭代器来模拟for循环'''
lst = ["apple", "banana", "orange"]
lst_iter = lst.__iter__()
while 1:
	try:
		print(lst_iter.__next__())  # apple banana orange
	except StopIteration:
		break

'''list可以一次性把迭代器中的内容全部那空，并装载在一个新的列表中'''
str_iter = "apple".__iter__()
print(list(str_iter))  # ['a', 'p', 'p', 'l', 'e']

'''
总结：
	Iterable：可迭代对象，内部包含__iter__()函数
	Iterator：迭代器，内部包含__iter__()和__next__()
	迭代器的特点：
		1、节省内存。
		2、惰性机制。
		3、不能反复，只能向下执行。
'''

