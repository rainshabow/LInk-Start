# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，
# 但是，没办法检查参数，导致可以把成绩随便改：
class Student:
    def __init__(self, name: str):
        self.name = name
        self.score = 0
bart = Student("Bart Simpson")
bart.score = 9999  # 直接把成绩改成9999分

# 为了限制score的范围，可以将其设为私有属性，
# 然后通过set_score和get_score方法来访问和修改它：
class Student1:
    def __init__(self, name: str):
        self.name = name
        self.__score = 0  # 私有属性

    def set_score(self, score: int):
        if not isinstance(score, int):
            raise ValueError("Score must be an integer")
        elif 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("Score must be between 0 and 100")

    def get_score(self) -> int:
        return self.__score
    
bart1 = Student1("Bart Simpson")
try:
    bart1.set_score(150)  # 错误设置成绩
except ValueError as e:
    print(e)
bart1.set_score(90)  # 正确设置成绩

# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
# Python内置的@property装饰器允许将一个方法以属性的方式调用
class Student2:
    def __init__(self, name: str):
        self.name = name
        self.__score = 0  # 私有属性

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, score: int):
        if not isinstance(score, int):
            raise ValueError("Score must be an integer")
        elif 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("Score must be between 0 and 100")
bart2 = Student2("Bart Simpson")
try:
    bart2.score = 150  # 错误设置成绩
except ValueError as e:
    print(e)
bart2.score = 95  # 正确设置成绩
print(bart2.score)  # 95

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student3(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
    
# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
# 要特别注意：属性的方法名不要和实例变量重名。例如，以下的代码是错误的：

class Student4(object):
    # 方法名称和实例变量均为birth:
    @property
    def birth(self):
        return self.birth
# 这是因为调用s.birth时，首先转换为方法调用，在执行return self.birth时，又视为访问self的属性，
# 于是又转换为方法调用self.birth()，造成无限递归，最终导致栈溢出报错RecursionError。

# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    _width : int | None = None
    _height : int | None = None

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def resolution(self):
        if self._width and self._height:
            return self._width * self._height    # type: ignore

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            print("error type")
        elif value < 0 :
            print("error range")
        else :
            self._width = value        

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            print("error type")
        elif value < 0 :
            print("error range")
        else :
            self._height = value  
    

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')