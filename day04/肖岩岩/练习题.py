'''1、写装饰器，控制函数被调用的频率，要求：5秒钟执行一次。少于5秒钟直接打印警告信息。'''
# import time
#
# def wrapper(fn):
# 	def inner(*args, **kwargs):
# 		'''目标函数执行前'''
# 		start_time = time.time()
# 		print("开始执行目标函数")
# 		ret = fn(*args, **kwargs)
# 		'''目标函数执行后'''
# 		end_time = time.time()
# 		if end_time - start_time < 5:
# 			print("警告：少于5秒钟。我需要睡%s秒。" % (5 - end_time + start_time))
# 			time.sleep(5 - end_time + start_time)
# 		print("结束执行目标函数")
# 		return ret
# 	return inner
#
#
# @wrapper
# def func():
# 	print("我是目标函数")
#
# func()


'''2、写装饰器，通过一次调用使函数执行5次。'''
# def wrapper(fn):
# 	def inner(*args, **kwargs):
# 		'''目标函数执行前'''
# 		for i in range(5):
# 			ret = fn(*args, **kwargs)
# 		return ret
# 		'''目标函数执行后'''
# 		return ret
# 	return inner
#
#
# @wrapper
# def func():
# 	print("我是目标函数")
#
# func()

'''3、（重点、难点）写装饰器，要求：被装饰的函数在执行的时候首先要判断登录状态，如果是已经登录状态，则直接执行，否则提示
用户去执行登录操作，直到用户登录成功为止。'''
# username = "lily"
# password = "123"
# login_status = False
#
# def login(fn):
# 	def inner(*args, **kwargs):
# 		'''目标函数执行前'''
# 		global login_status
# 		if login_status:
# 			ret = fn(*args, **kwargs)
# 			return ret
# 		else:
# 			num = 3
# 			for i in range(num, 0, -1):
# 				user = input("Username:").strip()
# 				pwd = input("Password:").strip()
# 				if username == user and password == pwd:
# 					print("登录成功")
# 					login_status = True
# 					ret = fn(*args, **kwargs)
# 					return ret
# 				else:
# 					if i > 1:
# 						print("用户名或密码错误，你还有%s次机会！" % (i -1))
# 			else:
# 				print("登录错误次数超过%s次，程序退出！" % num)
# 	return inner
#
# @login
# def add():
# 	print("我是新增函数")
#
# @login
# def upd():
# 	print("我是修改函数")
#
# add()
# upd()

'''4、看代码写出结果'''
# def say_hi(func):
# 	def wrapper(*args, **kwargs):
# 		print("HI")
# 		ret = func(*args, **kwargs)
# 		print("BYE")
# 		return ret
# 	return wrapper
#
#
# def say_yo(func):
# 	def wrapper(*args, **kwargs):
# 		print("YO")
# 		return func(*args, **kwargs)
# 	return wrapper
#
#
# @say_hi
# @say_yo
# def func():
# 	print("ROCK & ROLL")
#
# func()

'''
打印的结果：
HI
YO
ROCK & ROLL
BYE
'''

'''5、一道面试题'''
def nums():
	return [lambda x: x * i for i in range(4) ]
print([m(2) for m in nums()])
'''
分析：
print([m(2) for m in nums()]) 打印的是一个列表
nums()的结果是 [lambda x: x*i for i in range(4)] i是0到3 
[0, 2, 4]
'''