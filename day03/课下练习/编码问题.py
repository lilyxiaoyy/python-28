'''
编码的问题
python2解释器在加载.py文件中的代码时，会对内容进行编码（默认ascii），而python3对内容进行编码的默认为utf-8。
计算机：
	早期，计算机是美国发明的，普及率不高，一般只是在美国使用，所以，最早的编码结构就是按照美国人的习惯来编码的。
对应数字+字母+特殊字符一共也没多少，所以就形成了最早的编码ASCII码，直到今天ASCII依然深深的影响着我们。
ASCII(American Standard Code for Information Interchange，美国标准信息交换代码)是基于拉丁字母的一套电脑编码系统。
主要用于显示现代英语和其他西欧语言，其最多只能用8位来表示（一个字节），即：2**8 = 256，所以， ASCII码最多只能表示
256个字符。

	随着计算机的发展，一级普及率的提高，流行到欧洲和亚洲。这时ASCII码就不合适了，比如：中文汉字有几万个，而ASCII最多
也就256个位置，所以ASCII不行了，怎么办呢？这时，不同的国家就提出了不同的编码用来适用于各自的语言环境，比如，中国的GBK,
GB2312,BIG5,ISO-8859-1等等。这时各个国家都可以使用计算机了。
	GBK，国标码占用2个字符，对应ASCII码GBK直接兼容。因为计算机底层是用英文写的，你不支持英文肯定不行，而英文已经使用了
ASCII码，所以GBK要兼容ASCII。
	这里GBK国标码，前面的ASCII码部分，由于使用两个字节，所以对于ASCII码而言，前9位都是0。
	国标码的弊端，只能中国用，日本就垮了，所以国标码不满足我们的使用。这时提出了一个万国码Unicode。Unicode一开始设计是
每个字符两个字节，设计完了，发现中国汉字依然无法金乡编码，只能进行扩充，扩充成32位也就是4个字节，这回够了。但是，
问题来了，中国字9万多，而unicode可以表示40多亿，根本用不了，太浪费了，于是乎，就提出了新的UTF编码。可边长度编码。
UTF-8：每个字符最少占8位，每个字符占用的字节数不定，根据文字内容进行具体编码，比如，英文，就一个字节就够了，汉字占3个字节。
这时即满足了中文，也满足了节约。也是目前使用频率最高的一种编码。
GBK：每个字符占2个字节，16位。

结论：
	1.ascii:8bit,主要存放的是英文，数字，特殊符号。
	2.gbk:16bit，主要存放中文和亚洲字符，兼容ascii。
	3.unicode:16bit和32bit两个版本。平时我们用的16bit这个版本，全世界所有国家的文字信息，缺点：浪费空间（传输和存储）
	4.utf-8:可变长度unicode，英文：8bit，欧洲文字：16bit，中文24bit。一般数据传输和存储的时候使用。
'''

str1 = "中国"
print(str1.encode("utf-8"))  # b'\xe4\xb8\xad\xe5\x9b\xbd'
print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode("utf-8"))  # 中国

print(str1.encode("gbk"))  # b'\xd6\xd0\xb9\xfa'
print(b'\xd6\xd0\xb9\xfa'.decode("gbk"))  # 中国

'''
总结：一个中文在utf-8编码中占用3个字节，在gbk编码中占用2个字节
'''

with open("a1.txt", mode="w", encoding="utf-8") as f:
	f.write("中国")

with open("a2.txt", mode="wb") as f:
	f.write("中国".encode("utf-8"))

'''
两种不同的写文件的模式，效果是一样的。
'''

print("中国".encode("utf-8"))  # b'\xe4\xb8\xad\xe5\x9b\xbd'
print(bytes("中国", encoding="utf-8"))  # b'\xe4\xb8\xad\xe5\x9b\xbd'
print("中国".encode("utf-8") == bytes("中国", encoding="utf-8"))  # True

'''
总结：字符串转字节，可以使用encode()函数，也可以使用bytes()函数。
'''

bytes1 = "中国".encode("utf-8")
bytes2 = bytes("中国", encoding="utf-8")
print(bytes1)  # b'\xe4\xb8\xad\xe5\x9b\xbd'
print(bytes2)  # b'\xe4\xb8\xad\xe5\x9b\xbd'
print(bytes1.decode("utf-8"))  # 中国
print(str(bytes1, encoding="utf-8"))  # 中国

'''
总结：字节转字符串，可以使用str()函数，也可以使用decode()函数。
'''