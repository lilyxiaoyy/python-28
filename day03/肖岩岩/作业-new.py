'''
文件a1.txt内容

序号     部门      人数     平均年龄    备注
1       python      30      26          单身狗
2       Linux       26      30          没对象
3       运营部      20      24          女生多
......
通过代码，将其构建成这种数据类型：
	[{'序号':'1', '部门':'Python', '人数':'30', '平均年龄'}:'26','备注':'单身狗'},......]

使用的知识点：
	1.文件读取
	2.字符串
	3.字典
	4.列表
'''
# def func(file):
# 	ret_lst = []
# 	with open(file, "r", encoding="utf-8") as f:
# 		key_lst = f.readline().strip().split()
# 		for line in f:
# 			value_lst = line.strip().split()
# 			ret_lst.append(dict(zip(key_lst, value_lst)))  # zip()拉链函数
# 	return ret_lst
#
#
# res_lst = func("a1.txt")
# print(res_lst)


'''
HR人力资源管理：
1. 菜单：("查看员工信息", "添加员工信息", "修改员工信息", "删除员工信息", "退出")
2. 添加员工信息：
	用户输入员工的基本信息（id, name, birthday， salary， input_time）,
	将员工信息写入到文件emp.db文件中
3. 修改员工信息：
	显示所有员工信息，然后让用户选择要修改的员工的id，然后让用户输入员工的工资，
	将员工的工资修改为用户输入的工资，其余内容不做改动
4. 删除员工信息：
	显示所有员工信息，然后用户选择要删除的员工id,根据用户输入的id删除该员工的全部信息
5. 查看员工信息：
	显示出所有员工的基本信息。
	
按照这个顺序做可能会容易一点儿： 1， 2， 5， 4， 3
'''
import os

file = "emp.db"


def printC(str1, color="black"):
	'''添加颜色输出
	color: red:红色 gre:绿色 yel:黄色
	'''
	col_type = 30
	if color == "red":
		col_type = 31
	elif color == "gre":
		col_type = 32
	elif color == "yel":
		col_type = 33
	print("\033[0;%sm%s\033[0m" % (col_type, str1))


def emp_isexist(id):
	'''
	判断员工ID是否已存在
	:param id:
	:return: 存在True， 不存在False
	'''
	with open(file, "r", encoding="utf-8") as f:  # 读员工信息文件
		for line in f:  # 一行一行读取
			if id == line.strip().split()[0]:  # 如果id已存在
				return True
	return False


def add_emp_info():
	'''	添加员工信息'''
	printC("添加员工信息：", "gre")
	while 1:
		id = input("ID: ").strip()
		if not id:  # 如果id为空
			printC("员工ID不能为空!", "red")
			continue
		if emp_isexist(id):  # 如果ID已存在
			printC("员工ID已存在，请重新输入！", "red")
		else:  # ID不存在，继续往下走
			name = input("Name: ").strip()
			if not name:  # 员工名为空
				printC("员工名不能为空！", "red")
				continue
			bir = input("Birthday（Year-month-day）: ").strip()
			if not bir:  # 出生日期为空
				printC("出生日期不能为空！", "red")
				continue
			salary = input("Salary: ").strip()
			if not salary:  # 工资为空
				printC("工资不能为空！", "red")
				continue
			input_time = input("Input_time（Year-month-day）: ").strip()
			if not input_time:  # 入职时间为空
				printC("入职时间不能为空！", "red")
				continue
			with open(file, 'a', encoding="utf-8") as f:  # 录入员工信息
				f.write(f"{id}\t{name}\t{bir}\t{salary}\t{input_time}\n")
			printC("员工%s信息录入成功！" % name, "gre")
			break

def format_str(*args):
	'''格式化字符串输出'''
	str1 = ""
	for item in args:
		str1 += format(item, " <10")
	return str1


def show_emp_info():
	'''查看员工信息'''
	printC("员工信息列表：", "gre")
	flag = 0  # 记录员工信息是否为空，默认为0
	printC(format_str("ID", "Name", "Birthday", "Salary", "Input_time"), "gre")
	with open(file, "r", encoding="utf-8") as f:  # 读取员工信息
		for line in f:  # 一行一行循环读取
			if line.strip():  # 去掉左右两边的空白
				flag += 1  # 代表有员工信息，flag改为1
			printC(format_str(*line.strip().split()), "gre")  # 显示员工信息
	if not flag:  # 员工信息为空
		printC("暂时没有员工信息！", "red")
	else:
		return True


def upd_emp_info():
	'''修改员工信息'''
	ret = show_emp_info()  # 显示员工信息
	if ret:
		while 1:
			upd_id = input("请输入要修改的用户ID: ").strip()
			if emp_isexist(upd_id):  # 判断员工ID是否存在
				upd_salary = input("请输入员工的工资：").strip()
				if not upd_salary:  # 工资不能为空
					printC("工资不能为空！", "red")
					continue
				with open(file, "r", encoding="utf-8") as f, \
						open(f"{file}-temp", "w", encoding="utf-8") as f2:
					for line in f:  # 一行一行循环读取
						emp_lst = line.strip().split()  # 将每个员工信息放入列表
						if emp_lst[0] == upd_id:  # 找到要修改的员工信息
							emp_lst[3] = upd_salary  # 修改工资
							printC("工资修改成功！", "gre")
						f2.write("%s\n" % '\t'.join(emp_lst))  # 将修改后的新信息写入文件副本
				os.remove(file)  # 删除原文件
				os.rename(f"{file}-temp", file)  # 将文件副本改为原文件
				break
			else:
				printC("输入错误，员工ID不存在！", "red")


def del_emp_info():
	'''删除员工信息'''
	ret = show_emp_info()  # 显示员工信息
	if ret:
		while 1:
			del_id = input("请输入要删除的员工ID: ").strip()
			if emp_isexist(del_id):  # 判断员工ID是否存在
				with open(file, "r", encoding="utf-8") as f, \
					open(f"{file}-temp", "w", encoding="utf-8") as f2:
					for line in f:  # 一行一行循环读取员工信息
						if line.strip().split()[0] != del_id:  # 不是删除的员工信息
							f2.write(line)  # 写入文件副本
						else:
							printC(f"员工ID{del_id}信息删除成功", "gre")
				os.remove(file)
				os.rename(f"{file}-temp", file)
				break
			else:
				printC("输入错误，员工ID不存在！", "red")


while 1:
	menu = ("查看员工信息", "添加员工信息", "修改员工信息", "删除员工信息", "退出")
	printC("序号\t功能", "yel")
	for i, item in enumerate(menu):
		printC("%s\t\t%s" % (i+1, item), "yel")
	inp = input("请输入功能序号>>>：").strip()
	if inp == "1":
		show_emp_info()
	elif inp == "2":
		add_emp_info()
	elif inp == "3":
		upd_emp_info()
	elif inp == "4":
		del_emp_info()
	elif inp == "5":
		printC("退出成功！", "gre")
		break
	else:
		printC("输出错误，功能序号不存在！", "red")