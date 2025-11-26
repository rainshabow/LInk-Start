#python中可以使用偏函数 (partial function)来固定函数的某些参数，从而得到一个新的函数
from functools import partial
int2 = partial(int, base=2)
print(int2('10010'))  # 输出18，因为10010是二进制表示
# 偏函数也可以用来简化函数调用
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数
# 例如，假设我们经常需要调用max函数来比较一组数和一个固定的数10的大小
max5 = partial(max, 10)
print(max5(1, 2, 3, 4, 5, 6, 7))  # 输出7，因为10被作为第一个参数传入max函数
# 偏函数的应用场景非常广泛，可以用来简化函数调用，提高代码的可读性和可维护性。