class Student:
    id = ""
    name = ""
    age = 0
    major = ""

    def __init__(self, id: str, name: str, age: int, major: str):
        self.id = id
        self.name = name
        self.age = age
        self.major = major
    
    def showWithoutTitle(self):
        print(f"{self.id}\t{self.name}\t{self.major}\t{self.age}")

    def show(self):
        print("学生ID\t学生名\t专业\t年龄")
        self.showWithoutTitle()
