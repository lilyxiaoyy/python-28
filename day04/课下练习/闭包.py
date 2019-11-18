def outer():
    a = 10
    def inner():
        print(a)
        print("内部函数")
    return inner

ret = outer()
ret()