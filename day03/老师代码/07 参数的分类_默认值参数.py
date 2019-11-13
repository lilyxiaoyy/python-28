#
# def info(name, age, gender="男"):
#     print(gender)
#
# info("马鹏", 118)
# info("张德", 13)
# info("宋达", 2)
# info("王大美女", 18, "女")
# info("徐峥", 26)
#
#
# # print("李嘉诚", "马化腾", "王健林", sep="_sb_", end="今天天气不错")
# # print(123)
#

# def chi(*food):
#     print(food)

# chi()
# chi("黄瓜")
# chi("黄瓜", "茄子")
# chi("黄瓜", "茄子", "辣椒")
# chi("黄瓜", "茄子", "辣椒", "胡萝卜")
# chi("黄瓜", "茄子", "辣椒", "胡萝卜", "大蒜")

# def chi(**food): # 关键字参数, 收到的内容装字典中
#     print(food)
#
# # chi("馒头") # 位置参数
# chi(zhushi="馒头", tang="珍珠白玉汤", tian="就转大还丹")
# chi(zhushi="馒头", tang="珍珠白玉汤")
# chi(zhushi="馒头")
# chi()


# def func(a, b, c, *args, m="哈哈", **kwargs):
#
#     print(kwargs)
#
#
# func(1,2,3,4,"a", "b", "e", "呵呵", wuda="武大", lang="西门")




lst1 = [1, 2, 3,]
lst2 = [11, 12, 13,]

def func(*args, **kwargs): # 形参, 聚合
    print(kwargs)

func(*lst1, *lst2) # func("alex", "傻不傻", {"a":"b"}, "多傻", "再见")
# func(1, 1) # 实参, 打散
# func("alex", "傻不傻", {"a":"b"}, lst[3]) # 实参

