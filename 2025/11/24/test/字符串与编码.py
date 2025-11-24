#Python3中，字符串以Unicode编码存储和处理，因此支持多语言。
print("包含中文的string")

#python使用ord()函数获取字符的Unicode码点，使用chr()函数把码点转换为对应的字符
print("字符 '中' 的Unicode码点是：", ord('中'))
print("Unicode码点 20013 对应的字符是：", chr(20013))

#如果知道字符的十六进制码点，可以使用十六进制表示法
print("中文", "\u4e2d\u6587", chr(0x4e2d) + chr(0x6587))

#Python中的字符串类型是str，在内存中以Unicode编码存储，一个字符对应若干个字节
#如果要在网络上传输或保存到磁盘上，就需要把字符串编码为字节序列
#Python对于bytes类型的数据用b前缀表示
x = b'ABC'  # bytes类型的数据
print("bytes:", x)
print("bytes的第一个字节:", x[0])  # 输出65
print("bytes的第二个字节:", x[1])  # 输出66
print("bytes的第三个字节:", x[2])  # 输出67

#Python使用encode()方法把str转换为bytes，使用decode()方法把bytes转换为str
s = 'Hello, 字符串'
b = s.encode('utf-8')  # 使用UTF-8编码
print("字符串转换为bytes:", b)
s2 = b.decode('utf-8')  # 使用UTF-8解码
print("bytes转换回字符串:", s2)
#如果编码和解码使用的字符集不一致，会导致报错
#如果bytes中包含无法解码的字节，decode()方法会报错，可以传入errors='ignore'忽略错误的字节
b_invalid = b'Hello, \xe4\xb8\xad\xff'
s_invalid = b_invalid.decode('utf-8', errors='ignore')
print("忽略错误字节后的字符串:", s_invalid)


#Python中，使用len()方法可以获取字符串的长度
#当字符串类型为str时，len()返回字符串的字符数
#当字符串类型为bytes时，len()返回字节数
txt1 = 'This is a 字符串'
txt2 = txt1.encode('utf-8')
print("str:", txt1)
print("bytes:", txt2)
print("字符串的字符数:", len(txt1))  # 输出13
print("字符串的字节数:", len(txt2))  # 输出19

#当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python中，采用的格式化方式和C语言是一致的，用%实现
print("Hello, %s" % 'world')  # %s表示字符串
print("整数: %d, 浮点数: %.2f" % (42, 3.14159))  # %d表示整数，%.2f表示浮点数，保留两位小数
print("百分比: %.2f%%" % 99.5)  # %%表示百分号

#Python3中，字符串格式化还可以使用str.format()方法
print("Hello, {}".format('world'))
print("整数: {}, 浮点数: {:.2f}".format(42, 3.14159))
print("百分比: {:.2f}%".format(99.5))

#Python3.6及以上版本，还可以使用f-string进行格式化
name = 'world'
print(f"Hello, {name}")
num = 42
pi = 3.14159
print(f"整数: {num}, 浮点数: {pi:.2f}")
print(f"百分比: {99.5:.2f}%")

#练习
#小明的成绩从去年的72分提升到了今年的85分，
#请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，
#只保留小数点后1位：
last_year = 72
this_year = 85
improvement = this_year - last_year
improvement_percentage = (improvement / last_year) * 100
print("成绩提升百分比，%.1f%%" % improvement_percentage)
print("成绩提升百分比，{:.1f}%".format(improvement_percentage))
print(f"成绩提升百分比，{improvement_percentage:.1f}%")