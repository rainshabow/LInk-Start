#python允许在整数中加入下划线以提高可读性
num = 1_000_0000
if num == 10000000:
    print("10_000_000 == 10000000")
else:
    print("10_000_000 != 10000000")

#python中的二进制、八进制和十六进制表示法
a = 0b1010  # 二进制表示法，等于十进制的10
b = 0o12    # 八进制表示法，等于十进制的10
c = 0xA     # 十六进制表示法，等于十进制的10
#输出结果时会自动转换为十进制
print("a =", a)
print("b =", b)
print("c =", c)

#python中的整数运算永远是精确的，而浮点数运算可能会有精度问题
x = 0.1 + 0.2
print("0.1 + 0.2 =", x) # 输出结果是0.30000000000000004，而不是0.3  

#python中的字符串可以使用单引号、双引号或三引号表示
str1 = 'Hello, World!'
str2 = "Hello, Python!"
str3 = '''Hello, Multi-line
String!'''
print(str1)
print(str2)
print(str3)

#python中常用的转义字符
print("This is a line.\nThis is another line.") # 换行符
print("She said, \"Hello!\"") # 双引号转义
print("This is a backslash: \\") # 反斜杠转义
print("Column1\tColumn2\tColumn3") # 制表符
print("C:\\Users\\Name\\Documents") # 文件路径
print(r"C:\Users\Name\Documents") # 原始字符串，不进行转义

#python支持布尔值与布尔运算
print(True and False)
print(True or False)
print(not True)

#python中，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
#变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
#静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言。
var = 100
print("var =", var)
var = "Now I'm a string"
print("var =", var)

#python中有两种除法运算符：/ 和 //（地板除）
#在C/C++/Java等静态语言中，整数除法的结果仍然是整数，余数会被舍弃掉。
#使用/进行除法运算时，结果总是浮点数
result1 = 7 / 3
print("7 / 3 =", result1) # 输出2.333333333333333
#使用//进行除法运算时，结果是向下取整的整数
result2 = 7 // 3
print("7 // 3 =", result2) # 输出2
#对于负数，向下取整是朝更小的整数方向取整，即对于正负数均是取不大于结果的最大整数
result3 = -7 // 3
print("-7 // 3 =", result3) # 输出-3
#使用%进行取模运算，结果是除法的余数
result4 = 7 % 3
print("7 % 3 =", result4) # 输出1
result5 = -7 % 3
print("-7 % 3 =", result5) # 输出2

#Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，
#变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。
a = 123
b = a
a = 456
print("a =", a) # 输出456, 说明变量a现在指向数据对象456
print("b =", b) # 输出123，说明变量b仍然指向原来的数据对象123，而不是变量a现在指向的数据对象456

#python中的整数类型没有大小限制，只要内存允许，整数可以是任意大的值。
#而在C/C++/Java等静态语言中，整数类型的大小是有限制的，超过限制就会发生溢出错误。
big_int = 1234567890123456789012345678901234567890
print("big_int =", big_int)

#python中的浮点数类型是双精度（64位）浮点数，符合IEEE 754标准
#浮点数的有效位数大约是15-17位十进制数字
#超过有效位数的部分会被舍弃
precise_float = 1.23456789012345678901234567890
print("precise_float =", precise_float) # 输出1.2345678901234567
#浮点数的表示范围大约是1.7E-308到1.7E+308，超出这个范围会被表示为正无穷大（inf）或负无穷大（-inf）
large_float = 1.7e+309
print("large_float =", large_float)  # 输出inf
small_float = 1.7e-309
print("small_float =", small_float)  # 输出0.0