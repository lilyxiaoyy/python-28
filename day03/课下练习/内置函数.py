'''iter()和next()取下一个值'''
lst = [1, 2, 3]
it = iter(lst)
print(it.__next__())  # 1
print(it.__next__())  # 2
print(next(it))  # 3

'''eval()执行代码. 有返回值'''
print(eval("1+1+9+18"))  # 29
print(eval("[1,2,2,3,4,5]"))  # [1, 2, 2, 3, 4, 5]

'''exec()执行代码，无返回值'''
# exec(input('请输入一段你想执行的代码:')) # a = 30
# print(a)  # 30

'''compile()'''
exec(compile("for i in range(10):print(i)", "", "exec"))
'''
打印结果：
0
1
2
3
4
5
6
7
8
9
'''

'''hash()哈希'''
# print(hash([1, 2, 3]))  # 列表不可哈希
print(hash(123))  # 123
print(hash("中国"))   # -7954274833788291907

'''__import__导入模块，相当于import os'''
s = "os"
__import__(s)

'''help()帮助'''
print(help(str))

'''callable()可调用'''
def func(a):
    if callable(a):
        a()
    else:
        print(a)

def ha():
    print("我是哈哈哈")

func(ha)  # 我是哈哈哈
func("hello")  # hello

'''bin() oct() hex()进制转换'''
print(bin(20))  # 0b10100
print(oct(20))  # 0o24
print(hex(20))  # 0x14

'''divmod()取商和余数'''
print(divmod(10, 3))  # (3, 1)

'''pow()次幂'''
print(pow(2, 10))  # 1024

'''sum()求和'''
print(sum([12, 2, 1, 2]))  # 17

'''reversed()倒序'''
lst = [2, 3, 4, 5, 6]
r = reversed(lst)  # <list_reverseiterator object at 0x00C072F0>
for i in r:
    print(i)

'''
打印结果：
6
5
4
3
2
'''

'''slice()切片'''
s = slice(1, 5, 2)
ss = "hello,I'm good"
print(ss[1:5:2])  # el

'''center()居中'''
s = "周杰伦"
print(s.center(20, "*"))  # ********周杰伦*********

'''format()格式化'''
print(format("周杰伦", "*>20"))  # *****************周杰伦
print(format("周杰伦", "*<20"))  # 周杰伦*****************
print(format("周杰伦", "*^20"))  # ********周杰伦*********
print(format(18, "010b"))  # 0000010010
print(bin(18))  # 0b10010

s = "192.168.1.1"
lst = s.split(".")
for item in lst:
    print(format(int(item), "08b"))
'''
打印结果：
11000000
10101000
00000001
00000001
'''

print(format(1.23956789, ".2f"))  # 1.24

'''ord()Unicode chr()'''
print(ord('中'))  # 20013
print(chr(20013))  # 中
# for i in range(1, 65536):
    # print(chr(i), end=" ")  # 打印各种字

'''repr() \\转义字符'''
print("你好\啊")  # 你好\啊
print(repr("你好\啊"))  # '你好\\啊'
print(r"我的天那\ 怎么不好使了")  # 我的天那\ 怎么不好使了

'''frozenset()冻结'''
s = {1, 2, 3}  # 集合
# print(hash(s))  # TypeError: unhashable type: 'set'
fs = frozenset(s)
print(hash(fs))  # -272375401224217160

'''enumerate()枚举'''
lst = [11, 22, 33, 44]
for i, item in enumerate(lst):
    print(i, ":", item)
'''
打印结果：
0 : 11
1 : 22
2 : 33
3 : 44
'''

'''all()相当于and并且 和 any()相当于or或'''
print(all([18, False, 12]))  # False
print(any([19, 0, 22]))  # True

'''zip() 拉链函数，水桶效应'''
lst1 = ["赵本山", "范伟", "小沈阳"]
lst2 = ("乡村爱情", "卖乖", "不差钱")
lst3 = ["白云", "黑土"]

z = zip(lst1, lst2, lst3)  # 水桶效应
for item in z:
    print(item)
'''
打印结果：
('赵本山', '乡村爱情', '白云')
('范伟', '卖乖', '黑土')
'''

'''sorted()排序函数'''
lst = [22, 1, 3, 5, 6, 7]
print(sorted(lst))  # [1, 3, 5, 6, 7, 22]

'''
sort(iterable, key) 
首先,打开这个可迭代对象. 然后获取到每一项数据. 把每一项数据传递给函数.
根据函数返回的数据进行排序
'''

lst = ["高进", "波多野结衣", "苍老师", "仓木麻衣", "红狗"]
print(sorted(lst, key=lambda s: len(s)))  # ['高进', '红狗', '苍老师', '仓木麻衣', '波多野结衣']


'''sorted(iterable, key, reverse)'''

lst = [
        {"id": 1, "name": 'alex', "age": 18},
        {"id": 2, "name": 'wusir', "age": 16},
        {"id": 3, "name": 'taibai', "age": 17}
]
print(sorted(lst, key=lambda d: d['age'], reverse=True))
'''
打印结果：
[{'id': 1, 'name': 'alex', 'age': 18}, {'id': 3, 'name': 'taibai', 'age': 17}, {'id': 2, 'name': 'wusir', 'age': 16}]
'''


'''
filter(function, iterable) 筛选出来. 大于20的数据
返回迭代器, 把可迭代对象中的每一项数据交给前面的函数. 由函数决定该数据是否保留
'''
lst = [18, 22, 66, 35, 1, 48]
f = filter(lambda n: n > 20, lst)
print(f)  # <filter object at 0x00BB39F0>
for item in f:
    print(item)  # 22 66 35 48



'''filter(function, iterable) 保留成年人  age >= 18'''
lst = [
    {"id": 1, "name": 'alex', "age": 18},
    {"id": 2, "name": 'wusir', "age": 20},
    {"id": 3, "name": 'taibai', "age": 17}
]
f = filter(lambda x: x['age'] >= 18, lst)
print(f)  # <filter object at 0x00C07870>
print(list(f))  # [{'age': 18, 'name': 'alex', 'id': 1}, {'age': 20, 'name': 'wusir', 'id': 2}]

'''map(func, iter1)'''

lst = [2, 5, 3, 2, 4]
m = map(lambda x: x*x, lst)
print(m)  # <map object at 0x00BB39F0>
for item in m:
    print(item)  # 4 25 9 4 16
