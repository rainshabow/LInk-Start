# 在Python中，一个.py文件就称之为一个模块（Module）
# 模块可以包含函数、类和可执行代码
# 模块的主要作用是组织代码，提升代码的可维护性和重用性
import abc as abc0

# 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）
# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。
# __init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是包名。
from package1 import abc as abc1
from package2 import abc as abc2
from package1.package3 import abc as abc3

# 创建自己的模块时，要注意：
# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
# 模块名不要和系统模块名冲突

import sys
# sys.path.append('/Users/michael/my_py_scripts')
# 修改sys.path，可以添加存放模块的目录
# 环境变量PYTHONPATH中的内容在运行时会自动添加到sys.path

def test():
    args = sys.argv
    # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
    # 运行python3 hello.py获得的sys.argv就是['hello.py']；
    # 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael']。
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败
# 因此, 如下代码仅在该模块文件被直接运行时执行，而在被导入时不执行
if __name__=='__main__':
    test()