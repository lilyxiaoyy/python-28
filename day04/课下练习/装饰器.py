# def wrapper(fn):
#     def inner():
#         print("开始记录日志")
#         fn()  # 执行目标函数
#         print("日志记录完毕")
#     return inner
#
#
# def add():
#     print("我是新增")
#
#
# add()
# add = wrapper(add)
# add()

# def wrapper(fn):
#     def inner():
#         print("目标函数执行前")
#         fn()
#         print("目标函数执行后")
#     return inner
#
# def add():
#     print("目标函数")
#
# add = wrapper(add)
# add()

# def wrapper(fn):
#     def inner():
#         print("目标函数执行前")
#         fn()
#         print("目标函数执行后")
#     return inner
#
# @wrapper  # add = wrapper(add)
# def add():
#     print("目标函数")
#
# add()
# username = "lily"
# password = "123"
# login_flag = False
#
#
# def login(fn):
#     def inner():
#         global login_flag
#         if login_flag:
#             fn()
#         else:
#             num = 3
#             for i in range(num, 0, -1):
#                 user = input("User:").strip()
#                 pwd = input("Pwd:").strip()
#                 if user == username and password == pwd:
#                     login_flag = True
#                     print("登录成功")
#                     fn()
#                     break
#                 else:
#                     if i > 1:
#                         print("登录失败，请重新登录，你还有%s次机会" % (i-1))
#             else:
#                 print("错误次数超过%s次，自动退出！" % num)
#     return inner
#
#
# @login
# def add():
#     print("新增")
#
# @login
# def upd():
#     print("修改")
#
# add()
# upd()

# def wrapper(fn):
#     def inner(*args, **kwargs):
#         print("执行目标函数前")
#         ret = fn(*args, **kwargs)
#         print("执行目标函数后")
#         return ret
#     return inner
#
# @wrapper
# def add():
#     print("新增")
#     return 123
#
#
# add()


def wrapper(fn):
    def inner(*args, **kwargs):
        for i in range(5):
            ret = fn(*args, **kwargs)
        return ret
    return inner


@wrapper
def add():
    print("add...")

add()