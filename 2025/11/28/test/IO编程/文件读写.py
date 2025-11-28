# 读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。
# 现代操作系统不允许普通程序直接操作硬盘文件，必须通过操作系统提供的API接口来读写文件。
# 所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
# 然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

path = './test_file/'
# 打开文件使用内置的open()函数，传入文件名和标识符就可以了，标识符'r'表示读文件，'w'表示写文件，'a'表示追加到文件末尾，'b'表示以二进制模式打开文件，通常用于图片、视频等媒体文件。
# 例如，下面的代码打开一个文件，并读取它的内容：
# 这里使用了with语句来自动管理文件资源，确保文件用完后正确关闭。
with open(path + 'test.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    print(data)

# 如果文件很大，无法一次性读取到内存，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
# 下面的代码演示了如何逐行读取文件：
with open(path + 'test.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())  # strip()去掉每行末尾的换行符

# file-like objectzhi是指具有read()或write()方法的对象，
# 不一定是文件对象，只要有read()和write()方法，都可以看成是file-like object。
# 例如，内存中的字节流，网络流，甚至自定义的流，都可以看成是file-like object，

# 要读取二进制文件，比如图片、视频等，必须以'b'模式打开文件：
with open(path + 'test.png', 'rb') as f:
    data = f.read()
    print(len(data))

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，指定正确的编码。
# 例如，读取GBK编码的文件：
with open(path + 'test_gbk.txt', 'r', encoding='gbk') as f:
    data = f.read()
    print(data)
# 针对编码不规范的文件，还可以传入errors参数，指定遇到编码错误时的处理方法，
# 比如忽略错误的编码：
with open(path + 'test_unknown.txt', 'r', encoding='utf-8', errors='ignore') as f:
    data = f.read()
    print(data)

# 写文件和读文件类似，也需要先打开文件，指定写模式，然后调用write()方法写入字符串。
# 唯一区别是写文件时，必须指定写模式'w'或者'wb'表示写文本文件或二进制文件。
# 下面的代码演示了如何写文件：
with open(path + 'test_write.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, world!\n')
    f.write('This is a test file.\n')
# 写文件时，write()方法不会自动添加换行符，如果需要换行，必须自己添加'\n'。
# 写入二进制文件和写入文本文件类似，只是要以'b'模式打开文件，然后写入bytes：
with open(path + 'test_bin.dat', 'wb') as f:
    f.write(b'\x00\x01\x02\x03\x04\x05')
# 如果我们希望追加到文件末尾，可以传入'a'以追加（append）模式写入。
with open(path + 'test.txt', 'a', encoding='utf-8') as f:
    f.write('Append this line.\n')