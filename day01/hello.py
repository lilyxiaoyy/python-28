# -*- coding: utf-8 -*-
# print('文能提笔安天下，'
# '武能上天定乾坤。'
# '心存谋略何人胜，'
# '古今英雄唯有君。')
#
# print('''文能提笔安天下，
# 武能上天定乾坤。
# 心存谋略何人胜，
# 古今英雄唯有君。
# ''')


# print("lily"*10)

'''
input用户交互
变量 = input(提示语)
input收到的数据都是字符串类型
'''
# salary = input("请输入您的工资：")
# salary = int(salary)
# print("正常拿到手的工资：", salary*0.98)

# money = input("请输入你的工资：")
# money = int(money)
#
# if money > 500:
# 	print("我要冲腾讯QQ会员")
# 	print("买一桶泡面")
#
# print("我要回家了")

# while True:
# 	a = input("请输入第一个数字：")
# 	b = input("请输入第二个数字：")
# 	try:
# 		a = int(a)
# 		b = int(b)
# 		break
# 	except Exception as e:
# 		print("输入有误，请输入数字类型: ", e)
# 		continue
#
# if a > b:
# 	print("Max: ", a)
# else:
# 	print("Max: ", b)


# username = "alex"
# password = "123"
# 
# name = input("Username: ")
# pwd = input("Password: ")
# if name == username and pwd == password:
# 	print("登录成功。")
# else:
# 	print("用户名密码错误！")


'''求1-2+3-4+5 ... 99的所有数的和'''
# i = 1
# Sum = 0
# while i <= 99:
# 	if i % 2:
# 		Sum += i
# 	else:
# 		Sum -= i
# 	i += 1
# print(Sum)

'''从1数数到99'''
# i = 1
# while i <= 99:
# 	print(i)
# 	i += 1


'''判断每个数是奇数还是偶数'''
# while True:
# 	i = input("请输入数字： ")
# 	try:
# 		i = int(i)
# 		if i % 2:
# 			print("奇数")
# 		else:
# 			print("偶数")
# 	except Exception as e:
# 		if i.upper() == "Q":
# 			print("退出。")
# 			break;
# 		print("请输入数字：", e)

'''奇数干什么，偶数干什么'''
