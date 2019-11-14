'''列表'''
lst = [1, "apple", "bb"]
'''
列表相对于字符串，不仅可以存放不同的数据类型，而且可以存放大量的数据。32位Python可以存放：536870912个元素，64位可以存放：
115291504606846975个元素。而且列表是有序的（按照你保存的顺序），有索引，可以切片方便取值。
'''

'''1、列表的索引'''
lst = ["apple", "banana", "orange", "strawberry"]
print(lst[0])  # apple
print(lst[1])  # banana
print(lst[-1])  # strawberry

lst[2] = "桔子"  # 注意，列表是可以发送改变的，这里和字符串不一样
print(lst)  # ['apple', 'banana', '桔子', 'strawberry']

s1 = "apple"
# s1[0] = "A"  # TypeError: 'str' object does not support item assignment
print(s1)

'''2、列表的切片'''
lst = ["apple", "banana", "orange", "strawberry"]
print(lst[0:3])  # ['apple', 'banana', 'orange']
print(lst[:3])  # ['apple', 'banana', 'orange']

print(lst[1::2])  # ['banana', 'strawberry']
print(lst[2::-1])  # ['orange', 'banana', 'apple']
print(lst[-1:-3:-2])  # ['strawberry']

'''字符串倒序'''
s1 = "apple"
print(s1[::-1])  # elppa

'''
str[start:end:step]
start：开始索引
end：结束索引，顾头不顾尾，取不到end
step：步长，掌握方向的，当step为正数时，start开始从左向右取；当step为负数时，start开始从右向左取。
'''

'''
3、添加列表元素 
append(item) 添加到最后一个
insert(index, item) 根据索引位置添加
extend()
'''
lst = ["apple", "banana", "orange"]
print(lst)  # ['apple', 'banana', 'orange']
lst.append("strawberry")  # ['apple', 'banana', 'orange', 'strawberry']
print(lst)

# lst = []
# while True:
# 	content = input("请输入你要录入的员工信息，输入Q退出：")
# 	if content.upper() == "Q":
# 		break
# 	lst.append(content)
# print(lst)
'''
请输入你要录入的员工信息，输入Q退出：lily
请输入你要录入的员工信息，输入Q退出：lucy
请输入你要录入的员工信息，输入Q退出：tom
请输入你要录入的员工信息，输入Q退出：q
['lily', 'lucy', 'tom']
'''

lst = ["apple", "banana", "orange"]
lst.insert(1, "strawberry")
print(lst)  # ['apple', 'strawberry', 'banana', 'orange']

'''迭代添加'''
lst = ["apple", "banana"]
lst.extend(["orange", "strawberry"])
print(lst)  # ['apple', 'banana', 'orange', 'strawberry']

'''
4、删除列表元素
pop()删除最后一个元素
pop(index)根据索引号删除元素
remove(item) 删除指定的元素，当删除的元素不存在时，会报错。
'''
lst = ["apple", "banana", "orange", "strawberry"]
print(lst)  # ['apple', 'banana', 'orange', 'strawberry']
deleted = lst.pop()
print(deleted)  # strawberry
print(lst)  # ['apple', 'banana', 'orange']

del2 = lst.pop(2)
print(del2)  # orange
print(lst)  # ['apple', 'banana']

lst.remove("apple")
print(lst)  # ['banana']
# lst.remove("wahaha")  # ValueError: list.remove(x): x not in list
print(lst)  # ['banana']

'''清空列表'''
lst.clear()
print(lst)  # []

'''使用切片删除列表元素'''
lst = ["apple", "banana", "orange", "strawberry"]
del lst[1:3]
print(lst)  # ['apple', 'strawberry']

'''5、修改列表元素'''
lst = ["apple", "banana", "orange", "strawberry"]
lst[0] = "苹果"
print(lst)  # ['苹果', 'banana', 'orange', 'strawberry']

'''
使用切片修改列表元素，如果步长不是1，要注意，元素的个数
报错：ValueError: attempt to assign sequence of size 1 to extended slice of size 2
值错误：尝试将大小为1的序列分配给大小为2的扩展切片 
'''
lst[:3:3] = ["香蕉"]
# lst[:3:3] = "香蕉"  # 报错：ValueError: attempt to assign sequence of size 2 to extended slice of size 1
print(lst)  # ['香蕉', 'banana', 'orange', 'strawberry']

'''如果切片没有步长或者步长是1，则不用关心个数'''
lst[1:3] = ["桔子"]
print(lst)  # ['香蕉', '桔子', 'strawberry']

'''
6、查询列表元素
列表是一个可迭代对象，所以可以进行for循环
'''
lst = ["apple", "banana", "orange", "strawberry"]
for item in lst:
	print(item)

'''
打印结果：
apple
banana
orange
strawberry
'''

'''7、统计列表中指定元素的个数count()'''
lst = ["apple", "banana", "orange", "banana"]
c = lst.count("banana")
print(c)  # 2

'''
8、列表排序
sort()
reverse()
'''
lst = [5, 2, 6, 8, 1]
lst.sort()  # 排序，默认升序
print(lst)  # [1, 2, 5, 6, 8]
lst.sort(reverse=True)  # 排序，倒序
print(lst)  # [8, 6, 5, 2, 1]

lst = ["apple", "banana", "apple", "orange"]
print(lst)  # ['apple', 'banana', 'apple', 'orange']
lst.reverse()  # 倒序
print(lst)  # ['orange', 'apple', 'banana', 'apple']

'''9、列表的长度len()'''
lst = ["apple", "banana", "orange"]
l = len(lst)
print(l)  # 3

'''10、列表循环的时候不能删除'''
lst = ["apple", "pear", "peach", "pineapple", "banana"]
for item in lst:
	if item.startswith("p"):
		lst.remove(item)
print(lst)  # ['apple', 'peach', 'banana']
'''
为什么会这样呢？原因是：当删除掉第一个元素之后，后面的元素就向前移动了一次，而for循环还要向后走一次。完美错过了"pear"这
个元素。我们需要把要删除的内容先保存在一个新列表中，然后循环这个新列表，去删除原来的数据列表。
正确的做法
'''
lst = ["apple", "pear", "peach", "pineapple", "banana"]
new_lst = []
for item in lst:
	if item.startswith("p"):
		new_lst.append(item)

for item in new_lst:
	lst.remove(item)
print(lst)  # ['apple', 'banana']


'''也可以这样'''
lst = ["apple", "pear", "peach", "pineapple", "banana"]
lst_temp = lst[:]
for item in lst_temp:
	if item.startswith("p"):
		lst.remove(item)
print(lst)  # ['apple', 'banana']
'''
结论：python中的列表和字典在循环的时候，不能删除自身中的元素，列表虽然不报错，但是删不干净。解决方案都一样，把要删除的内
容保存在一个新列表中，循环新列表，删除老列表。
'''