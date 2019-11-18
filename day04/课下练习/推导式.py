# lst = ["python%s期" % i for i in range(1, 29)]
# print(lst)

lst = [i * i for i in range(100) if i % 3 == 0]
print(lst)

gen = (i * i for i in range(100) if i % 3 == 0)
print(list(gen))