# Python中的条件判断格式如下
a = 10
if a < 5:
    print("a小于5")
elif a > 10:
    print("a大于10")
else:
    print("a介于5和10之间")

# if语句从上到下依次判断条件，直到找到第一个为真的条件，然后执行对应的代码块，
# 之后跳过剩余的elif和else部分。如果没有任何条件为真，则执行else部分的代码块（如果存在）。
# 以下代码只会输出"a大于0"，因为第一个条件为真，后续的elif不会被执行。   
if a > 0:
    print("a大于0")
elif a > 5:
    print("a大于5")
elif a > 8:
    print("a大于8")
      
# if条件可以简写
b = 15
if b:
    print("b为真值")  # 非零数值、非空字符串、非空列表等都被视为真值

# input函数获取的输入默认是字符串类型
c = input("请输入一个数字：")
# 这里会报错，因为c是字符串，不能直接与数字比较
# if c > 0:  
#     print("输入的数字大于0")
# else:
#     print("输入的数字不大于0")    
#需要将输入转换为整数类型
c = int(c)
if c > 0:
    print("输入的数字大于0")
else:
    print("输入的数字不大于0")

# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，
# 并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖    
height = 1.75
weight = 80.5
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")