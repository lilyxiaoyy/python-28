'''装饰器
装饰器是干嘛的呢？它是一种固定的语法。可以让我们再补修改原有函数内部代码的基础上，给函数增加新的功能。'''
def add():
	pass
def delete():
	pass
def update():
	pass
def search():
	pass

'''此时，我想给每个函数添加一个新功能，记录日志，记录一下，在xxx时间执行的xxx函数。'''
def add():
	# 记录日志的代码
	pass
def delete():
	# 记录日志的代码
	pass
def update():
	# 记录日志的代码
	pass
def search():
	# 记录日志的代码
	pass

'''
设想一下，如果我现在想更换日志格式：xxx函数在xxx时间执行了。你怎么办？
传统办法：改代码，修改每个函数。太繁琐了，如果这一段代码有n次重复，你要修改n次。
最佳办法：把记录日志的代码提取成函数，然后每个函数分别调用。
'''

def log():
	# 记录日志的代码
	pass
def add():
	log()
	pass
def delete():
	log()
	pass
def update():
	log()
	pass
def search():
	log()
	pass
'''
这样是不是好多了，我们只要修改log()函数就可以完成我们想要的结果了，但是，随着需求的进一步增加。你会发现你这几个函数没有
消停的时候了，例如，不论执行增删改查任何操作之前都要进行登录验证。
'''

def log():
	# 记录日志的代码
	pass

def add():
	while 1:
		uname = input(">>>")
		pwd = input(">>>")
		if uname == "lily" and pwd == "123":
			log()
			pass
			break
		else:
			print("密码错误")

def delete():
	log()
	pass
def update():
	log()
	pass
def search():
	log()
	pass

'''
发现没有，如果继续下去，你会发现你这个add方法永无宁日。不停的再改。原有代码一直再不断的被修改。
那怎么办呢？在程序设计是行我们的程序要遵循开闭原则
开：对添加新功能开放。
闭：对修改函数中的源代码封闭。
也就是说，在不修改源代码内部的基础上给函数添加新功能，这就需要使用我们的装饰器。
'''

'''1、装饰器雏形'''
def wrapper(fn):
	def inner():
		'''在执行fn之前'''
		fn()  # 这里是一个闭包的效果，外面函数中有一个fn：局部变量被内层函数使用。
		'''在执行fn之后'''
	return inner

def add():
	pass
def delete():
	pass
def update():
	pass
def search():
	pass

'''上面的wrapper就是一个装饰器，其实看起来没什么特别的，就是一个闭包而已。接下来看看它怎么使用。'''
add = wrapper(add)
add()

'''add = wrapper(add) 把add函数作为参数传递给wrapper。那么wrapper()中的fn就是外面的add函数，然后wrapper返回inner，此时
注意了，add这个变量被修改，重新指向inner这个函数。
此时我们用add()执行的时候，实际上执行的是inner()这个函数，而inner中执行的是fn()。fn是原来的add()饶了一大圈，执行的还是
原来的add()。
饶这么大一圈的好处和作用是什么呢?我们可以在inner函数中，访问fn()之前和之后加入你想加入的任何代码。而没有改变原来的add()。
'''

def wrapper(fn):
	def inner():
		'''在执行fn之前'''
		while 1:
			uname = input(">>>")
			pwd = input(">>>")
			if uname == "lily" and pwd == "123":
				log()
				fn()
				break
			else:
				print("密码错误")
		'''在执行fn之后'''
	return inner

def add():
	pass
def delete():
	pass
def update():
	pass
def search():
	pass
add = wrapper(add)
add()

'''add = wrapper(add)看着是真的不舒服，python提供了一种语法糖，可以帮助我们简化这句话。'''
@wrapper  # 相当于add = wrapper(add)
def add():
	pass

'''
@后面加上装饰器的名字（装饰器函数名）就是语法糖。相当于写了一个add = wrapper(add)
在上面的例子中，wrapper被称为装饰器，add和fn被称为被装饰的函数（目标函数）。
'''

'''2、被装饰的函数如果带参数怎么办？'''
def wrapper(fn):
	def inner():
		'''在执行fn之前'''
		fn()
		'''在执行fn之后'''
	return inner

@wrapper
def play_game(username, password):
	print(username, password)

play_game("lily", "123")

'''
此时，我们发现程序报错了，为什么呢？
我们执行play_game("lily", "123")其实不是原来的play_game()而是inner，而inner又没有参数，此时不符合传参的定义。
那怎么办呢？我们需要给inner添加参数，并传递给fn()
'''

def wrapper(fn):
	def inner(username, password):
		'''在执行fn之前'''
		fn(username, password)
		'''在执行fn之后'''
	return inner

'''如果被装饰的函数有很多参数呢?怎么办，我们之前学过*args和**kwargs,无敌传参。'''

def wrapper(fn):
	def inner(*args, **kwargs):
		'''在执行fn函数之前'''
		fn(*args, **kwargs)  # 把接收到的参数打散再传过去
		'''在执行fn函数之后'''
	return inner

'''
一定看清楚了，在inner()的小括号里写的是形参，表示可以接收各种参数。
在fn()位置的*args和**kwargs是实参，这里表示的是把args和kwargs打散在发送出去。
'''

'''3、被装饰的函数如果带返回值怎么办？'''
def wrapper(fn):
	def inner(*args, **kwargs):
		'''在执行fn函数之前'''
		fn(*args, **kwargs)
		'''在执行fn函数之后'''
	return inner

@wrapper
def play_game(username, password):
	print(username, password)
	return "我想学Python."

ret = play_game("lily", "123")
print(ret)  # None

'''
为什么是None呢？由于play_game函数被装饰器装饰过了，那么此时，我们执行play_game实际上执行的是inner函数，而真正执行
play_game的位置是在fn()这里。而fn()这里并没有接受返回值，inner也没有返回值。
那么对于外界访问inner的时候自然没有返回值了。
怎么办呢？
'''
def wrapper(fn):
	def inner(*args, **kwargs):
		'''在执行fn函数之前'''
		ret = fn(*args, **kwargs)
		'''在执行fn函数之后'''
		return ret  # 把fn执行之后的结果返回
	return inner

@wrapper
def play_game(username, password):
	print(username, password)
	return "我要学Python."

ret = play_game("lily", "123")
print(ret)  # 我要学Python.

'''问题解决。'''

'''4、通用装饰器写法（记住）'''
def wrapper(fn):
	def inner(*args, **kwargs):
		'''执行fn函数之前'''
		ret = fn(*args, **kwargs)
		'''执行fn函数之后'''
		return ret  # 把fn执行之后的结果返回
	return inner

'''这就是通用装饰器的写法。'''

'''5、带参数的装饰器'''
def gua(fn):
	def inner(*args, **kwargs):
		ret = fn(*args, **kwargs)
		return ret
	return inner

@gua
def play():
	pass
play()

'''此时，我们只是开挂了，开什么挂 还不知道，这里就可以选择使用带参数的装饰器了。'''

def gua_bi(kind_of_gua):
	def gua(fn):
		def inner(*args, **kwargs):
			print("我要使用%s" % kind_of_gua)
			ret = fn(*args, **kwargs)
			return ret
		return inner
	return gua  # 注意这句话，返回的是一个装饰器

@gua_bi("科比")  #  gua = gua_bi("科比") => play_1 = gua(play_1)
def play_1():
	pass

@gua_bi("独行侠")  # gua_bi
def play_2():
	pass
play_1()
play_2()

'''此时注意了，@gua_bi("科比")这句话要拆开来看。先执行的是后半段。gua_bi("科比") 这就是一个普通函数的调用，执行完这个
函数，返回的是gua。再和前面的@组合，正好是@gua。还是原来的装饰器的样子。'''

'''6、同一个函数被多个装饰器装饰'''
def wrapper1(fn):
	def inner(*args, **kwargs):
		print("before wrapper1")
		ret = fn(*args, **kwargs)
		print("before wrapper1")
		return ret
	return inner

def wrapper2(fn):
	def inner(*args, **kwargs):
		print("before wrapper2")
		ret = fn(*args, **kwargs)
		print("before wrapper2")
		return ret
	return inner

def wrapper3(fn):
	def inner(*args, **kwargs):
		print("before wrapper3")
		ret = fn(*args, **kwargs)
		print("before wrapper3")
		return ret
	return inner

@wrapper1
@wrapper2
@wrapper3
def func():
	print("target function")

func()

'''
执行结果：
before wrapper1
before wrapper2
before wrapper3
target function
before wrapper3
before wrapper2
before wrapper1
'''

'''看结果应该就能明白，wrapper1装饰的是wrapper2装饰的结果，wrapper2装饰的是wrapper3装饰的结果...以此类推。最接近目标函数
的就是wrapper3。所以目标函数之前和之后执行的是wrapper3，然后外面套上一层wrapper2,最后wrapper1。'''