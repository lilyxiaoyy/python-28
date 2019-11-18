# fn = lambda a, b: a + b
# ret = fn(3, 5)
# print(ret)

# lst = ["斯琴格日乐", "斯琴高娃", "斯大林", "斯坦达麦尔", "斯皮尔伯格"]
# def func(n):
#     return len(n)
#
#
# print(sorted(lst, key=lambda i: len(i)))
# print(sorted(lst, key=func))

lst = ["斯琴格日乐", "斯琴高娃", "章子怡", "斯坦达麦尔", "斯皮尔伯格"]
print(list(filter(lambda name: name.startswith("斯"), lst)))