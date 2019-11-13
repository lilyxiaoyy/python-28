# def yue():
#     print("拿出手机")
#     print("打开微信")
#     print("找到附近的人")
#     print("找一个比较不错的它")
#     print("出来约一约")


# # 编写函数. 获取到用户输入的电话号码. 打印该电话号码的后四位
# def func():
#     phone = input(">>>")
#     print(phone[-4:])
# func()


# def yue():
#     print("拿出手机")
#     print("打开微信")
#
#     return 1
#     print("找到附近的人")
#     return 2
#     print("找一个比较不错的它")
#     print("出来约一约")
#     # return None

# ret = yue()
# print("接受到的返回值是:", ret)


# 接受到用户输入的两个值, a,b
# 返回a和b中比较大那个数

# def func():
#     a = int(input(">>>"))
#     b = int(input(">>>"))
#     c = 0
#     if a > b:
#         c = a
#     else:
#         c = b
#     print(c)
#     return c
#
# while 1:
#     func()

def yue(tools, age): # 形参
    print("拿出手机")
    print("打开%s" % tools)
    print("找到附近的人")
    print("找一个比较不错的它, 年靓最好是%s岁" % age)
    print("出来约一约")

yue("探探", 18)

# 写函数, 接收两个参数 a, b  返回a+b的结果
def cul(a, b):
    return a + b

c = cul(10, 20)
print(c)
