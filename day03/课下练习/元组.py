'''
元组：俗称不可变的列表，又被称为只读列表。里面可以放任何数据类型的数据。
'''
tup = ("apple", "banana", "orange")
print(tup)  # ('apple', 'banana', 'orange')

print(tup[0])  # apple
print(tup[:2])  # ('apple', 'banana')
print(tup)  # ('apple', 'banana', 'orange')

for item in tup:
	print(item)
'''
打印结果：
apple
banana
orange
'''

'''
尝试修改元组，报错：TypeError: 'tuple' object does not support item assignment
'''
tup = ("apple", [], "banana", "orange")
# tup[0] = "苹果"  # TypeError: 'tuple' object does not support item assignment
print(tup)  # ('apple', [], 'banana', 'orange')

'''
关于不可变，注意：这里元组的不可变的意思是子元素不可变。而子元素内部的子元素是可以变的，这取决于子元素是否是可变对象。
'''
tup[1].append("苹果")
print(tup)  # ('apple', ['苹果'], 'banana', 'orange')

'''
元组中如果只有一个元素，一定要添加一个逗号，否则就不是元组。
'''
tup = ("aa")
print(tup)  # aa
print(type(tup))  # <class 'str'>

tup = ("aa",)
print(tup)  # ('aa',)
print(type(tup))  # <class 'tuple'>