'''列表推导式'''
lst = []
for i in range(1, 10):
    lst.append(i)
print(lst)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''替换成列表推导式'''
print([i for i in range(1, 10)])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
列表推到式是通过一行来构建你要的列表，列表推导式看起来代码简单。但是出现错误之后很难排查。
列表推导式的常用写法：
    [结果 for 变量 in 可迭代对象]
'''

print(["python%s" % i for i in range(1, 10)])
'''
打印结果：
['python1', 'python2', 'python3', 'python4', 'python5', 'python6', 'python7', 'python8', 'python9']
'''

'''
我们还可以对列表中的数据进行筛选。
筛选模式：   
    [结果 for 变量 in 可迭代对象 if 条件]    
'''
print([i for i in range(1, 10) if i % 2 == 0])
'''
打印结果：
[2, 4, 6, 8]
'''

'''生成器表达式和列表推导式的语法基本上是一样的，只是把[]替换成()'''
gen = (i for i in range(10))
print(gen)
'''
打印结果：
<generator object <genexpr> at 0x000000000221FFC0>
'''

'''打印的结果就是一个生成器，我们可以使用for循环来循环这个生成器'''
gen = ("苹果%s" % i for i in range(1, 10))
for i in gen:
    print(i)
'''
打印结果：
苹果1
苹果2
苹果3
苹果4
苹果5
苹果6
苹果7
苹果8
苹果9
'''

'''生成器表达式也可以进行筛选'''
gen = (i for i in range(1, 10) if i % 2 == 0)
for num in gen:
    print(num)
'''
打印结果：
2
4
6
8
'''

'''获取1-100内能被3整除的数'''
gen = (i for i in range(1, 100) if i % 3 == 0)
for num in gen:
    print(num)

'''100以内能被3整除的数的平方'''
gen = (i * i for i in range(1, 100) if i % 3 == 0)
for num in gen:
    print(num)

'''寻找名字中带有两个e的人的名字'''
names = [["Tom", "Billy", "Jefferson", "Andrew", "Steven", "Joe"],
         ["Alice", "Jill", "Ana", "Wendy", "Jennifer", "Sherry", "Eva"]]

lst = []
for item in names:
    for name in item:
        if name.count("e") > 1:
            lst.append(name)
print(lst)

'''生成器表达式'''
names = [["Tom", "Billy", "Jefferson", "Andrew", "Steven", "Joe"],
         ["Alice", "Jill", "Ana", "Wendy", "Jennifer", "Sherry", "Eva"]]

gen = (name for item in names for name in item if name.count("e") >= 2)
print(list(gen))

'''-----------------------'''
def func():
    print(111)
    yield 222