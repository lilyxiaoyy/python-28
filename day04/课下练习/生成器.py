# def func():
#     print(123)
#     yield 456
#     print(789)
#     yield 100
#
#
# gen = func()  # 生成器
# first = gen.__next__()
# print(first)
# second = gen.__next__()
# print(second)

def func():
    lst = []
    for i in range(100):
        lst.append(i)
        if i % 10 == 0:
            yield lst
            lst = []

gen = func()
print(gen.__next__())
print(gen.__next__())