# Day 39 - Inheritence
# Project : School Management


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("-" * 10)

class Student(Person):

    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def grade(self):
        print("Grade of student :", self.name)
        if self.marks >= 90:
            return("A")
        elif self.marks >= 75:
            return("B")
        elif self.marks >= 50:
            return("C")
        else:
            return("F")
        
class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print("Name :", self.name)
        print("Teaching :", self.subject)
        print("-" * 10)

student = Student("Het",21, 88)
teacher = Teacher("Vinni",33,"Mathematics")


teacher.show_info()

student.show_info()

print(student.grade())

teacher.teach()
