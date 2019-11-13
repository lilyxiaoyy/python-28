'''
and 并且，与
or 或
not 非
逻辑运算的运算顺序：（）> not > and > or
'''
print(3 > 4 or 4 < 3 and 1 == 1)  # f or f and t => f or f => f
print(1 < 2 and 3 < 4 or 1 > 2)  # t and t or f => t or f => t
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1)  # t and t or f and f => t or f =》 t
print(1 > 2 and 3 < 4 or 4 > 5 and 2 > 1 or 9 < 8)  # f and t or f and t or f => f or f or f => f
print(1 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  # f and f or f and t and t or f => f or f and t or f => f
print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)  # f and t or f and t and t or f => f or f or f => f
'''
打印结果：
False
True
True
False
False
False
总结：使用负责的逻辑运算的时候切记加括号。
'''

print(bool(0))  # False
print(bool(1))  # True
print(bool(-1))  # True

print(bool(""))  # False
print(bool(" "))  # True
print(bool("哈哈"))  # True

print(bool([]))  # False
print(bool([1, 2, 3]))  # True
print(bool({}))  # False
'''
结论：所有表示空的东西都是False。
'''