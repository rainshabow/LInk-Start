# 函数是最基本的一种代码抽象的方式。
# 它可以将一段代码封装起来，通过函数名来调用，从而提高代码的复用性和可读性。
# 定义一个简单的函数
def greet(name):
    return f"Hello, {name}!"

# 调用函数
print(greet("Alice"))

# 函数可以有多个参数
def add(a, b):
    return a + b
print(add(3, 5))

# 函数可以有默认参数
def power(base, exponent=2):
    return base ** exponent
print(power(4))        # 默认平方
print(power(2, 3))     # 立方

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())  # 输出['END']
print(add_end())  # 输出['END', 'END']，因为默认参数L在函数定义时只被创建一次
# 正确的写法应该是：
def add_end_correct(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end_correct())  # 输出['END']
print(add_end_correct())  # 输出['END']

# 函数可以有可变参数，可变参数允许传入任意数量的参数
# 可变参数在函数内部自动组装为一个tuple
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all(1, 2, 3))        # 输出6
print(sum_all(4, 5, 6, 7, 8))  # 输出30

# Python允许使用*来把一个list或tuple变成可变参数传入函数
nums = [1, 2, 3, 4]
print(sum_all(*nums))

# 函数可以有关键字参数，关键字参数允许传入任意数量的带名字的参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Bob", age=25)

# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
# 至于到底传入了哪些，就需要在函数内部通过kw检查。
def print_info_with_check(**kwargs):
    if 'name' in kwargs:
        print(f"Name: {kwargs['name']}")
    if 'age' in kwargs:
        print(f"Age: {kwargs['age']}")
print_info_with_check(name="Charlie", age=30, city="New York")

# 如果要限制关键字参数的名字，就可以用命名关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def print_info_limited(*, name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")
print_info_limited(name="Diana", age=28)

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def print_info_mixed(*args, city, country):
    for arg in args:
        print(f"Arg: {arg}")
    print(f"City: {city}")
    print(f"Country: {country}")
print_info_mixed(1, 2, 3, city="Los Angeles", country="USA")

# 命名关键字参数必须传入参数名，否则调用会报错
# 但同时, 命名关键字参数允许不按照定义时的顺序传入参数
print_info_mixed(1, 2, 3, country="USA", city="Los Angeles")

# 函数可以返回多个值
# 实际上python函数只能返回一个值，但可以通过返回一个tuple来实现返回多个值的效果
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder
q, r = divide_and_remainder(10, 3)
print(f"Quotient: {q}, Remainder: {r}")

# 函数可以作为参数传递给另一个函数
def apply_function(func, value):
    return func(value)
print(apply_function(lambda x: x * x, 5))  # 输出25

# 函数可以嵌套定义
def outer_function(x):
    def inner_function(y):
        return y * y
    return inner_function(x) + 1
print(outer_function(3))  # 输出10

# 解释器会自动检查函数调用时传入的参数个数是否正确
# 但是自定义函数并不会检查参数类型
# 可以使用isinstance()检查函数的参数类型
def safe_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers.")
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

# 可以使用help()函数查看函数的文档字符串
def sample_function():
    """这是一个示例函数，用于展示文档字符串的用法。"""
    pass
help(sample_function)

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
alias_for_sample = sample_function
help(alias_for_sample)

# 递归函数会导致栈溢出
# Python默认的递归深度限制是1000，可以通过sys模块修改这个限制
# import sys
# print(sys.getrecursionlimit())  # 输出默认递归深度限制
# sys.setrecursionlimit(2000)  # 修改递归深度限制为2000

# 通过尾递归，也即return语句中不包含表达式调用，编译器或解释器可以进行尾递归优化，避免栈溢出的问题
# 但大多数语言并不支持尾递归优化，Python也不例外

# 练习
# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
num = 255
hex_str = hex(num)
print(hex_str)  # 输出'0xff'
# 然后再利用int()函数把十六进制表示的字符串转换回整数：
converted_num = int(hex_str, 16)
print(converted_num)  # 输出255

# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数
# 返回一元二次方程ax^2 + bx + c = 0的两个解。
def quadratic(a, b, c):
    if b**2 - 4*a*c < 0:
        raise ValueError("No real roots.")
    root1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    root2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return root1, root2

# 练习
# 递归解决汉诺塔问题
def move(n, a, b, c):#(count, origin, auxiliary, target)
    if n == 1:
        print(a, '-->', c)
    elif n >= 2:
        move(n - 1, a, c, b) # 将上面的n-1个盘子从A借助C移动到B
        move(1, a, b, c) # 将最下面的盘子从A移动到C
        move(n - 1, b, a, c) # 将B上的n-1个盘子借助A移动到C
move(3, 'A', 'B', 'C')
