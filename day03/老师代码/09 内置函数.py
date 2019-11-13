# s = "print('你好啊, 我叫赛利亚')"
# exec(s)
# exec("a = 20")
# print(a)

# s = "[1,2,3,4]"
# ret = eval(s) # 可以把一个字符串代码执行. 通常用来还原列表或者字典
# print(ret)
# print(type(ret))

# code = input(">>")
# exec(code)
# print(123)

# lst ="abc"
# print(hash(lst)) # unhashable type: 'list' TypeError: unhashable type: 'list'
# # 字典的key: 必须可哈希
# # {[]:123}


# print(help(str))
# a = 10
# def func():
#     pass
# print(callable(func))
# print(dir(str)) # 查看str能执行哪些操作
# print(dir(list))

# print(hex(1238)) # 0x4d6
# print(oct(1238)) # 0o2326   8 0-7  2  0-1  10  0-9  16 0-F
# print(bin(18)) # 0b10010
# a = 0b10010
# print(a)

# print(abs(4))
# print(abs(-4))
#
# print(divmod(10, 3))
# print(round(6.2))
#
# print(pow(2, 10))
# # 1 2 4 8 16 32 64 128 256 512 1024
# print(sum([1,2,3,4,5,6,7,8,9,10]))
# print(max([1,2,3,4,5,6,7,8,9,10]))
# print(min([1,2,3,4,5,6,7,8,9,10]))
#
# print(list(reversed([1,2,3,4,5,6,7,8,9,10])))

# s = slice(0, 2) # 切片
# ss = "alex"
# print(ss[s])
# sss = "wusir"
# print(sss[s])
# start = 0
# end = 2
# print(ss[start:2])
# print(sss[0:2])

# print(ord("中")) # 97
# print(chr(20013))
# for i in range(1, 65536):
#     print(chr(i),"", end="")
# import random
# print(chr(random.randint(ord("a"), ord("z"))))
# print(ascii("中"))

# format()
# print(format(3141592653, ".2f"))
# print(format(8, "08b")) # 二进制

# # 192.168.1.1
# print(format(192, "08b"), format(168, "08b"), format(1, "08b"), format(1, "08b"))
# # print(bin(192))
# print(format(8, "o"))

# lst = ["呵呵", "哈哈", "吼吼"]
# for item in lst:
#     print(item)
# for i in range(len(lst)):
#     print(i)
#     print(lst[i])
# for i, item in enumerate(lst):
#     print(i)
#     print(item)

# 1 or 0 or True or [] or False
# print(any([None, 1, "", [], False])) # or
# print(all([None, 1, "", [], False])) # and

lst1 = ["赵本山","宋丹丹", "范伟", "alex"]
lst2 = ["卖拐", "家有儿女", "道士下山", "吹B"]
lst3 = ["好看", "有钱", "有镜头"]
# 拉链函数
print(list(zip(lst1, lst2, lst3)))

