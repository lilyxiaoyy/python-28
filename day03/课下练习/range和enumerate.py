'''
range(n) 指从0到n-1
range(m, n) 指从m到n-1
range(m, n, step) 当step为正数时，指从m到n-1，每step个取一个数。当step为负数时，且m>n，指从m到n-1，每step个取一个数。
range可以通过for循环能帮我们获取到一组数据。
'''
for num in range(10):
	print(num)  # 0 1 2 3 4 5 6 7 8 9


for num in range(1, 10, 2):
	print(num)  # 1 3 5 7 9


for num in range(10, 1, -2):
	print(num)  # 10 8 6 4 2

'''
range最大的作用是可以循环出列表中每一个元素的索引
'''
lst = ["apple", "banana", "orange", "watermelon"]
for i in range(len(lst)):
	print(i)  # 0 1 2 3

'''
enumerate(lst)的使用
'''
lst = ["apple", "banana", "orange", "watermelon"]
for i, v in enumerate(lst):
	print(i, v)
'''
打印结果：
0 apple
1 banana
2 orange
3 watermelon
'''

'''enumerate(lst, n) 从n开始计数'''
lst = ["apple", "banana", "orange", "watermelon"]
for i, v in enumerate(lst, 1):
	print(i, v)
'''
打印结果：
1 apple
2 banana
3 orange
4 watermelon
'''