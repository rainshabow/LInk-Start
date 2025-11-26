# 1. 高阶函数

# 变量可以指向函数。函数的名称就是指向函数的变量。
# 一个函数可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)
print(add(-5, 6, abs))  # 11
# 传入abs函数作为参数f，返回x和y的绝对值之和。
# 这种把函数作为参数传入的函数称为高阶函数（Higher-Order Function）。

# 1.1 map/reduce
# Python内置的map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 把f(x)作用在list的每一个元素上，并把结果作为新的Iterator返回。
# 由于map()函数返回的是Iterator，因此，通过list()函数让它把整个序列都计算出来并返回一个list。

# map()作为高阶函数，事实上它把运算规则抽象了，
# 因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，
# 比如，把这个list所有数字转为字符串：
r = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))  # ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 2, 3, 4]))  # 1234
# 把序列[1, 2, 3, 4]变换成整数1234。
# 当然，上面的fn函数可以用lambda函数进一步简化：
print(reduce(lambda x, y: x * 10 + y, [1, 2, 3, 4]))  # 1234

# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def nameNormalize(name : str):
    return name[0].upper() + name[1:].lower()
list1 = ['adam', 'LISA', 'barT']
print(list1)
list2 = list(map(nameNormalize, list1))
print(list2)

# 1.2 filter
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1
r = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))  # [1, 3, 5, 7, 9]

# 埃式筛法求素数
def _not_divisible(n):
    return lambda x: x % n > 0
def primes(maxNum):
    yield 2
    it = iter(range(3, maxNum, 2))  # 初始序列
    while True:
        try:
            n = next(it)  # 取当前序列第一个数
        except StopIteration:
            return
        yield n
        it = filter(_not_divisible(n), it)  # 对于得到的每个素数，筛掉它的倍数
str1 = ""
count = 0
for n in primes(1000):
    str1 += str(n) + "\t"
    count += 1
    if count % 10 == 0:
        str1 += "\n"
print(str1)

# 练习
# 回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909。请利用filter()筛选出回数：
def judge(num: int | str) -> bool:
    if isinstance(num, int):
        numStr = str(num)
    else:
        numStr = num
    for i in range(0, len(numStr) // 2):
        if numStr[i] != numStr[-i - 1]:
            return False
    return True
list3 = [123, 121, 1245, "123321", 191, 2, 454, "3443", 4567]
list4 = list(filter(judge, list3))
print(list3)
print(list4)

# 1.3 sorted
# sorted()函数可以对所有可迭代的对象进行排序操作。
print(sorted([36, 5, -12, 9, -21]))  # [-21, -12, 5, 9, 36]
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，
# 例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))  # [5, 9, -12, -21, 36]
# key指定的函数将作用于每个元素上，并根据key函数返回的结果进行排序。
# 例如字符串排序时，默认按照ASCII码的大小进行排序，
# 要忽略大小写排序，可以这么写：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))  # ['about', 'bob', 'Credit', 'Zoo']
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))  # ['Zoo', 'Credit', 'bob', 'about']

# 从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。

# 练习
# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序, 再按成绩从高到低排序。
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def byName(stu) -> str :
    return stu[0]
def byMark(stu) -> int : 
    return stu[1]
print(L)
L1 = sorted(L, key=byName)
print(L1)
L2 = sorted(L, key=byMark, reverse=True)
print(L2)

