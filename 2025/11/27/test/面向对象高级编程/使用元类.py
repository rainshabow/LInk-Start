# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
# 这就允许动态语言在运行过程中实时创建类和类型。
# 可以使用type()函数动态创建类。
# type()函数既可以返回一个对象的类型，又可以创建出新的类型。
class Hello:
    def hello(self, name='world'):
        print('Hello, %s.' % name)
# 创建出Hello类的对象
h = Hello()
h.hello() # Hello, world.
print(type(Hello)) # <class 'type'>
print(type(h))     # <class '__main__.Hello'>

# 也可以通过type()函数创建出Hello类。
# type()函数的3个参数分别是：
# 1. class的名称；
# 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple单元素的写法；
# 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法hello上。
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)
Hello2 = type('Hello2', (object,), {'hello': fn}) # 创建Hello类
h2 = Hello2() # 创建Hello2类的实例 
h2.hello()  # Hello, world. # type: ignore
print(type(Hello2)) # <class 'type'>
print(type(h2))      # <class '__main__.Hello'>
# 可以看到，使用type()函数创建的类和直接定义的类是完全一样的。
# 实际上，Python解释器遇到class定义时，也是调用type()函数创建出类的。

# 除了使用type()动态创建类以外，还可以是使用metaclass控制类的创建行为，
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
# 看一个简单的例子：
# 定义metaclass，就像定义类一样：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
# 有了ListMetaclass，我们就可以创建出类似list的类，只不过，增加了一个add()方法：
class MyList(list, metaclass=ListMetaclass):
    pass
L = MyList()
L.add(1)
print(L) # [1]
# 可以看到，MyList类继承自list类，由于指定了metaclass=ListMetaclass，
# 因此，在创建MyList类时，ListMetaclass的__new__方法被调用，
# 在__new__方法中，我们给类增加了一个add()方法，然后返回修改后的类。
# 这样，我们创建的MyList类就拥有了list的所有功能，还拥有一个add()方法。  

# 元类的使用比较复杂，一般情况下，不需要使用元类。
# 只有在你需要控制类的创建时，才会考虑使用metaclass。
# 例如在ORM框架中，metaclass就是非常重要的应用。
# ORM全称“Object Relational Mapping”，即对象-关系映射，
# 就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
# 通过metaclass，我们可以扫描类的属性，然后根据属性创建出对应的数据库表结构。
# 因为只有使用者才能定义出符合特定要求的类，
# 所以，ORM的底层框架通常会使用metaclass来自动化地完成这些工作。