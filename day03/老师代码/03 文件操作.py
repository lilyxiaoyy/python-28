
# 打开这个文件
# r: 只读 read
# w: 只写 write
# a: 追加写 append
# 相对路径：相对于当前程序所在的文件夹
#       ../ 上一层文件夹
#       文件夹名字/  进入到某一个文件夹
# 绝对路径：c:/sylar/a.txt
# #
# f = open("../day2/abc/def.txt", mode="r", encoding="utf-8")
# # 读取内容
# print(f.read())
# f = open("珍藏自拍.txt", mode="r", encoding="utf-8")

# print(f.readline().strip()) # 读一行数据
# print(f.readline().strip()) # 读一行数据
# print(f.readlines()) # 耗费内存
# for line in f:
#     print(line.strip())

# # w模式可以帮我们创建文件
# # w模式下。只要打开文件的一瞬间。 会清空源文件
# f = open("小护士.txt",  mode="w", encoding="utf-8")
# # f.write("风行小王子")
# # f.write("货拉拉小眼睛")

# f = open("alex的女朋友们", mode="a", encoding="utf-8")
# f.write("小仓玛利亚\n")
# f.write("仓木麻衣\n")
# f.write("小泉彩\n")

# mode： r+   # 读写操作
#        w+   # 写读
#        a+  追加写读

# f = open("金瓶梅.txt", mode="a+", encoding="utf-8")
# f.write("alex也来过")
# f.seek(0) # 移动到开头
# print(f.read())

# mode：b bytes   不需要给出编码. 读写非文本文件(图片， 音乐， 视频）
# # 文件复制
# f1 = open("D:/alex.jpg", mode="rb")
# f2 = open("E:/alex.jpg", mode="wb")
# for line in f1:
#     f2.write(line)
# f1.close()
# f2.close()
# # 打开文件最OK的方式
# with open("abc.txt", mode="w", encoding="utf-8") as f:
#     f.write("123456")


# 文件修改
# 创建一个文件副本
# 从源文件中读取内容。 加载到内存。 然后在内存进行修改。 写入到文件副本
# 删除源文件
# 把副本文件重命名成原文件（偷天换日)
import time
import os
with open("人名单_副本", mode="w", encoding="utf-8") as f1,\
    open("人名单", mode="r", encoding="utf-8") as f2:
    for line in f2: # 从原文件中读取内容
        line = line.replace("帅", "傻x") # 内存层面的修改
        f1.write(line)  #  写入到新文件

time.sleep(2)
os.remove("人名单")
time.sleep(2)
os.rename("人名单_副本", "人名单")







