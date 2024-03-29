'''
函数：对代码块和功能的封装和定义。
def 函数名():
	函数体
'''
def func():
	print("hello world")
func()


'''
函数的返回值：
1、遇到return，函数结束，函数后面的代码将不会再执行。
2、return 返回值
1）.如果不写return，那么返回的就是None。
2）.如果return后面写了一个值，则调用者可以接收一个结果。
3）.如果return后面写了多个结果，则调用者可以接收一个tuple，调用者可以直接结构成多个变量。

def func(形参):
	函数体

func(实参)

实参：位置参数和关键字参数
形参：位置形参和默认值参数

1、位置参数。
练习：编写函数，给函数传递两个参数a,b。比较a,b的大小，返回a,b中最大的那个数。
'''
def my_max(a, b):
	return a if a > b else b  # 三元运算符


ret = my_max(5, 8)
print(ret)  # 8

'''
2、关键字参数
'''
def my_max(a, b):
	return a if a > b else b


ret = my_max(b=4, a=8)
print(ret)  # 8

'''
3、混合参数
注意：在使用混合参数的时候，关键字参数必须在位置参数后面。
'''
def my_max(a, b):
	return a if a > b else b


ret = my_max(9, b=8)
print(ret)
# ret = my_max(b=8, 9)  # 报错，最开始使用了关键字参数，那么后面的位置就串

'''
总结：在实参的角度来看，分为三种：
	1、位置参数。
	2、关键字参数。
	3、混合参数，位置参数必须在关键字参数前面。
'''


'''
在形参角度看
1、位置参数
'''
def my_max(a, b):
	return a if a > b else b


ret = my_max(4, 6)
print(ret)  # 6

'''
2、默认值参数
注意：必须先声明位置参数，才能声明默认值参数。
'''
def my_max(a, b=10):
	return a if a > b else b


ret = my_max(3)
print(ret)  # 10


'''
动态传参
动态接收位置参数，在形参位置编写*表示接收任意内容。
'''
def func(*args):  # 多个参数传递进去，收到的内容是元组tuple
	print(args)  # ('aa', 'bb')


func("aa", "bb")


'''
动态接收参数的时候要注意：动态参数必须在位置参数后面
'''
def func(*args, a, b):
	print(args)


# func("aa", "bb", "cc", "dd") # 报错：TypeError: func() missing 2 required keyword-only arguments: 'a' and 'b'
'''
这时程序运行会报错，因为前面传递进去的所有位置参数都被*args接收了，a和b永远接收不到参数。
修改为：
'''
func("aa", "bb", a="cc", b="dd")   # ('aa', 'bb')
'''
这个时候a和b就有值了，但是这样写，位置参数就不能用了，所以，我们要先写位置参数，然后再用动态参数。
'''
def func(a, b, *args):
	print(args)


func("aa", "bb", "cc", "dd")  # ('cc', 'dd')

'''
位置参数、动态参数、默认值参数
'''
def func(a, b, c="abc", *args):
	print(a, b, c, args)


func("a1", "a2", "a3", "a4", "a5")  # a1 a2 a3 ('a4', 'a5')
'''
我们发现默认值参数写在动态参数的前面，默认值没有生效，除非，动态参数和默认值参数都不进行传参。
修改上面的代码：
'''
def func(a, b, *args, c="abc"):
	print(a, b, args, c)


func("a1", "a2", "a3", "a4", "a5")  # a1 a2 ('a3', 'a4', 'a5') abc

'''
这时候我们发现默认值生效了。如果不给关键字传参，默认值是永远都生效的。
顺序：位置参数，动态参数*，默认值参数

在python中，动态接收位置参数使用*args，args是一个tuple。
动态接收关键字参数使用**kwagrs，kwargs是一个dict。
下面看动态接收关键字参数
'''
def func(**kwargs):
	print(kwargs)

func(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
func(a=1, b=2)  # {'a': 1, 'b': 2}

'''
顺序的问题，在函数调用的时候，如果先给出关键字参数，则整个参数列表会报错
'''
def func(a, b, c, d):
	print(a, b, c, d)


# func(1, 2, c=3, 4)  # 报错： SyntaxError: positional argument follows keyword argument
'''
所以，实参的顺序，关键字参数必须在位置参数后面。形参接收的时候也是这个顺序，位置参数必须在关键字参数前面。
'''
def func(a, b, *args, d=8, **kwargs):
	print(a, b, args, d, kwargs)


func(1, 2, 3, 4, 5, 6, name="lily", age=18)  # 1 2 (3, 4, 5, 6) 8 {'name': 'lily', 'age': 18}
func(1, 2, 3, 4, 5, 6, d=6, name="lily", age=18)  # 1 2 (3, 4, 5, 6) 6 {'name': 'lily', 'age': 18}
func(1, 2, 3, 4, 5, 6, name="lily", age=18, d=6)  # 1 2 (3, 4, 5, 6) 6 {'name': 'lily', 'age': 18}
'''
最终形参的顺序：位置参数 > *args > 默认值参数 > **kwargs
形参里的*的作用，*表示聚合成tuple，**表示聚合成dict。
实参里的*的作用，*表示打散成具体的元素，**表示打散成关键字传参的形式
'''
def func(*args):
	print(args)

str1 = "abc"
lst = ["apple", "orange"]
func(*str1, *lst)  # ('a', 'b', 'c', 'apple', 'orange')


'''
形参里的*的作用，*表示聚合成tuple，**表示聚合成dict。
实参里的*的作用，*表示打散成具体的元素，**表示打散成关键字传参的形式
'''
def func(**kwargs):
	print(kwargs)


dic = {"name": "lily", "age": 18}
func(**dic)  # {'name': 'lily', 'age': 18}


'''
测试版本
'''
def func(a, b, *args, c=8, **kwargs):
	print(a, b, args, c, kwargs)


func(1, 2, 3, 4, name="lily", c=6, age=19)  # 1 2 (3, 4) 6 {'name': 'lily', 'age': 19}

'''
总结：
函数的基本语法：
def 函数名（形参1, 形参2......）：
	函数体
	return 值1, 值2，值3...
	

函数名(实参)

形参：函数声明的位置的变量，准备用来接收数据的。
实参：在调用函数的时候给函数传递的具体的值。

返回值：
	如果什么都不写，默认在函数结束的时候返回None。
	如果只写了个return，则遇见return结束函数运行，返回None。
	如果写了return 值。表示只有一个返回值。
	如果写了return 值1，值2， 值3... 表示可以有多个返回值，返回的时候回自动打包成元组。
	
参数：
	形参
		1.位置参数
		2.*args：动态接收位置参数
		3.默认值参数
		4.**kwargs：动态接收关键字参数
		顺序：位置 > *args > 默认值 > **kwargs
	
	实参
		1.位置参数
		2.关键字参数
		3.混合参数
		
无敌传参：
def func(*args, **kwargs):  # 什么都能传进去
	pass
	
*和** 在形参表示聚合，在实参表示打散	
'''

'''当知道有几个参数的时候，就不使用*和**'''
dic = {"name": "lily", "age": 18}
def func(d):
	for k, v in d.items():
		print(k, v)

func(dic)
'''
打印结果：
name lily
age 18

总结：这里的实参func(dic)属于位置参数，定义函数的地方def func(d)这里的d也是位置参数，因为实参dic是字典的类型，
所以，形参d有是字典类型。
实参是什么类型，形参就是什么类型，只有不确定变量的数量的时候，才会使用*和**
'''

'''当函数有一个形参，并且参数是列表的情况'''
def func(lst):
	print(lst)   # ['apple', 'banana', 'orange']
	print(type(lst))  # <class 'list'>

lst1 = ["apple", "banana", "orange"]
func(lst1)

'''当函数有一个形参，并且参数是元组的情况'''
def func(tup):
	print(tup)  # ('a', 'b', 'c')
	print(type(tup))  # <class 'tuple'>

tup1 = ("a", "b", "c")
func(tup1)

'''当函数有一个形参，并且参数是集合的情况'''
def func(s):
	print(s)  # {'b', 'a', 'c' }
	print(type(s))  # print(s)  # {'b', 'a', 'c' }


set1 = {"a", "b", "c"}
func(set1)

'''当函数有一个形参，并且参数是一个函数名的情况'''
def wrapper(fn):
	print(fn)  # <function add at 0x00000000029A4A60>
	print(type(fn))  # <class 'function'>

def add():
	print("我是新增功能")

wrapper(add)