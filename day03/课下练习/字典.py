'''
字典（dict）是python中唯一的一个映射类型。
它是以{}括起来的键值对组成，在dict中key是唯一的，在保存的时候，根据key来计算出一个内存地址。然后将key-value保存在这个
地址中。这种算法被称为hash算法。在dict中存储的key-value中的key必须是可hash的，可哈希意味着不可变。

已知的可哈希（不可变）的数据类型：int, str, bool, tuple
不可哈希（可变）的数据类型：list, dict, set

语法：
	{key1:value1, key2:value2...}

注意：key必须是不可变（可哈希）的，value没有要求，可以保存任意类型的数据。
合法字典
'''
dic = {123: 456, True: 999, "id": 1, ("a", "b", "c"): "aaa"}
print(dic[123])  # 456
print(dic[True])  # 999
print(dic["id"])  # 1
print(dic[("a", "b", "c")])  # aaa

'''
不合法
'''
# dic = {[1, 2, 3]: "abc"}  # list是可变的，不能作为key  TypeError: unhashable type: 'list'
# dic = {{1: 2}: "apple"}  # dict是可变的，不能作为key  TypeError: unhashable type: 'dict'
# dic = {{1, 2, 3}: "orange"}  # set是可变的，不能作为key  TypeError: unhashable type: 'set'

'''
dict保存的数据不是按照我们添加进去的顺序保存的，是按照hash表的顺序保存的，而hash表不是连续的，所以不能进行切片。
它只能通过key获取dict中的数据。
'''

'''
1、字典添加元素
'''
dic = {}
dic['name'] = "lily"  # 如果dict中没有出现这个key，就会新增一个key-value的组合进dict
dic['age'] = 18
print(dic)  # {'name': 'lily', 'age': 18}

'''
如果dict中没有出现过这个key-value，可以通过setdefault设置默认值。
如果dict中已经存在了，那么setdefault将不会起作用。
'''
dic.setdefault("salary")  # 也可以往里面设置值
print(dic)  # {'name': 'lily', 'age': 18, 'salary': None}
dic["salary"] = 10000
print(dic)  # {'name': 'lily', 'age': 18, 'salary': 10000}
dic.setdefault("salary", 12000)
print(dic)  # {'name': 'lily', 'age': 18, 'salary': 10000}

'''
2、字典删除元素
pop(key)
del dic[key]
'''
dic = {"a": "apple", "b": "banana", "o": "orange"}
print(dic)  # {'a': 'apple', 'b': 'banana', 'o': 'orange'}
ret = dic.pop("b")
print(ret)  # banana
print(dic)  # {'a': 'apple', 'o': 'orange'}

del dic["o"]
print(dic)  # {'a': 'apple'}

'''
随机删除
'''
dic = {"a": "apple", "b": "banana", "o": "orange"}
ret = dic.popitem()
print(ret)  # ('o', 'orange')
print(dic)  # {'a': 'apple', 'b': 'banana'}

'''
清空字典中的所有内容
'''
dic = {"a": "apple", "b": "banana", "o": "orange"}
dic.clear()
print(dic)  # {}

'''
3、修改字典中的元素
'''
dic = {"a": "apple", "b": "banana", "o": "orange"}
dic2 = {"s": "strawberry", "w": "watermelon", "b": "banana"}
dic.update(dic2)
print(dic)  # {'a': 'apple', 'b': 'banana', 'o': 'orange', 's': 'strawberry', 'w': 'watermelon'}
print(dic2)  # {'s': 'strawberry', 'w': 'watermelon', 'b': 'banana'}
dic2["s"] = "草莓"
print(dic2)  # {'s': '草莓', 'w': 'watermelon', 'b': 'banana'}

'''
4、查询
dic[key] 没有会报错
dic.get(key) 没有不会报错
'''
dic = {"a": "apple", "b": "banana", "o": "orange"}
print(dic["a"])  # apple
print(dic.get("b"))  # banana
print(dic.get("c"))  # None
print(dic.get("w", "watermelon"))  # watermelon

'''
5、keys()
values()
items()
'''
dic = {"a": "apple", "b": "banana", "o": "orange"}
print(dic.keys())  # dict_keys(['a', 'b', 'o'])
for k in dic.keys():
	print(k)
'''
打印结果：
a
b
o
'''

dic = {"a": "apple", "b": "banana", "o": "orange"}
for k in dic:
	print(k)
'''
打印结果：
a
b
o
'''

dic = {"a": "apple", "b": "banana", "o": "orange"}
print(dic.values())  # dict_values(['apple', 'banana', 'orange'])
for v in dic.values():
	print(v)
'''
打印结果：
apple
banana
orange
'''

dic = {"a": "apple", "b": "banana", "o": "orange"}
print(dic.items())  # dict_items([('a', 'apple'), ('b', 'banana'), ('o', 'orange')])
for k, v in dic.items():
	print(k, v)
'''
打印结果：
a apple
b banana
o orange
'''

'''
items()比较常用，keys()和values()相对比较用的少。
'''

'''
解构：解构的时候注意数量必须匹配
'''
a, b = 1, 2
print(a, b)  # 1 2

(c, d) = 3, 4
print(c, d)  # 3 4

# e, f = [1, 2, 3]  # 报错：ValueError: too many values to unpack (expected 2)
# print(e, f)