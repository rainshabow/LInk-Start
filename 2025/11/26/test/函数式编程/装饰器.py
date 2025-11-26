# 由于函数也是一个对象, 所以，通过变量也能调用该函数。
# 函数对象有一个属性__name__, 可以获取函数的名字
def now():
    print("2024-06-10")
f = now
f()  # 2024-06-10
print(now.__name__)  # now
print(f.__name__)    # now

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def nowBeAt():
    print("2024-06-10")
nowBeAt()

# 由于log()是一个装饰器，返回一个函数，所以调用now_beAt()实际上调用的是wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
# wrapper()函数内首先打印日志，然后再调用原始函数。
# 由于返回的函数名字是wrapper, 运行now_beAt.__name__会输出'wrapper'，
# 修正这个问题，可以在wrapper函数上添加@functools.wraps(func)装饰器，
# 这样，wrapper函数就会把原始函数的__name__等属性复制过来：
from functools import wraps
def logFin(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper
@logFin
def nowFin():
    print("2024-06-10")
nowFin()
print(nowFin.__name__)  # nowFin

# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
# 比如，要自定义log的文本：
def logText(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@logText("execute")
def nowText():
    print("2024-06-10")
nowText()
print(nowText.__name__)  # nowText

# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
import time, functools

def metric(fn):
    @wraps(fn)
    def wrapper(*args, **kw):
        start = time.perf_counter_ns()
        res = fn(*args, **kw)
        end = time.perf_counter_ns()
        print('%s executed in %s ms' % (fn.__name__, (end - start) / 1_000_000))
        return res
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# 再思考一下能否写出一个@log的decorator，使它既支持：
# @log
# def f():
#     pass
# 又支持：
# @log('execute')
# def f():
#     pass
def call(text = 'undefined'):
    # 情况1：@log  —> text 是函数
    if callable(text):
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("begin call")
            res = func(*args, **kw)
            print("end call")
            print(f"undefined, {func.__name__}")
            return res
        return wrapper
    else:
        # 情况2：@log('execute')  —> text 是字符串
        def decorator(func):
            @wraps(func)
            def wrapper(*arg, **kw):
                print("begin call")
                res = func(*arg, **kw)
                print("end call")
                print(f"{text}, {func.__name__}")
                return res
            return wrapper
        return decorator

@call
def f1():
    pass

@call()
def f2():
    pass

@call('execute')
def f3():
    pass

f1()
f2()
f3()

# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
# OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。
# Python的decorator可以用函数实现，也可以用类实现。
# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。