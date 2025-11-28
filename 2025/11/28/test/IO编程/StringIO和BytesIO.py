# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# Python内置的StringIO和BytesIO就是在内存中读写str和bytes。
from io import StringIO, BytesIO
# StringIO顾名思义就是在内存中读写str。
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
f = StringIO()
f.write('Hello, world!')
print(f.getvalue())  # 获取写入后的str内容
# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
# BytesIO顾名思义就是在内存中读写bytes。
# 要把bytes写入BytesIO，我们需要先创建一个BytesIO，然后，像文件一样写入即可：
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())  # 获取写入后的bytes内容
# 要读取BytesIO，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())  # 读取bytes

# StringIO和BytesIO是在内存中操作str和bytes的方法，使得读写内存和读写文件具有一致的接口。