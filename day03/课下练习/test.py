li = [11, 22, 33, 44, 55, 66, 77, 88, 99]
dic = {}

for item in li:
	if item > 66:
		if dic.get("k1"):
			dic["k1"].append(item)
		else:
			dic["k1"] = []
			dic["k1"].append(item)
			# dic["k1"] = item
	else:
		if dic.get("k2"):
			dic["k2"].append(item)
		else:
			dic["k2"] = []
			dic["k2"].append(item)
			# dic["k2"] = item

print(dic)