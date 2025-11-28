# 继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能。
# 在设计类的继承关系时，通常，主线都是单一继承下来的。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，这种设计通常称之为MixIn。
class Person:
    def greet(self):
        print("Hello!")
class Teacher(Person):
    def teach(self):
        print("Teaching...")
class Student(Person):
    def study(self):
        print("Studying...")
class TA(Teacher, Student):
    pass
ta = TA()
ta.greet()   # 输出: Hello!
ta.teach()   # 输出: Teaching...
ta.study()   # 输出: Studying...

# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，
# 我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
# 这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。