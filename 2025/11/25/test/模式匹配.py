# 针对某个变量匹配多种情况，Python提供了match语句的模式匹配功能
# match语句与switch语句类似，但更加强大和灵活
# 例如match语句支持复杂的数据结构匹配，而switch语句只能匹配简单的值
# match语句会依次检查每个case模式，直到找到第一个匹配的模式，然后执行对应的代码块
# case _相当于default，用于匹配所有未被前面case匹配到的情况   
str1 = "hello"
match str1:
    case "hello":
        print("匹配到hello")
    case "world":
        print("匹配到world")
    case _:
        print("没有匹配到任何情况")

# match语句除了可以匹配单个值外，还可以匹配多个值、匹配一定范围的值，并且把匹配后的值绑定到变量
num = 15
match num:
    case n if 0 <= n < 10:
        print(f"数字在0到9之间，值为{n}")
    case 10 | 11 | 12 | 13 | 14:
        print("数字在10到14之间")
    case 15:
        print("数字为15")
    case _:
        print("数字不在0到15之间")        
     
# match语句还可以匹配列表，功能非常强大
args = ["gcc", "hello.c", "world.c"]
match args:
    # 第一个case ['gcc']表示列表仅有'gcc'一个字符串，没有指定文件名，报错；
    # 第二个case ['gcc', file1, *files]表示列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，
    # 后面的任意个字符串绑定到*files，它实际上表示至少指定一个文件
    case ["gcc"]:
        print("编译命令没有指定文件")
    case ["gcc", filename, *files]:#匹配gcc后跟一个或多个文件
        print(f"编译文件：{filename}")
        for file in files:
            print(f"编译文件：{file}")
    case _:
        print("不是gcc编译命令")