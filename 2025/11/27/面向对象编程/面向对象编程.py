# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
# OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数

# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。
# 为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

# 面向对象的程序设计把数据和操作数据的函数结合起来，组织成一个个“对象”，
# 每个对象都包含了数据和操作数据的函数，称为“方法”（Method）。
# 这样一来，程序就变成了一组对象的集合，这些对象通过彼此之间的方法来通信，从而完成计算任务。

# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。
# 自定义的对象数据类型就是面向对象中的类（Class）的概念。

# 假设我们要编写一个学生信息管理系统
# 如果使用面向过程的编程思想，我们可能会这样设计程序：
# 用一个dict表示学生信息，用list表示学生列表，然后编写一系列函数来操作这些数据结构
# 例如，添加学生、删除学生、修改学生信息、查询学生信息等。
students = []
def add_student(name, student_id):
    student = {'name': name, 'id': student_id}
    students.append(student)
def remove_student(student_id):
    global students
    students = [s for s in students if s['id'] != student_id]
def find_student(student_id):
    for student in students:
        if student['id'] == student_id:
            return student
    return None
def update_student(student_id, name):
    student = find_student(student_id)
    if student:
        student['name'] = name
# 添加学生
add_student("Alice", "S001")
add_student("Bob", "S002")
# 查询学生
student = find_student("S001")
print(student)  # 输出: {'name': 'Alice', 'id': 'S001'}
# 更新学生信息
update_student("S001", "Alice Smith")
print(find_student("S001"))  # 输出: {'name': 'Alice Smith', 'id': 'S001'}


# 这种设计方法在学生信息比较简单的时候是可行的，
# 但是，如果学生信息变得复杂起来，例如需要添加更多的属性（如年龄、性别、成绩等），
# 以及更多的操作（如计算平均成绩、按成绩排序等），那么程序就会变得非常复杂，难以维护。
# 这时，使用面向对象的编程思想会更好一些。

# 如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，
# 这个对象拥有name和score这两个属性（Property）。如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，
# 然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
class Student:
    def __init__(self, name: str, student_id: str) -> None:
        self.name = name
        self.student_id = student_id

    def print_info(self) -> None:
        print(f"Name: {self.name}, ID: {self.student_id}")  

# 通过面向对象的编程思想，我们把数据和操作数据的函数结合在一起，组织成一个个“对象”，
# 每个对象都包含了数据和操作数据的函数，这样一来，程序就变成了一组对象的集合，这些对象通过彼此之间的方法来通信，从而完成计算任务。
# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）。
# 创建学生对象
student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")
# 调用对象的方法
student1.print_info()
student2.print_info()

# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student。
# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。
# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。