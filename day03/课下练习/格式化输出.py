'''
一、格式化输出
'''
name = input("Name:")
age = input("Age:")
info = '''
---------- info of %s ----------
Name：%s
Age： %s
---------- end --------
''' % (name, name, age)
print(info)

'''
%s 字符串占位符
%d 数字占位符
如果把上面的age后面的换车%d，就代表你必须只能输入数字啦。这时对应的数据必须是int类型，否则程序会报错。
'''

name = input("Name:")
age = input("Age:")
print(f"{name}的年龄：{age}")
'''
这是第二种格式化输出，推荐使用这种方式，在python3.5以上版本可以使用。
'''

name = input("Name:")
age = input("Age:")
print("{}的年龄：{}".format(name, age))
'''
这是第三种格式化输出
'''

'''固定长度的格式化输出'''
lst = [["1", "lily",  "18", "2008-01-01"], ["2", "lucy",  "18", "2009-01-01"]]

def format_str(lst):
	'''
	格式化输出
	:param lst:
	:return:
	'''
	str1 = ""
	for item in lst:
		str1 += format(item, "<10")
	return str1

for item in lst:
	'''方式一'''
	print("%-10s%-10s%-10s%-10s" % (item[0], item[1], item[2], item[3]))
	'''方式二'''
	print(format_str(item))
	'''方式三'''
	print("%s%s%s%s" % (format(item[0], "<10"), format(item[1], "<10"), format(item[2], "<10"), format(item[3], "<10")))

'''
打印结果：
1         lily      18        2008-01-01
1         lily      18        2008-01-01
1         lily      18        2008-01-01
2         lucy      18        2009-01-01
2         lucy      18        2009-01-01
2         lucy      18        2009-01-01
'''