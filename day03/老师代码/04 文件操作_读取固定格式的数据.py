f = open("水果", mode="r", encoding="utf-8")
lst = [] # 最终承接数据的地方
for line in f:
    line = line.strip() # "1,苹果,9.9,10000"
    line_lst = line.split(",") # [1,苹果,9.9,10000]
    num = line_lst[0]
    name = line_lst[1]
    price = line_lst[2]
    count = line_lst[3]
    dic = {"编号":num, "名称":name, "价格":price, "库存":count}
    lst.append(dic)
print(lst)
