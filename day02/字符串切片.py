# -*- coding: utf-8 -*-
s = "第一次鸦片战争中国开始进入半殖民地半封建社会"
print(s[-2:-6:-1])
print(s[-2:-6:-2])
print(s[10:1:-2])

'''回文：从左到右和从右到左是一样的
上海自来水来自海上
'''
s = input("请输入：")
if s == s[::-1]:
	print("您输入的是回文。")
else:
	print("您输入的不是回文。")