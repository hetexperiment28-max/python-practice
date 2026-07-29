#Day41 - polymorphism
# company work management

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work():
        print("Working...")
        


class Developer(Employee):

    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def work(self):
        print("Coding in", self.language)
        print("-" * 20)


class Designer(Employee):

    def __init__(self, name, age, software):
        super().__init__(name, age)
        self.software = software

    def work(self):
        print("Designing in", self.software)
        print("-" * 20)


class Tester(Employee):

    def __init__(self, name, age, tool):
        super().__init__(name, age)
        self.tool = tool

    def work(self):
        print("Testing using", self.tool)
        print("-" * 20)


developer = Developer("Het",21,"Python")
designer = Designer("Vraj",23,"Figma")
tester = Tester("Jainish",23,"Selenium")


employees = [
    developer,
    designer,
    tester
]

for e in employees:
    e.work()