# 通过for循环来遍历list或tuple，这种遍历我们称为迭代（Iteration）
# C语言中，for循环只能用来遍历可用整数索引来访问的数组
# Python内置的for循环可以直接作用于任何可迭代对象，包括list、tuple、dict、set、str等。
# 例如，遍历list
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
# 也可以遍历字符串
for ch in 'ABC':
    print(ch)
# Python的for循环还有一个特点，就是可以同时引用两个或多个变量
# 例如，同时遍历两个列表
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for x, y in zip(list1, list2):
    print(x, y)
# 通过for循环遍历dict时，key和value可以同时取出
dict1 = {'a': 1, 'b': 2, 'c': 3}
for key, value in dict1.items():
    print(key, value)
# 如果只想遍历key，可以直接遍历dict
for key in dict1:
    print(key)
# 如果只想遍历value，可以用dict的values()方法
for value in dict1.values():
    print(value)

# 判断一个对象是否是可迭代对象，可以使用collections模块的Iterable类型进行判断
# 注意：Python3.3以后，Iterable需要从collections.abc模块导入
from collections.abc import Iterable
print(isinstance('abc', Iterable))  # str是否可迭代，True
print(isinstance([1, 2, 3], Iterable))  # list是否可迭代，True
print(isinstance(123, Iterable))  # 整数是否可迭代，False
    
# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def find_min_and_max(L):
    if(len(L) == 0): 
        return None, None
    _max = L[0]
    _min = L[0]
    for i in L:
        if(i > _max):
            _max = i
        if(i < _min): 
            _min = i
    return _min, _max

# 测试
if find_min_and_max([]) != (None, None):
    print('测试失败!')
elif find_min_and_max([7]) != (7, 7):
    print('测试失败!')
elif find_min_and_max([7, 1]) != (1, 7):
    print('测试失败!')
elif find_min_and_max([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')