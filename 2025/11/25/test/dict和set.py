# Python内置了dict，dict即字典（dictionary），在其他语言中，dict也被称为map，即关联数组或哈希表（hash）。
# dict是一种映射类型，使用键-值（key-value）对存储数据，具有极快的查找速度。
# 举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
# 要查找某个同学的成绩，需要先在names中找到对应的索引位置，再用这个索引位置去scores中取出成绩，效率较低。
for i in range(len(names)):
    if names[i] == 'Bob':
        print(scores[i])
        break
# 使用dict实现，只需要一个dict即可：
scores_dict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# 通过键可以直接获取对应的值，效率非常高。
print(scores_dict['Bob'])
# dict在内部使用哈希表实现，查找速度非常快，不会随着key的增加而变慢。
# 需要注意的是，dict的key必须是不可变类型，比如字符串、整数、元组等，而list是可变类型，不能作为key。

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
scores_dict['Thomas'] = 88
print(scores_dict['Thomas'])
# 如果key已经存在，赋值会覆盖原来的value
scores_dict['Thomas'] = 95
print(scores_dict['Thomas'])
# 如果key不存在，直接访问会抛出KeyError错误，
# 可以使用in判断key是否存在：
print('Thomas' in scores_dict)  # true
print('Jack' in scores_dict)    # false
# 也可以使用get()方法返回None，或者自己指定的value
print(scores_dict.get('Thomas'))  # 95
print(scores_dict.get('Jack'))    # None
print(scores_dict.get('Jack', -1))  # -1

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
scores_dict.pop('Thomas')
print(scores_dict)

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

# 和list比较，dict有以下几个特点：
# *查找和插入的速度极快，不会随着key的增加而变慢；
# *需要占用大量的内存，内存浪费多。
# 而list相反：
# *查找和插入的时间随着元素的增加而增加；
# *占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，可以列出每一个元素并用{}括起来
s = {1, 2, 3}
print(s)  # {1, 2, 3}
# 或者提供一个list作为输入集合，使用set()函数创建
s = set([1, 2, 3])
print(s)  # {1, 2, 3}
# 重复元素在set中会被自动过滤
s = set([1, 2, 2, 3, 3, 3])
print(s)  # {1, 2, 3}
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(4)
s.add(4)
print(s)  # {1, 2, 3, 4}
# 通过remove(key)方法可以删除元素
s.remove(4)
print(s)  # {1, 2, 3}
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # 交集 {2, 3}
print(s1 | s2)  # 并集 {1, 2, 3, 4}
print(s1 - s2)  # 差集 {1}

# set和dict一样，也需要占用大量的内存，内存浪费多。
# set和dict的原理一样，所以set的key也必须是不可变类型。

# 再议不可变对象
# str是不变对象，而list是可变对象
# 对于可变对象，比如list，对list进行操作，list的内容是会变化的
a = ['c', 'b', 'a']
a.sort()
print(a)  # ['a', 'b', 'c']
# 对于不可变对象，比如str，对str进行操作，实际上是创建了一个新的str对象
b = 'abc'
print(b.replace('a', 'A')) # 'Abc'
print(b)  # 'abc'
# 不可变对象调用自身的方法不会改变对象本身，而是会返回一个新的对象
# 这是因为不可变对象一旦创建，对象内部的数据就不能修改。


# 练习
# 请利用set删除list中的重复元素，并按升序排序，输出结果
l = [1, 2, 3, 2, 3, 1, 4, 5, 6, 5]
s = set(l)
l_unique_sorted = sorted(s)
print(l_unique_sorted)  # [1, 2, 3, 4, 5, 6]
# 或者一行代码实现
print(sorted(set(l)))  # [1, 2, 3, 4, 5, 6]

# tuple虽然是不变对象，但试试把(1, 2, 3)和(1, [2, 3])放入dict或set中，并解释结果。
dict_with_tuple_key = {(1, 2, 3): 'a'}
print(dict_with_tuple_key)  # {(1, 2, 3): 'a'}
# dict_with_list_key = {(1, [2, 3]): 'b'}  # 报错，list是可变对象，不能作为dict的key
# print(dict_with_list_key)  # TypeError: unhashable type: 'list'