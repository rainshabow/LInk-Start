# Python中有两种循环语句

# 一种是for...in循环，依次把list或tuple中的每个元素迭代出来
list1 = [1, 2, 3, 4, 5]
tuple1 = ('a', 'b', 'c')
for item in list1:
    print(item)
# for循环可以与range函数结合使用，通过下标迭代一个序列
for i in range(len(tuple1)):
    print(f"下标{i}对应的元素是{tuple1[i]}")

# 另一种是while循环，只要条件满足，就不断循环，直到条件不满足时退出循环
count = 0
while count < 5:
    print(f"count的值是{count}")
    count += 1
# while循环也可以与break、continue和else语句结合使用
# break语句用于退出整个循环
m = 0
while m < 10:
    print(f"当前m的值是{m}")
    if m == 5:
        print("m等于5，退出循环")
        break
    m += 1
# continue语句用于跳过当前循环的剩余代码，进入下一次循环
# 打印1到10之间的所有奇数
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue  # 跳过本次循环，继续下一次循环
    print(f"奇数是{n}")    
# else语句可以与while循环结合使用，当循环条件不满足时执行else语句块
x = 0
while x < 3:
    print(f"x的值是{x}")
    x += 1
else:
    print("循环结束，x不再小于3")

# 练习
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：    
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(f"Hello, {name}")

for i in range(len(L)):
    print(f"Hello, {L[i]}")

i = 0
while i < len(L):
    print(f"Hello, {L[i]}")
    i += 1