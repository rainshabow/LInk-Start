# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和结果，而是返回求和函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f)  # <function lazy_sum.<locals>.sum at 0x000001B2C8C3B550>
print(f())  # 25
# 调用lazy_sum()时，返回的并不是求和结果，而是求和函数。
# 当调用函数f时，才真正计算求和的结果。
# 每次调用lazy_sum()都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)  # False
# f1和f2虽然都是调用lazy_sum(1, 3, 5, 7, 9)返回的函数，但每次调用都会返回一个新的函数对象。
# 闭包
# 在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 注意：返回的函数并没有立刻执行，而是直到调用了f()才执行。

# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 也即防止“闭包陷阱”。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count() # 这里的f1、f2、f3实际上指向同一个函数对象
print(f1())  # 9
print(f2())  # 9
print(f3())  # 9


# 如果一定要引用循环变量怎么办？可以再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count_fixed():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count_fixed()
print(f1())  # 1    
print(f2())  # 4
print(f3())  # 9

# 使用闭包时，内层函数g可以引用外层函数f的参数和局部变量
def f(x):
    def g():
        return x * x
    return g

# 但是，内层函数g不能直接修改外层函数f的参数和局部变量
def f_modify(x):
    def g():
        #x = x + 1  # 这里会报错，因为解释器将x视作g()中的局部变量，但未初始化
        return x
    return g

# 如果要修改x，可以用nonlocal声明
# nonlocal语句用于在函数或其他作用域中使用外层（非全局）变量。
def f_modify_fixed(x):
    def g():
        nonlocal x
        x = x + 1
        return x
    return g
fa = f_modify_fixed(2)
print(fa())  # 3
print(fa())  # 4
fb = f_modify_fixed(5)
print(fb())  # 6
print(fb())  # 7

# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    n = 0
    def counter():
        nonlocal n
        n += 1
        return n
    return counter

counterA = createCounter()
print(counterA())  # 1
print(counterA())  # 2
print(counterA())  # 3
counterB = createCounter()
print(counterB())  # 1
print(counterB())  # 2
print(counterA())  # 4