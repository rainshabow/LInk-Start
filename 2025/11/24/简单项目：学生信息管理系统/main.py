from student import Student
import until

students = []

def showstudents():
    if len(students) != 0:
        students[0].show()
        for i in range(1,len(students)):
            students[i].showWithoutTitle()           

def addStudent():
    id = input("请输入学生id：")
    name = input("请输入学生名：")
    age = input("请输入学生年龄：")
    major = input("请输入学生专业：")
    students.append(Student(id, name, age, major))
    print("添加成功！")

if __name__ == "__main__":
    # students.append(Student("0001","赵一",19,"应用数学"))
    # students.append(Student("0002","钱二",16,"理论物理"))
    # students.append(Student("0003","张三",21,"法学"))
    # students.append(Student("0004","李四",20,"哲学"))
    students = until.import_students_from_csv()
    addStudent()
    showstudents()
    until.export_students_to_csv(students)
