# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
# __str__
# __str__()方法返回用户看到的字符串，也就是用print()函数打印一个对象时，打印出来的内容。
class Student:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'Student object (name: {self.name})'
    __repr__ = __str__  # __repr__()返回程序开发者看到的字符串,通常和__str__()的内容一样。
print(Student('Michael'))  # 打印对象，打印的是对象的字符串
# 如果没有定义__str__()，打印出来的实例连名字都没有，显示出来的是<__main__.Student object at 0x10f8f5d90>，很不直观。
# 因为没有__str__，所以，Python解释器才会使用默认的显示方式。
# 有了__str__()，就可以打印出我们想要看到的字符串了

# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib:
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b
    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值
for n in Fib():
    print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# Fib()[5]  # 报错
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib2:
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib2()
print(f[5])  # 8
# 这样就可以按下标访问Fib2的任意元素了。

# 但与普通的list不同，在切片时报错
# print(f[0:5])  # 报错
# 要对切片做出响应，需要在__getitem__()方法中进行判断：
# 下面的代码对Fib3实现了切片的支持：
class Fib3:
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start or 0
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib3()
print(f[0:5])  # [1, 1, 2, 3, 5]
print(f[:10])  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 这样就完全实现了一个可以切片的Fib3了。

# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
# 如果我们想要动态地返回某个属性怎么办？这就需要用到__getattr__()方法了。
class Student2:
    def __init__(self, name):
        self.name = name
    def __getattr__(self, attr):
        if attr == 'name':
            return 'Anonymous'
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25 # 返回函数也是可行的
        raise AttributeError(f"'Student2' object has no attribute '{attr}'")
s = Student2('Bob')
print(s.name)  # Bob #只有在没有找到属性的情况下，才调用__getattr__，已有的属性不会在__getattr__中查找。
print(s.age())   # 25 #type: ignore
print(s.score) # 99

# print(s.height)  # 报错
# 因为height属性不存在，且__getattr__也没有返回，就会抛出AttributeError的错误.

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

# __call__
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student3:
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print(f'My name is {self.name}.')
s = Student3('Charlie')
s()  # My name is Charlie.
# __call__()方法让我们可以直接对实例进行调用，就好像调用一个函数一样。