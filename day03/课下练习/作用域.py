'''
globals()查看全局作用域
locals()查看当前作用域
'''
a = 10
def func():
	a = 20
	print(a)


func()  # 20
print(a)  # 10
'''
注意，在python中，变量是遵循就近原则的。
在函数外面的变量被称为全局变量，它的作用域是整个py文件。
在函数内部的变量被称为局部变量，作用范围仅限于函数内部。
我们可以通过globals()和locals()查看全局和局部作用域中的内容。
'''
a = 10
def func():
	a = 40
	b = 20
	def abc():
		print("abc")
	print(a, b)
	print(globals())
	print(locals())


func()  # 40 20
# {......, 'a': 10, 'func': <function func at 0x00000000029A58C8>}
# {'abc': <function func.<locals>.abc at 0x00000000029A5950>, 'b': 20, 'a': 40}


'''
global和nonlocal关键字
'''
a = 10
def func():
	a = 20
	print(a)


func()  # 20
'''
这种情况是正常的。接着看下面的情况：
'''
a = 10
def func():
	# a += 1  # 报错：UnboundLocalError: local variable 'a' referenced before assignment
	print(a)


func()
'''
注意报错那句话，这句话相当于a = a + 1先计算右边，右边会把全局变量a引入进来使用，然后重新赋值给a，但是，python中不允许函
数内部改变外面变量的值，这样做很不安全，python规定，在函数内部想要修改全局变量，必须使用global关键字把外面的变量引入才可
以进行修改（赋值）。
'''
a = 10
def func():
	global a
	a += 1
	print(a)


func()  # 11
'''
nonlocal也是一样的操作，它负责在内层函数中引入外层函数的局部变量。
'''
a = 10
def func():
	a = 20
	def inner():
		nonlocal a
		a = 30
		print(a)
	inner()
	print(a)


print(a)  # 10
func()  # 30 30
'''
不加nonlocal的情况
'''
a = 10
def func():
	a = 20
	def inner():
		a = 30
		print(a)
	inner()
	print(a)


print(a)  # 10
func()  # 30 20
