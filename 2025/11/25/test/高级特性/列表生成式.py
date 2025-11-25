# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 列表生成式的语法格式为：[expression for item in iterable if condition]，其中expression是表达式，item是变量，iterable是可迭代对象，condition是可选的过滤条件。

# 例如，生成一个包含1到10的平方数的列表：
squares = [x * x for x in range(1, 11)]
print(squares)  # 输出: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 还可以添加条件来过滤元素，例如，生成一个包含1到10中所有偶数的平方数的列表：
even_squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # 输出: [4, 16, 36, 64, 100]

# 列表生成式还可以使用嵌套的for循环，例如，生成一个包含所有可能的坐标点的列表：
points = [(x, y) for x in range(3) for y in range(3)]
print(points)  # 输出: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 列表生成式还可以使用函数调用，例如，生成一个包含1到10的平方根的列表：
import math
sqrt_list = [math.sqrt(x) for x in range(1, 11)]
print(sqrt_list)  # 输出: [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]

# 列表生成式还可以使用多个if条件来过滤元素，例如，生成一个包含1到100中所有能被3和5整除的数的列表：
divisible_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 if x % 5 == 0]
print(divisible_by_3_and_5)  # 输出: [15, 30, 45, 60, 75, 90]

#在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
list1 = [x for x in range(1, 11) if x % 2 == 0] # 生成1到10的偶数列表
list2 = [x if x % 2 == 0 else -x for x in range(1, 11)] # 生成1到10的偶数为正，奇数为负的列表
print(list1)  # 输出: [2, 4, 6, 8, 10]
print(list2)  # 输出: [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

# 练习
# 利用列表生成式，将一个包含多种元素的list中的所有字符串变成小写
list3 = ["Hello", "World", 18 , "Day", 3.14, 'A']
list4 = [s.lower() if isinstance(s, str) else s for s in list3]
print(list3)
print(list4)
