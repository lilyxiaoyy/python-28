'''
一、文件操作（读写追加，其他方法）
f = open(文件，mode="模式", encoding="编码")
模式：
	r：只读
	w：只写
	a：追加写
	+：扩展
	b：字节（非文本文件）

读取文件最好的方案
with open() as f:
	for line in f:
		line = line.strip()

修改文件：
1、创建一个文件副本。
2、把源文件中的内容读取到内存。
3、然后再内存中进行修改。
4、修改之后保存在文件副本中。
5、把源文件删除。
6、把文件副本更改名称为源文件的名称。

1.1.初识文件操作
	使用python来读写文件是非常简单的操作。我们使用open()函数来打开一个文件，获取到文件句柄。
然后通过文件句柄就可以进行各种各样的操作了。根据打开方式的不同能够执行的操作也会有相应的差异。
打开文件的方式：r, w, a, r+, w+, a+, rb, wb, ab, r+b, w+b, a+b默认使用的是r（只读）模式

1.2.只读操作（r, rb）
需要注意encoding表示编码，根据文件的实际保存编码进行获取数据，对于我们而言，更多的是utf-8.
'''
f = open("a1.txt", mode="r", encoding="utf-8")
content = f.read()
print(content)
'''打印如下：
苹果
香蕉
桔子
桃子
'''
f.close()

'''
rb读取出来的数据是bytes类型，在rb模式下，不能选择encoding字符集。
rb的作用：在读取非文本文件的时候，比如读取MP3、图像、视频、直播等信息的时候就需要用到rb。因为这种数据是没办法直接显示出来的。
在后面我们文件上传下载的时候还会用到。
'''
f = open("a1.txt", "rb")
content = f.read()
print(content)
'''打印如下：
b'\xe8\x8b\xb9\xe6\x9e\x9c\r\n\xe9\xa6\x99\xe8\x95\x89\r\n\xe6\xa1\x94\xe5\xad\x90\r\n\xe6\xa1\x83\xe5\xad\x90'
'''
f.close()

'''
读取文件的方法：
1.read()将文件中的内容全部读取出来，弊端：占内存，如果文件过大。容易导致内存崩溃。
'''
f = open("a1.txt", mode="r", encoding="utf-8")
content = f.read()
print(content)
'''打印结果：
苹果
香蕉
桔子
桃子'''
f.close()


'''
2.read(n)读取n个字符。需要注意的是，如果每次读取，那么会在当前位置继续去读取而不是从头读。
如果使用的是rb模式，则读取出来的是n个字节。
'''
f = open("a1.txt", mode="r", encoding="utf-8")
content = f.read(4)
print(content)
'''
打印结果：
苹果
香
'''
f.close()


f = open("a1.txt", mode="rb")
content = f.read(4)
print(content)
'''
打印结果：b'\xe8\x8b\xb9\xe6'
'''
f.close()


f = open("a1.txt", mode="r", encoding="utf-8")
content = f.read(4)
content2 = f.read(4)
print(content)
'''
打印结果：
苹果
香
'''
print(content2)
'''
打印结果：
蕉
桔子
'''
f.close()


'''
3.readline()一次读取一行数据，注意：readline()结尾，注意每次读取出来的数据都会有一个\n，需要我们使用strip()方法来去掉\n或者空格。
'''
f = open("a1.txt", mode="r", encoding="utf-8")
content = f.readline()
content2 = f.readline()
content3 = f.readline()
print(content)
print(content2)
print(content3)
'''
打印结果：
苹果

香蕉

桔子
'''
f.close()


'''
4.readlines()将每一行形成一个元素，放到一个列表中。将所有的内容都读取出来，容易出现内存崩溃的问题，不推荐使用。
'''
f = open("a1.txt", mode="r", encoding="utf-8")
lst = f.readlines()
print(lst)
'''
打印输出结果：
['苹果\n', '香蕉\n', '桔子\n', '桃子']
'''
for line in lst:
	print(line.strip())
f.close()
'''
打印输出结果：
苹果
香蕉
桔子
桃子
'''


'''
5.循环读取，这种方式是最好的，每次读取一行内容，不会产生内存溢出的问题。
'''
f = open("a1.txt", mode="r", encoding="utf-8")
for line in f:
	print(line.strip())
f.close()
'''
打印结果：
苹果
香蕉
桔子
桃子
'''

'''
1.3.写模式（w, wb）
写的时候注意，如果没有文件，则会创建文件，如果文件存在，则将原件中原来的内容删除，再写入新内容
'''
f = open("b1.txt", mode="w", encoding="utf-8")
f.write("橙汁")
f.flush()  # 刷新，养成好习惯
f.close()


'''
尝试读一读
'''
f = open("b1.txt", mode="w", encoding="utf-8")
f.write("橙汁")
# f.read()  # 报错:io.UnsupportedOperation: not readable
f.flush()
f.close()

'''
wb模式下，不指定打开文件的编码，但是在写文件的时候必须将字符串转换成utf-8的bytes数据。
'''
f = open("c1.txt", mode="wb")
print("橙汁".encode("utf-8"))
'''
打印结果：
b'\xe6\xa9\x99\xe6\xb1\x81'
'''
f.write("橙汁".encode("utf-8"))
f.flush()
f.close()


'''
1.4.追加（a, ab）
只要是a、ab、a+都是在文件的末尾写入，不论光标在任何位置。
在追加模式下，我们写入的内容会追加在文件的结尾。
'''
f = open("a1.txt", mode="a", encoding="utf-8")
f.write("南果梨")
f.flush()
f.close()

f = open("a1.txt", mode="ab")
f.write("天山雪莲".encode("utf-8"))
f.flush()
f.close()


'''
1.5读写模式（r+, r+b）
对于读写模式，必须是先读，因为默认光标是在开头的。当读完了之后再进行写入，我以后使用频率最高的模式是r+
正确操作：
'''
f = open("a1.txt", mode="r+", encoding="utf-8")
content = f.read()
f.write("冬桃")
print(content)
f.flush()
f.close()
'''
打印结果：
苹果
香蕉
桔子
桃子南果梨天山雪莲
'''


'''
错误操作：
结果：将开头的内容改成了“石榴”，然后读取的内容是后面的内容。
所以记住：r+模式下，必须是先读取，然后再写入
深坑请注意：在r+模式下，如果读取了内容，不论读取内容多少，光标显示的是多少，再写入或者操作文件的时候都是在结尾进行的操作。
'''
f = open("a1.txt", mode="r+", encoding="utf-8")
f.write("石榴")
content = f.read()
print(content)
f.flush()
f.close()
'''
打印结果：

香蕉
桔子
桃子南果梨天山雪莲冬桃
'''


f = open("a1.txt", mode="r+", encoding="utf-8")
content = f.read(3)
print(content)
f.write("草莓")
f.flush()
f.close()


'''
1.6.其他相关操作
1.seek(n)光标移动到n的位置，注意，移动的单位是byte。所以如果是UTF-8的中文部分要是3的倍数。
通常我们使用seek都是移动到开头或者结尾。
移动到开头：seek(0)
移动到结尾：seek(0, 2) seek的第二个参数表示的是从哪个位置进行偏移，默认是0，表示开头，1表示当前位置，2表示结尾。
'''
f = open("a1.txt", mode="r+", encoding="utf-8")
f.seek(0)  # 光标移动到开头，此行可有可无
content = f.read()  # 读取内容，此时光标移动到结尾
print(f"content: {content}\n")
f.seek(0)  # 再次将光标移动到开头
content2 = f.read()
print(f"content2: {content2}\n")
f.seek(0, 2)  # 将光标移动到结尾
content3 = f.read()  # 读取内容，什么都没有
print(f"content3: {content3}\n")
f.seek(0)  # 移动到开头
f.write("苹果")  # 写入信息，此时光标在6 中文2*3 = 6
f.flush()
f.close()
'''
打印的内容：
content: 苹果
香蕉
桔子
桃子南果梨天山雪莲冬桃草莓

content2: 苹果
香蕉
桔子
桃子南果梨天山雪莲冬桃草莓

content3:
'''


'''
2.tell()使用tell()可以帮我们获取到当前光标在什么位置
'''
f = open("a1.txt", mode="r+", encoding="utf-8")
f.seek(0)  # 光标移动到开头
content = f.read()  # 读取内容，此时光标移动到结尾
print(content)
f.seek(0)  # 再次将光标移动到开头
f.seek(0, 2)  # 将光标移动到结尾
content2 = f.read()  # 读取内容，什么都没有
print(content2)
f.seek(0)  # 移动到开头
f.write("榴莲")  # 写入信息，此时光标在6 中文3*2 = 6
print(f.tell())  # 光标的位置6
f.flush()
f.close()
'''
打印结果：
苹果
香蕉
桔子
桃子南果梨天山雪莲冬桃草莓

6
'''


'''
3.truncate()截断文件
'''
f = open("d1.txt", mode="w", encoding="utf-8")
f.write("苹果")  # 写入两个字符
f.seek(3)  # 光标移动到3，也就是两个字中间
f.truncate()  # 删除光标后面的所有内容
f.close()


f = open("a1.txt", mode="r+", encoding="utf-8")
content = f.read(3)  # 读取3个字符
print(content)
f.seek(4)
print(f.tell())  # 4
f.truncate()  # 后面的所有内容全部都删掉
f.flush()
f.close()


'''
总结：
f.read(n) 如果是r模式打开，表示读取n个字符
f.read(n) 如果是rb模式打开，表示读取n个字节
f.seek(n) 表示n个字节，1中文由3个字节组成 
'''

'''
1.7.修改文件以及另一种打开文件的方式（重点）
文件修改：只能将文件中的内容读取到内存中，将信息修改完毕，然后将源文件删除，将新文件的名字改成老文件的名字。
'''
import os

with open("b1.txt", mode="r", encoding="utf-8") as f1, \
	open("b1.txt_temp", mode="w", encoding="utf-8") as f2:
	content = f1.read()
	new_content = content.replace("橙汁", "砀山梨")
	f2.write(new_content)
os.remove("b1.txt")  # 删除源文件
os.rename("b1.txt_temp", "b1.txt")  # 重命名新文件


'''
弊端：一次将所有内容进行读取，内存溢出，解决方案：一行一行的读取和操作
'''
import os

with open("b1.txt", mode="r", encoding="utf-8") as f1,\
	open("b1.txt_temp", mode="w", encoding="utf-8") as f2:
	for line in f1:
		new_line = line.replace("砀山梨", "橙汁")
		f2.write(new_line)
os.remove("b1.txt")  # 删除源文件
os.rename("b1.txt_temp", "b1.txt")  # 重命名新文件
