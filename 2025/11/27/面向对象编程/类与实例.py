# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，
# 而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
# 在Python中，定义类是通过class关键字：
# class后面紧跟类名，类名通常是大写开头的单词，紧接着是冒号，然后缩进块内是类的主体内容。
class Student:
    pass

# 定义好了类以后，就可以根据类创建出实例，创建实例是通过类名+()实现的：
bart = Student()
# 创建实例时，类名后面的括号中可以提供参数，这些参数会传递给__init__方法，用于初始化实例的属性。
# 由于我们还没有定义__init__方法，所以创建实例时不需要传入参数。
# 可以自由地给实例绑定属性，比如，给实例绑定一个name属性：
bart.name = "Bart Simpson" # type: ignore
print(bart.name)  # 输出: Bart Simpson # type: ignore

# 由于类本身就是一个模板，所以可以自由地给类绑定属性，这样，所有该类创建的实例都拥有这个属性。
Student.school = "Hogwarts" # type: ignore
print(bart.school)  # 输出: Hogwarts # type: ignore

# 但是，给类绑定的属性，对已有的实例是不起作用的。由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，school等属性绑上去：
class Student1:
    def __init__(self, name: str | None = None, school: str = "Hogwarts"):
        self.name = name
        self.school = school
bart1 = Student1("Bart Simpson")
print(bart1.name)   # 输出: Bart Simpson        
print(bart1.school) # 输出: Hogwarts

# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身
# 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
# 有了__init__方法，在创建实例的时候，就不能传入空参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器会自动把实例变量传进去：
# bart = Student1() # 这样是不行的，会报错

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
# 除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

# 面向对象编程的一个重要特点就是数据封装。在下面的Student2类中，每个实例就拥有各自的name和score这些数据。
class Student2:
    def __init__(self, name: str | None = None, score: int | None = None):
        self.name = name
        self.score = score
    def print_score(self):
        print(f"{self.name}: {self.score}")
bart2 = Student2("Bart Simpson", 59)
lisa2 = Student2("Lisa Simpson", 87)        
# 我们可以通过函数来访问这些数据，比如打印一个学生的成绩：
def print_score(student: Student2):
    print(f"{student.name}: {student.score}")
print_score(bart2)  # 输出: Bart Simpson: 59
print_score(lisa2)  # 输出: Lisa Simpson: 87

# 但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，
# 可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。
# 这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：
bart2.print_score()  # 输出: Bart Simpson: 59
lisa2.print_score()  # 输出: Lisa Simpson: 87

# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：


