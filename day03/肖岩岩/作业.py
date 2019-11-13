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

def add_emp_info():
	'''	添加员工信息'''
	id = input("ID: ")
	name = input("Name: ")
	bir = input("Birthday（Year-month-day）: ")
	salary = input("Salary: ")
	input_time = input("Input_time（Year-month-day）: ")
	with open(file, 'a', encoding="utf-8") as f:
		f.write(f"{id}\t{name}\t{bir}\t{salary}\t{input_time}\n")
	print("添加员工%s成功！" % name)


def show_emp_info():
	'''查看员工信息'''
	empty = 0
	with open(file, "r", encoding="utf-8") as f:
		for line in f:
			if line.strip():
				empty = 1
			print(line.strip())
	if not empty:
		print("暂时没有员工信息！")
	else:
		return True


def upd_emp_info():
	'''修改员工信息'''
	ret = show_emp_info()
	if ret:
		upd_id = input("请输入要修改的用户ID: ")
		upd_salary = input("请输入员工的工资：")
		with open(file, "r", encoding="utf-8") as f, \
				open(f"{file}-temp", "w", encoding="utf-8") as f2:
			for line in f:
				emp_lst = line.strip().split()
				if emp_lst[0] == upd_id:
					emp_lst[3] = upd_salary
					print("修改成功！")
				f2.write("%s\n" % '\t'.join(emp_lst))
		os.remove(file)
		os.rename(f"{file}-temp", file)


def del_emp_info():
	'''删除员工信息'''
	ret = show_emp_info()
	if ret:
		del_id = input("请输入要删除的用户ID: ")
		with open(file, "r", encoding="utf-8") as f, \
			open(f"{file}-temp", "w", encoding="utf-8") as f2:
			for line in f:
				if line.strip().split()[0] != del_id:
					f2.write(line)
				else:
					print(f"用户id{del_id}删除成功")
		os.remove(file)
		os.rename(f"{file}-temp", file)


while 1:
	menu = ("查看员工信息", "添加员工信息", "修改员工信息", "删除员工信息", "退出")
	print("序号\t功能")
	for i, item in enumerate(menu):
		print("%s\t\t%s" % (i+1, item))
	inp = input("请输入序号>>>：")
	if inp == "1":
		print("查看员工信息")
		show_emp_info()
	elif inp == "2":
		print("添加员工信息")
		add_emp_info()
	elif inp == "3":
		print("修改员工信息")
		upd_emp_info()
	elif inp == "4":
		print("删除员工信息")
		del_emp_info()
	elif inp == "5":
		print("退出成功！")
		break
	else:
		print("输出错误，序号不存在！")




