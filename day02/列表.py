# -*- coding: utf-8 -*-
li = ["苍老师", "东京热", "武藤兰", "波多也结二"]
while 1:
	inp = input(">>>（退出Q）: ").strip()
	if inp.upper() == "Q":
		break
	for item in li:
		if inp.find(item) != -1:
			inp = inp.replace(item, len(item)*"*")
	print(inp)
