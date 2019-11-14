'''
while 条件：
	循环体
else:循环在正常情况跳出之后会执行这里
'''
i = 1
while i < 6:
	print(i)
	i = i + 1
else:
	print("hello")
'''
打印结果：
1
2
3
4
5
hello
'''

'''满足while条件，不满足else的情况，不执行else'''
i = 1
while i < 11:
	print(i)
	if i == 3:
		break
	i = i + 1
else:
	print("hello")
'''
打印结果：
1
2
3
'''


'''
注意：如果循环是通过break退出的，那么while后面的else将不会被执行。只有在while条件判断是假的时候才会执行这个else。
'''

for i in range(1, 6):
	print(i)
	i = i + 1
else:
	print("hello")
'''
打印结果：
1
2
3
4
5
hello
'''

'''总结: while...else和for...else是一样的用法。'''

lst = [1, 2, 3, 4, 5]
for i in lst:
	if i == 6:
		print(i, "if")
		break
else:
	print(i, "else")  # 5 else