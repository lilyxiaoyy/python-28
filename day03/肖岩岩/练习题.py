'''
写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
PS:字典中的value只能是字符串或列表
'''
# def func(**kwargs):  # 形参里的**表示聚合
# 	new_dic = {}
# 	for k, v in kwargs.items():
# 		if len(v) > 2:
# 			new_dic[k] = v[:2]
# 		else:
# 			new_dic[k] = v
# 	return new_dic
#
#
# dic = {"k1": "v1v1", "k2": [11, 22, 33, 44], "k3": "a", "k4": "ab"}
# ret_dic = func(**dic)  # 实参里的**表示打散
# print(ret_dic)


'''
写函数，此函数只接收一个参数且此参数必须是列表数据类型，
此函数完成的功能是返回给调用者一个字典，
此字典的键值对为此列表的索引及对应的元素。
例如：
	传入的列表为：[11, 22, 33]
	返回的字典为 {0:11, 1:22, 2:33}
'''
# def func(*args):
# 	dic = {}
# 	for i, v in enumerate(args):
# 		dic[i] = v
# 	return dic
#
#
# lst = [11, 22, 33, "aa", "bb", "cc"]
# ret = func(*lst)
# print(ret)


'''
写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作。
'''
# import os
#
#
# def func(file, old_content, new_content):
# 	file_temp = "%s-temp" % file
# 	with open(file, "r", encoding="utf-8") as f,\
# 			open(file_temp, "w", encoding="utf-8") as f2:
# 		for line in f:
# 			line = line.replace(old_content, new_content)
# 			f2.write(line)
# 	os.remove(file)
# 	os.rename(file_temp, file)
#
#
# func("1.txt", "上海", "北京")


'''
读代码，回答：代码中，打印出来的值a, b, c分别是什么？为什么？
a = 10
b = 20
def test5(a, b):
	print(a, b)
c = test5(b, a)
print(c)
'''
# a = 20  # 因为调用函数时，传递的实参是b
# b = 10  # 因为调用函数时，传递的实参是a
# c = None  # 因为函数没有return 返回值，默认返回值为None


'''
读代码，回答：代码中，打印出来的值a, b, c分别是什么？为什么？
a = 10
b = 20
def test5(a, b):
	a = 3
	b = 5
	print(a, b)
c = test5(b, a)
print(c)
'''
# a = 3  # 因为a在函数体内重新赋值为3
# b = 5  # 因为b在函数体内重新赋值为5
# c = None  # 因为函数没有return返回值，默认返回值为None


'''
写函数，传入韩世忠多个实参（均为可迭代对象如字符串，列表，元组，集合等），
将每个实参的每个元素依次添加到函数的动态参数args里面，
例如 传入函数两个参数[1, 2, 3] (22, 33)最终args为(1, 2, 3, 22, 33)
'''
# def func(*args):  # 形参中的*表示聚合
# 	print(args)
#
#
# lst = [1, 2, 3]
# tup = (22, 33)
# func(*lst, *tup)  # 实参中的*表示打散
# s = {"a", "b"}
# str1 = "老男孩"
# func(*lst, *tup, *s, *str1)


'''
写函数，传入函数中多个实参（实参均为字典），将每个实参的键值对依次添加到函数的动态实参kwargs里面。
例如 传入函数两个参数{"name": "alex"} {"age": 1000}最终kwargs为{"name":"alex", "age": 1000}
'''
# def func(**kwargs):
# 	print(kwargs)
#
#
# dic1 = {"name": "alex"}
# dic2 = {"age": 1000}
# func(**dic1, **dic2)


'''
下面代码成立么？如果不成立为什么报错？怎么解决？
题目一：
a = 2
def wrapper():
	print(a)
wrapper()

题目二：
a = 2
def wrapper():
	a += 1
	print(a)
wrapper()

题目三：
def wrapper():
	a = 1
	def inner():
		print(a)
	inner()
wrapper()

题目四：
def wrapper():
	a = 1
	def inner():
		a += 1
		print(a)
	inner()
wrapper()
'''
# 题目一成立

# 题目二不成立， 因为函数体内的a不能改变全局变量a的值，解决如下：
# a = 2
# def wrapper():
# 	global a
# 	a += 1
# 	print(a)
# wrapper()

# 题目三成立

# 题目四不成立，因为inner函数内不能修改局部变量a的值，解决如下：
# def wrapper():
# 	a = 1
# 	def inner():
# 		nonlocal a
# 		a += 1
# 		print(a)
# 	inner()
# wrapper()


'''
写函数，传入n个数，返回字典{"max": 最大值, "min": 最小值}
例如：如：min_max(2, 5, 7, 8, 4)返回：{"max": 8, "min": 2}
此题用到max(),min()内置函数
'''
# def min_max(*args):
# 	dic = {}
# 	dic['max'] = max(args)
# 	dic['min'] = min(args)
# 	return dic
#
#
# ret = min_max(2, 5, 7, 8, 4)
# print(ret)


'''
写函数，传入一个参数n，返回n的阶乘
例如： cal(7) 计算7*6*5*4*3*2*1
'''
# def cal(n):
# 	ret = 1
# 	if n >= 1 and type(n) == int:
# 		for i in range(1, n+1):
# 			ret *= i
# 	else:
# 		ret = "无效的参数，请传入一个正整数"
# 	return ret
#
#
# ret = cal(7)
# print(ret)