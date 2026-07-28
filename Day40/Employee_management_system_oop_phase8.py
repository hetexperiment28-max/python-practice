#Day40 - oop Phase 8 (Method Overriding)
#employee management system

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name :", self.name)
        print("Age :", self.age)


class Developer(Person):

    def __init__(self, name, age, language):

            super().__init__(name, age)
            self.language = language

    def show_info(self):
        super().show_info()
        print("Language :", self.language)

    def code(self):
        print("Code in", self.language)
        print("-" * 15)


        
class Designer(Person):

    def __init__(self, name, age, software):
    
                super().__init__(name, age)
                self.software = software

    def show_info(self):
        super().show_info()
        print("Software :", self.software)

    def design(self):
        print("Design in", self.software)
        print("-" * 15)

developer = Developer("Het",21, "Python")
designer = Designer("Jay", 23, "Canva")


designer.show_info()
designer.design()

developer.show_info()
developer.code()