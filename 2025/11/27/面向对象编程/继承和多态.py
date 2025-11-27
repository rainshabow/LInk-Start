# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
# 比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal:
    def run(self) -> None:
        print("Animal is running...")
animal = Animal()
animal.run()
# 如果我们要编写Dog和Cat这两个class，由于它们和Animal有很多共同的地方，
# 我们就可以直接从Animal类继承，新的class定义如下：
class Dog(Animal):
    pass
class Cat(Animal):
    pass
# 这样，Dog和Cat就获得了Animal的run()方法：
dog = Dog()
dog.run()
cat = Cat()
cat.run()
# 当然，也可以对子类增加一些方法，比如Dog类增加一个bark()方法
class Dog1(Animal):
    def bark(self) -> None:
        print("Woof!")
dog1 = Dog1()
dog1.run()
dog1.bark()
# 子类继承父类后，可以重写父类的方法
class Dog2(Animal):
    def run(self) -> None:
        print("Dog is running...")
dog2 = Dog2()
dog2.run()
# 如果想调用父类的方法，可以使用super()
class Dog3(Animal):
    def run(self) -> None:
        super().run()  # 调用父类的方法
        print("Dog is running...")
dog3 = Dog3()
dog3.run()

# 继承的另一个好处是多态
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True
# dog对象同时是Dog和Animal类型
# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类，但是反过来就不行。
print(isinstance(animal, Animal))    # True
print(isinstance(animal, Dog))       # False

# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：
def run_twice(animal: Animal) -> None:
    animal.run()
    animal.run()
run_twice(animal)
run_twice(dog)
# 由于Dog是从Animal继承下来的，所以，传入Dog对象也是完全没有问题的：
# Animal的子类，不必对run_twice()做任何修改，
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。

# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
# 而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
# 这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
# 这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

# 继承还可以一级一级地继承下来，比如，Dog继承Animal，Bulldog又可以继承Dog：
class Bulldog(Dog):
    def run(self) -> None:
        print("Bulldog is running slowly...")
bulldog = Bulldog()
bulldog.run()

# python允许和C++、Java一样进行多重继承
class A:
    def method_a(self) -> None:
        print("Method A")
class B:
    def method_b(self) -> None:
        print("Method B")
class C(A, B):
    pass
c = C()
c.method_a()
c.method_b()

# python同时也允许和C++一样进行多级继承，这与Java不同，Java不支持多级继承
class D(C):
    def method_d(self) -> None:
        print("Method D")
d = D()
d.method_a()
d.method_b()
d.method_d()

# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer:
    def run(self) -> None:
        print("Time is running...")
timer = Timer()
run_twice(timer)  # 仍然有效 #type:ignore
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，
# 只要看起来像鸭子、走起路来像鸭子，那它就可以被看做是鸭子。
# 这种类型的动态特性称为“结构化子类型”（Structural Subtyping），
# 与基于继承的“名义子类型”（Nominal Subtyping）相对。
# Python的“鸭子类型”特点决定了继承不像Java那样是必须的。
# 继承的目的主要是为了代码重用和多态。

# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。
# 许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。