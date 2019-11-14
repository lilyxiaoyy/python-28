'''
set集合是python的一个基本数据类型，一般不是很常用，set中的元素是不重复的，无序的。里面的元素必须是可hash的（int, str,
tuple, bool），我们可以这样来记，set就是dict类型的数据但是不保存value,值保存key，set也用{}表示
'''
set1 = {1, 2, "apple", True, ("aa", "bb")}
print(set1)  # {('aa', 'bb'), 1, 2, 'apple'}

# set2 = {'1', 'apple', 2, True, [1, 2, 3]}  # 报错 TypeError: unhashable type: 'list'
# set3 = {'1', 'apple', 2, True, {1: 2}}  # 报错 TypeError: unhashable type: 'dict'
# set4 = {'1', 'apple', 2, True, (1, 2, [2, 3, 4])}  # 报错 TypeError: unhashable type: 'list'

'''
使用这个特性，我们可以使用set来去掉重复
'''
lst = ["apple", "banana", "orange", "banana", "banana"]
lst = list(set(lst))
print(lst)  # ['apple', 'banana', 'orange']

'''
最主要的操作：去重复，交，并，差
'''
s1 = {"apple", "banana", "orange"}
s2 = {"banana", "orange", "watermelon"}

'''取交集'''
print(s1 & s2)  # {'banana', 'orange'}
print(s1.intersection(s2))  # {'banana', 'orange'}

'''取并集'''
print(s1 | s2)  # {'banana', 'orange', 'watermelon', 'apple'}
print(s1.union(s2))  # {'banana', 'orange', 'watermelon', 'apple'}

'''差集'''
print(s1 - s2)  # {'apple'}
print(s1.difference(s2))  # {'apple'}