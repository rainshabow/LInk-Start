# Python中使用切片可以方便地操作列表、字符串等序列类型的数据。
# 切片通过指定起始和结束索引来获取序列的一部分，语法为：sequence[start:end:step]。
# 其中，start是起始索引（包含），end是结束索引（不包含），step是步长（可选，默认为1）。

# 切片可以用于列表： 
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 获取前5个元素
print(list1[:5])  # 输出: [0, 1, 2, 3, 4]
# 获取索引2到5的元素
print(list1[2:6])  # 输出: [2, 3, 4, 5]
# 获取所有偶数索引的元素
print(list1[::2])  # 输出: [0, 2, 4, 6, 8]
# 获取列表的倒序
print(list1[::-1])  # 输出: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 切片也可以用于字符串
str1 = "Hello, World!"
# 获取前5个字符
print(str1[:5])  # 输出: Hello
# 获取索引7到11的字符
print(str1[7:12])  # 输出: World
# 获取字符串的倒序
print(str1[::-1])  # 输出: !dlroW ,olleH

# 切片还可以用于元组
tuple1 = (10, 20, 30, 40, 50, 60)
# 获取前3个元素
print(tuple1[:3])  # 输出: (10, 20, 30)
# 获取索引2到4的元素
print(tuple1[2:5])  # 输出: (30, 40, 50)
# 获取所有奇数索引的元素
print(tuple1[1::2])  # 输出: (20, 40, 60)
# 获取元组的倒序
print(tuple1[::-1])  # 输出: (60, 50, 40, 30, 20, 10)

# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
    if not len(s) :
        return ''

    start = 0
    end = len(s) - 1
    while(start <= end and s[start] == ' '):
        start += 1
    while(end >= start and s[end] == ' '):
        end -= 1    
    return s[start : end + 1]    

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

