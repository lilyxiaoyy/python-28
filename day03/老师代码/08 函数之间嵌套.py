# def func1():
#     print(1)
#     func2()
# def func2():
#     print(2)
#     func3()
# def func3():
#     print(3)
# def func4():
#     print(4)
#     func1()
#
# func4() # 4 1 2 3
# def outer():
#     a = 10
#     print("吼吼")
#     def inner():
#         a = 20
#         print("哈哈")
#     print("嘻嘻")
#     inner()
#     print("呵呵")
# outer()
# outer()



# a = 10  # 全局变量
# def func():
#     b = 20 # 局部变量: 内部的变量. 外界是无法直接访问到
#     print(locals())  # 查看当前作用域中的内容
# func()
#
# print(globals()) # 查看全局作用域中的变量: 变量, 函数名, 模块名, 类名, 对象名

# a = 10
# def func1():
#     global a  # 把全局变量引入到局部(函数内部)
#     a = a + 10
#
# func1()
# print(a)

# a = 10
# def func1():
#     a = 20
#     def func2():
#         nonlocal a
#         a = a + 10
#     func2()
#     print(a) # 30
#
# func1()
# print(a)

a = 1
def fun_1():
    a = 2
    def fun_2():
        a = 3
        def fun_3():
            nonlocal a
            a = 4
            print(a)
        print(a)
        fun_3()
        print(a)
    print(a)
    fun_2()
    print(a)

print(a)
fun_1()
print(a)
