# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：

# >>> bart = Student('Bart Simpson', 59)
# >>> bart.__name
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute '__name'
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。

# 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# 以单下划线开头的实例变量名，比如_name，也是一种约定俗成的用法，
# 意思是“虽然我可以被访问，但是请把我视为私有变量，不要随意访问”。
# 但是从技术上讲，Python并没有什么“私有变量”，一切都是公开的。
# 但是如果你真的想让外部代码无法访问某个变量怎么办？那就只能把变量名改成__xxx的形式。
# 其实Python解释器会把__name这样的变量名改成_Student__name这样的变量名，
# 也就是说Python解释器会把两个下划线开头的变量名改成_类名__变量名的形式，
# 这样就避免了外部代码直接访问__name变量了。
# 但是外部代码仍然可以通过_Student__name来访问__name变量：
bart = Student('Bart Simpson', 59)
# print(bart.__name)  # 报错
print(bart._Student__name)  # 正确输出Bart Simpson # type: ignore 
# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

# 注意因此而导致的错误写法
bart.__name = "New Name"  # 这实际上是给bart新增了一个__name属性，并不是修改了原有的__name属性
print(bart.__name)  # 输出: New Name
print(bart._Student__name)  # 仍然输出: Bart Simpson # type: ignore 
