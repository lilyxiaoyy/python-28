'''
is 判断左右两端的数据是否是同一个内存地址
== 判断左右两端的数据是否一样
'''
s1 = "alex"
s2 = "alex"
print(s1 == s2)  # True
print(s1 is s2)  # str被放入小数据池，结果为：True

'''
复杂的字符串不会被放入小数据池
'''
s1 = "alex"*10
s2 = "alex"*10
print(id(s1))  # 31918288
print(id(s2))  # 31918192

'''
列表 不会被放入小数据池
'''
lst1 = ["apple", "banana"]
lst2 = ["apple", "banana"]
print(lst1 == lst2)  # True
print(lst1 is lst2) # list不会被放入小数据池，结果：False