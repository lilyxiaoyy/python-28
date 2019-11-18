'''
简易博客园系统
1）.启动程序，首页面应该显示成如下格式：
	欢迎来到博客园首页
	1：请登录
	2：请注册
	3：文章页面
	4：日记页面
	5：注销
	6：退出程序
2）.用户输入选项，3,4选项必须在用户登录成功之后，才能访问成功。
3）.用户选择登录，用户名密码从register文件中读取验证，三次机会，没成功则结束整个程序。登陆成功之后，可以选择访问3,4项，
访问页面之前，必须要在log文件中打印日志，日志格式为-->用户：xx在xx年xx月xx日 执行了xxx函数，访问页面时，页面内容为：
欢迎xx用户访问评论（文章，日记）页面。
4）.如果用户没有注册，则可以选择注册，注册成功之后，可以自动完成登录，然后进入首页选项。
5）.注销用户是指注销用户的登录状态，使其在访问任何页面时，必须重新登录。
6）.退出程序为结束整个程序运行。
'''
def access_log(fn):
	'''日志装饰器'''
	def inner(*args, **kwargs):
		with open(access_log_file, "a", encoding="utf-8") as f:
			dt = datetime.datetime.now()
			f.write("%s在%s年%s月%s日 执行了%s函数\n" % (usr, dt.year, dt.month, dt.day, fn.__name__))
		ret = fn(*args, **kwargs)
		return ret
	return inner


def islogin(fn):
	'''验证用户是否登录的装饰器'''
	def inner(*args, **kwargs):
		global usr
		if usr:
			ret = fn(*args, **kwargs)
			return ret
		else:
			# 判断用户文件是否存在
			if file_isexist(user_info_file):
				num = 3
				print("请先登录")
				for i in range(num, 0, -1):
					user = input("Username:").strip()
					pwd = input("Password:").strip()
					with open(user_info_file, "r", encoding="utf-8") as f:
						for line in f:
							username, password = line.strip().split()
							if username == user and password == pwd:
								print("恭喜登录成功！")
								usr = user
								ret = fn(*args, **kwargs)
								return ret
						else:
							if i > 1:
								printC("用户名或密码错误，你还有%s次机会！" % (i-1), "red")
				else:
					exit("登录错误次数超限，程序退出！")
			else:
				printC("请先登录！", "red")
				return
	return inner


def register():
	'''用户注册'''
	print("用户注册")
	global usr
	while not usr:
		username = input("Username:").strip()
		if not username:
			printC("请输入用户名!", "red")
			continue
		user_isexist = False
		# 判断用户文件是否存在
		if file_isexist(user_info_file):
			with open(user_info_file, "r", encoding="utf-8") as f:
				for line in f:
					if username == line.strip().split()[0]:
						printC("用户已存在！", "red")
						user_isexist = True
						break
			if user_isexist:
				continue
		password = input("Password:").strip()
		if not password:
			printC("请输入密码!", "red")
			continue

		with open(user_info_file, "a", encoding="utf-8") as f:
			f.write("%s\t%s\n" % (username, password))
		usr = username
		print("用户%s注册成功！" % usr)
		f = open("%s_article.txt" % usr, "w")
		f.close()
		f2 = open("%s_diary.txt" % usr, "w")
		f2.close()
	else:
		printC("%s用户已登录！" % usr, "gre")


def login():
	'''登录'''
	print("用户登录")
	global usr
	# 判断用户文件是否存在
	if file_isexist(user_info_file):
		if not usr:
			num = 3
			for i in range(num, 0, -1):
				user = input("Username:").strip()
				pwd = input("Password:").strip()
				with open(user_info_file, "r", encoding="utf-8") as f:
					for line in f:
						username, password = line.strip().split()
						if username == user and password == pwd:
							printC("恭喜登录成功！", "gre")
							usr = user
							return
					else:
						if i > 1:
							printC("用户名或密码错误，你还有%s次机会！" % (i - 1), "red")
			else:
				exit("登录错误次数超限，程序退出！")
		else:
			printC("%s用户已登录" % usr, "gre")
	else:
		printC("请先注册!", "red")


@islogin
@access_log
def article_page():
	'''文章页面'''
	printC("欢迎%s用户访问文章页面" % usr, "yel")
	article_menu = ["查看文章", "添加文章", "删除文章", "返回上一单元"]
	art_func = ["show_func", "add_article", "delete_func", "return_pre"]
	while 1:
		for i, art in enumerate(article_menu, 1):
			printC("%-5s%-10s" % (i, art), "yel")
		inp = input("请输入您要执行的功能序号：").strip()
		if inp.isdigit():
			inp = int(inp)
			if inp in range(len(art_func)+1):
				if inp == 4:
					break
				eval(art_func[inp-1]+"('article', '文章', '主题')")
			else:
				printC("输入错误，序号不存在!", "red")
		else:
			printC("输入错误，序号不存在！", "red")


def add_article(type, des, con):
	print(f"添加{des}")
	while 1:
		title = input("Title:").strip()
		if not title:
			printC("请输入标题！", "red")
			continue
		title_isexist = False
		# 判断文章文件是否存在
		if file_isexist(f"{usr}_{type}.txt"):
			with open(f"{usr}_{type}.txt", "r", encoding="utf-8") as f:
				for line in f:
					if title == line.strip().split("===:::")[0]:
						printC(f"{con}已存在！", "red")
						title_isexist = True
						break
			if title_isexist:
				continue
		content = input("Content:").strip()
		if not content:
			printC("请输入内容！", "red")
			continue
		with open(f"{usr}_{type}.txt", "a", encoding="utf-8") as f:
			f.write(f"{title}===:::{content}\n")
		printC("文章添加成功!", "gre")
		break


@islogin
@access_log
def diary_page():
	'''日记页面'''
	print("日记页面")
	printC("欢迎%s用户访问日记页面" % usr, "yel")
	diary_menu = ["查看日记", "添加日记", "删除日记", "返回上一单元"]
	dia_func = ["show_func", "add_diary", "delete_func", "return_pre"]
	while 1:
		for i, art in enumerate(diary_menu, 1):
			printC("%-5s%-10s" % (i, art), "yel")
		inp = input("请输入您要执行的功能序号：").strip()
		if inp.isdigit():
			inp = int(inp)
			if inp in range(len(dia_func) + 1):
				if inp == 4:
					break
				eval(dia_func[inp - 1]+"('diary', '日记', '日期')")
			else:
				printC("输入错误，序号不存在!", "red")
		else:
			printC("输入错误，序号不存在！", "red")


def add_diary(type, des, con):
	print(f"添加{des}")
	while 1:
		diary = input(f"{type}:").strip()
		if not diary:
			printC(f"请输入{des}内容！", "red")
			continue
		dt = datetime.datetime.now()
		now_date = "%s-%s-%s" % (dt.year, dt.month, dt.day)
		with open(f"{usr}_{type}.txt", "a", encoding="utf-8") as f:
			f.write(f"{now_date}===:::{diary}\n")
		printC(f"{des}添加成功!", "gre")
		break


def show_func(type, des, con1):
	'''查看文章或日记'''
	print(f"查看{des}")
	if file_isexist(f"{usr}_{type}.txt"):
		num = 0
		with open(f"{usr}_{type}.txt", "r", encoding="utf-8") as f:
			for line in f:
				col1, col2 = line.strip().split("===:::")
				if num == 0:
					printC("%-5s%-13s%s" % ("序号", con1, "内容"), "yel")
				num += 1
				printC("%-7s%-15s%s" % (num, col1, col2), "yel")
		if not num:
			printC(f"暂无{des}!", "red")
		return num
	else:
		printC(f"暂无{des}!", "red")


def delete_func(type, des, con):
	'''删除文章或日记'''
	print(f"删除{des}")
	ret_num = show_func(type, des, con)
	if ret_num:
		while 1:
			del_num = input(f"请输入删除的{des}序号：").strip()
			if del_num.isdigit():
				del_num = int(del_num)
				if del_num in range(1, ret_num + 1):
					num = 0
					with open(f"{usr}_{type}.txt", "r", encoding="utf-8") as f, \
							open(f"{usr}_{type}.txt-temp", "w", encoding="utf-8") as f2:
						for line in f:
							num += 1
							if num != del_num:
								f2.write(line)
					printC(f"{des}删除成功！", "gre")
					os.remove(f"{usr}_{type}.txt")
					os.rename(f"{usr}_{type}.txt-temp", f"{usr}_{type}.txt")
					return
				else:
					printC(f"输入错误，请重新输入正确的{des}序号！", "red")
			else:
				printC(f"输入错误，请重新输入正确的{des}序号！", "red")


def logout():
	'''注销'''
	global usr
	if usr:
		usr = ""
		printC("注销成功！", "gre")
	else:
		printC("您还没有登录哦！", "red")


def sign_out():
	'''退出'''
	exit("退出成功！")


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


def file_isexist(file):
	'''判断文件是否存在'''
	if os.path.exists(file) and os.path.isfile(file):
		return True


if __name__ == '__main__':
	'''主程序'''
	import os
	import datetime

	menu_lst = ["请登录", "请注册", "文章页面", "日记页面", "注销", "退出程序"]
	func_lst = ["login", "register", "article_page", "diary_page", "logout", "sign_out"]
	usr = ""
	user_info_file = "register"
	access_log_file = "access.log"

	while 1:
		printC("欢迎来到博客园首页".center(20, "*"), "yel")
		for i, menu in enumerate(menu_lst, 1):
			printC("%-5s%-10s" % (i, menu), "yel")
		inp = input("请输入功能序号：").strip()
		if inp.isdigit():
			inp = int(inp)
			if inp in range(1, len(menu_lst)+1):
				eval(func_lst[inp-1]+'()')
			else:
				printC("输入错误，请输入正确的功能序号。", "red")
		else:
			printC("输入错误，请输入正确的功能序号。", "red")

'''
坑：由于所有的操作都要带着用户名的，比如，查看alex的文章，打开的文件就是alex_文章.txt。
所以，我们需要在登录的时候把用户名记录在全局变量中，方便其他函数访问。

做题顺序：先把框架搭起来，让用户选择不同的菜单。
根据不同的菜单，执行不同的函数。
先做：
	注册
	登录
	日志（装饰器）
	登录状态检查（装饰器）
	注销
	退出程序
后做：
	文章
	日记
其中进入文章和日记之后：
进入文章页面：
	1.查看文章
	2.添加文章
	3.删除文字
	4.返回上一单元

进入日记页面：
	1.查看日记
	2.添加日记
	3.删除日记3
	4.返回单一单元

思路：在注册用户的时候，给该用户创建两个文件，一个是存储文章的，一个是存储日记的。
alex_文章.txt：
	{"title": "昨夜大保健被抓实录", "content": "人在江湖漂，哪能不去piao"}
	{"title": "前天大保健被抓实录", "content": "这家不好，以后不来了"}
	{"title": 标题, "content": 文章内容}
alex_日记.txt
	2019-01-02$$今天很无聊，在家看电影
	2019-01-02$$今天很无聊，在家看电影
	时间$$内容
'''