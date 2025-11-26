# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
# 在Python中，对匿名函数提供了有限支持。
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 匿名函数没有函数名, 因此不需要担心函数名冲突。
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f(5))  # 25
# 也可以把匿名函数作为返回值返回：
def build(x, y):
    return lambda: x * x + y * y
print(build(3, 4)())  # 25

# 练习
# 请用匿名函数改造下面的代码：
# def is_odd(n):
#     return n % 2 == 1

# L = list(filter(is_odd, range(1, 20)))
L = list(filter(lambda n: n % 2 == 1,range(1, 20)))
print(L)

# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。