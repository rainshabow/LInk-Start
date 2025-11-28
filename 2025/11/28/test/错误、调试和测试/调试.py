# 编写程序时总是需要调试
# 在python中，主要有以下几种调试方法：

# 1. 使用print()函数打印变量值，观察程序执行流程
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')
try:
    main()
except ZeroDivisionError:
    print("main()函数中发生了除零错误")
# 这种方法简单直接，但缺点是需要手动添加和删除print语句，且打印的信息有限。

# 2. 使用assert语句断言某个条件，如果条件不成立则抛出AssertionError
def foo2(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main2():
    foo2('0')
try:
    main2()
except AssertionError as e:
    print("main2()函数中发生了除零错误:", e)
# 启动Python解释器时可以用-O参数来关闭assert语句，这样就不会影响程序的性能。

# 3. 使用logging模块记录日志
import logging
# loggin允许我们指定记录信息的级别，有debug、info、warning、error等几个级别
logging.basicConfig(level=logging.INFO)
def foo3(s):
    n = int(s)
    logging.info('info: n = %d' % n)
    logging.debug('debug: n = %d' % n) # 这条日志不会输出，因为默认级别是info
    return 10 / n

def main3():
    foo3('0')
try:
    main3()
except ZeroDivisionError as e:
    logging.error("main3()函数中发生了除零错误: %s" % e)
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

# 4. 使用pdb、ipdb等调试器单步执行代码，设置断点，查看变量值
# 启动程序时，可以用-p参数启动pdb调试器
# python -m pdb your_program.py
# 运行时，可以用命令c继续运行，q退出调试，n单步执行代码，p打印变量值等
# 也可以在代码中直接import pdb，然后调用pdb.set_trace()设置断点
import pdb
def foo4(s):
    n = int(s)
    return 10 / n
def main4():
    pdb.set_trace() # 设置断点
    foo4('0')
try:
    main4()
except ZeroDivisionError as e:
    print("main4()函数中发生了除零错误:", e)
# 这种方法可以让我们以单步方式执行代码，随时查看和修改变量，非常强大。
