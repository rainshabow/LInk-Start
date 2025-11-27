# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 可以使用内置的 type() 函数来获取对象的类型。
# 基本类型都可以用type()判断：
if type(123) == int:
    print(type(123))          # <class 'int'>
if type('abc') == str:    
    print(type('abc'))        # <class 'str'>
if type([2, 3, 4]) == list:
    print(type([2, 3, 4]))         # <class 'list'>

# type模块中也定义了一些常用的类型常量，可以直接使用这些常量来进行类型判断：
import types
def fn():
    pass
if type(fn) == types.FunctionType:
    print(type(fn))           # <class 'function'>
if type(None) == types.NoneType:
    print(type(None))         # <class 'NoneType'>
if type(abs)==types.BuiltinFunctionType:
    print(type(abs))          # <class 'builtin_function_or_method'>
if type(lambda x: x)==types.LambdaType:
    print(type(lambda x: x))  # <class 'function'>
if type((x for x in range(10)))==types.GeneratorType:
    print(type((x for x in range(10))))  # <class 'generator'>

# 对于class的继承关系来说，使用type()就很不方便。我们要判断一个对象是否是某个类型，使用isinstance()函数：
class Animal:
    pass
class Dog(Animal):
    pass
dog = Dog()
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True
print(isinstance(dog, object))   # True
print(isinstance(dog, str))      # False
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。

# 基础类型也可以用isinstance()判断：
print(isinstance('abc', str))    # True
print(isinstance(123, int))      # True
print(isinstance(b'abc', bytes)) # True
print(isinstance([1, 2, 3], list)) # True
print(isinstance((1, 2, 3), tuple)) # True

# 通过dir()函数，可以获得一个对象的所有属性和方法的列表：
print(dir('abc'))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__sizeof__', '__str__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'upper', 'zfill']
# 类似__开头和结尾的属性和方法在Python中都是有特殊用途的，比如__len__方法返回字符串长度。
# 当然，也可以直接调用len()函数获得字符串长度，实际上，在len()函数内部，它会自动去调用该对象的__len__()方法：
print(len('abc'))  # 3
# 但是，如果调用字符串的__len__()方法也是可以的：
print('abc'.__len__())  # 3

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject:
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

# 紧接着，可以测试该对象的属性：

print(hasattr(obj, 'x')) # 有属性'x'吗？
print(obj.x) # 获取属性'x'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(setattr(obj, 'y', 19)) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(getattr(obj, 'y')) # 获取属性'y'
print(obj.y) # 获取属性'y'
# 如果试图获取不存在的属性，会抛出AttributeError的错误：

# getattr(obj, 'z') # 获取属性'z'
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: 'MyObject' object has no attribute 'z'

# 可以传入一个default参数，如果属性不存在，就返回默认值：
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

#也可以获得对象的方法：
print(hasattr(obj, 'power')) # 有属性'power'吗？
print(getattr(obj, 'power')) # 获取属性'power'
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print(fn) # fn指向obj.power
print(fn()) # 调用fn()与调用obj.power()是一样的

# 一个正确的用法的例子如下：

# 如果传入的对象有read()方法，我们就认为它是一个file-like Object，然后调用read()方法读取数据：
def readImage(fp):
    if hasattr(fp, 'read'):
        return fp.read()
    return None