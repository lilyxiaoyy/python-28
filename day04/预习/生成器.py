'''生成器
生成器的本质就是迭代器，在python中有两种方式来获取生成器：
	1、通过生成器函数
	2、通过生成器表达式来实现生成器
首先，我们先看一个很简单的函数：
'''
def func():
	print("111")
	return 222

ret = func()
print(ret)
'''
打印结果：
111
222
'''

'''将函数中的return换成yield就是生成器'''
def func():
	print("111")
	yield 222

ret = func()
print(ret)
'''
打印结果：
<generator object func at 0x00000000005D0D58>
'''

'''
运行的结果和上面不一样，为什么呢？由于函数中存在了yield。那么这个函数就是一个生成器函数。这个时候，我们再执行和这个函数
的时候，就不再是函数的执行了，而是获取这个生成器。如何使用呢？想想迭代器，生成器的本质就是迭代器。所以，我们可以直接执行
__next__()来执行以下生成器。
'''

def func():
	print("111")
	yield 222

gener = func()  # 这个时候函数不会执行，而是获取到生成器
ret = gener.__next__()  # 这个时候函数才会执行，yield的作用和return一样，也是返回数据
print(ret)
'''
执行结果：
111
222
'''

'''我们可以看到，yield和return有什么区别呢？yield是分段来执行一个函数，return直接停止执行函数。'''
def func():
	print("111")
	yield 222
	print("333")
	yield 444

gener = func()
ret = gener.__next__()  # 111
print(ret)  # 222
ret2 = gener.__next__()  # 333
print(ret2)  # 444
# ret3 = gener.__next__()  # StopIteration
'''最有一个yield执行完毕，再次__next__()程序报错 StopIteration'''

'''当程序执行完最后一个yield，那么后面继续进行__next__()程序会报错。'''
def cloth():
	lst = []
	for i in range(10):
		lst.append("衣服"+str(i))
	return lst

cl = cloth()
print(cl)  # ['衣服0', '衣服1', '衣服2', '衣服3', '衣服4', '衣服5', '衣服6', '衣服7', '衣服8', '衣服9']

'''改用生成器函数'''
def cloth():
	for i in range(10):
		yield "衣服"+str(i)

cl = cloth()
print(cl.__next__())  # 衣服0
print(cl.__next__())  # 衣服1
print(cl.__next__())  # 衣服2
print(cl.__next__())  # 衣服3

'''区别：第一种是直接一次性全部拿出来，会很占用内存。第二种使用生成器，一次就一个，用多少生成多少，生成器是一个一个的指
向下一个，不会回去，__next__()到哪，指针就到哪，下一次继续获取指针指向的值。'''

'''send方法，send和__next__()一样都可以让生成器执行到下一个yield。'''
def fruit():
	print("苹果")
	a = yield "apple"
	print("a=", a)
	b = yield "banana"
	print("b=", b)
	c = yield "cherry"
	print("c=", c)
	yield "over"

gen = fruit()  # 获取生成器
ret1 = gen.__next__()  # 苹果
print(ret1)  # apple
ret2 = gen.send("喜欢")  # a= 喜欢
print(ret2)  # banana
ret3 = gen.send("很喜欢")  # b= 很喜欢
print(ret3)  # cherry
ret4 = gen.send("非常喜欢")  # c = 非常喜欢
print(ret4)  # over

'''
send和__next__()区别：
	1、send和next()都是让生成器向下走一次
	2、send可以给上一个yield的位置传递值，不能给最后一个yield发送值，在第一次执行生成器代码的时候不能使用send()
'''

'''生成器可以使用for循环来循环获取内部的元素'''
def func():
	print(111)
	yield 222
	print(333)
	yield 444
	print(555)
	yield 666

gen = func()
for i in gen:
	print(i)
'''
打印结果：
111
222
333
444
555
666
'''
