# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。
# 但是，如果我们要编写程序来操作文件和目录怎么办？这时候，就需要使用IO编程。
# 操作系统提供了文件和目录相关的API接口，Python内置的os模块封装了操作系统提供的文件和目录相关的API，Python程序可以直接调用这些API来操作文件和目录。
import os

print(os.name) # 操作系统类型， posix表示Linux、Unix或Mac OS X， nt表示Windows系统。

# 要获取详细的系统信息，可以调用uname()函数：
# print(os.uname()) # posix.uname()函数在Windows上不提供。
# 获取环境变量
print(os.environ) # 获取系统环境变量
print(os.environ.get('PATH')) # 获取某个环境变量的值
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中。
# 查看当前目录的绝对路径：
print(os.path.abspath('.')) # .表示当前目录
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来：
new_dir = os.path.join(os.path.abspath('.'), 'testdir')
# 然后创建一个目录：
os.mkdir(new_dir)
# 删掉一个目录：
os.rmdir(new_dir)
# 把两个路径合成一个路径时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 要拆分路径时，可以使用os.path.split()()函数，它会把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('/home/user/testdir/file.txt')) # ('/home/user/testdir', 'file.txt')
# os.path.splitext()可以直接让你得到文件扩展名：
print(os.path.splitext('/home/user/testdir/file.txt')) # ('/home/user/testdir/file', '.txt') 
# 获取当前目录下的所有目录和文件：
print(os.listdir('.'))
# 获取当前目录下的所有目录：
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 获取当前目录下的所有.py文件：
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
