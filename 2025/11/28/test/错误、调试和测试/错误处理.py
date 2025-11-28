# 高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
# 通过这种机制，我们可以捕获程序运行过程中出现的异常，并进行相应的处理，保证程序不会因为一个小错误就完全崩溃。
# 下面是一个简单的例子，演示如何使用try...except...finally结构来处理异常：
a = '0'
try:# 监控可能出错的代码块
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e: # 捕获到特定类型的异常将会执行的代码块
    print('except:', e)
except ZeroDivisionError as e: # 捕获到特定类型的异常将会执行的代码块
    print('except:', e)
else: # 如果没有发生异常将会执行的代码块
    print('no error!')
finally: # 无论是否发生异常，都会执行的代码块
    print('finally...')
print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException。
# 因此，在捕获错误时，不仅捕获该类型的错误，也会捕获其子类的错误。
def foo(s):
    return 10 / int(s)

try:
    foo('0')
except ValueError as e:
    print('ValueError:', e)
except UnicodeError as e: # 该语句不会捕获到任何异常，因为UnicodeError是ValueError的子类 # type: ignore
    print('UnicodeError:', e)

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
main()

# 也就是说，不需要在每个调用foo()的地方去捕获错误，只需要在合适的层次捕获错误就可以了。

# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
# 既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
# Python内置的logging模块可以非常方便地记录错误堆栈信息：
import logging

def main2():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main2()
print('END')

# 因为错误是class，捕获错误就是捕获该类的一个实例。
# 所有，错误不是凭空产生的，而是有意创建并抛出的。
# 我们自己编写的函数，也可以抛出错误。
class FooError(ValueError):
    pass
def foo2(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
try:
    foo2('0')
except FooError as e:
    print('FooError:', e)

# 只有在必要的时候才定义我们自己的错误类型，尽量使用Python内置的错误类型。

# 以下是一种常见的错误处理方式：
def foo3(s):
    return 10 / int(s)
def bar3(s):
    return foo3(s) * 2
def main3():
    try:
        bar3('0')
    except Exception as e:
        print('bar3 Caught an exceptio:', e)
        raise
try:    
    main3()
except Exception as e:
    print('Main Caught an exception:', e)
# 这种方式可以让错误信息往上传递，同时在每一层都可以增加一些自己的信息。
# 很多时候，当前函数并不知道该如何处理错误，只能一层一层往上抛，让顶层调用者去处理。
# raise语句如果不带参数，就会把当前错误原样抛出。
# raise语句还可以把一种类型的错误转化成另一种类型。
# 这种方式在需要屏蔽底层错误信息的时候很有用。
# 但注意，在处理异常时，应该尽量保留原始错误信息，不应当将原始错误转换为毫不相关的错误。

# 程序也可以主动抛出错误，让调用者来处理相应的错误。
# 但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。