#Day 35 - Phase4
#TITLE : Student Management System V2

#Need to build 2 classes just like real programming experience

class Student:

    def __init__(self, name, marks,):
        self.name = name
        self.marks = marks
        
    def show_info(self):
        print("Name :", self.name)
        print("Marks :", self.marks)
        print("Grade :", self.grade())
        print("--" * 20)

    def grade(self):

         if self.marks >= 90:
             return("A")
         elif self.marks >= 75:
             return("B")
         elif self.marks >= 50:
             return("C")
         else:
             return("F")

    def update_marks(self, new_marks):
        self.marks = new_marks



class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        
    def show_all(self):
        if not self.students:
            print("No students found.")
            return
        for s in self.students:
            s.show_info()

    def search_student(self, name):
            for s in self.students:
                if name == s.name:
                    s.show_info
                    print("Found")
                    break
            else:
                print("Name Not Found")

    def average(self):
        total_marks_count = 0
        
        for s in self.students:
            total_marks_count += s.marks

        avg = total_marks_count/len(self.students)  
        print("Average of marks :", avg)
        print("--" * 20)
    
    def topper_student(self):
        for s in self.students:
            if s.marks >= 90:
                print("Name:", s.name)
                print("Marks:", s.marks)

        print("--" * 20)

    def update_student_marks(self, name, new_marks):
        for s in self.students:
            if s.name == name:
                s.update_marks(new_marks)
                print(f"updater {name}'s marks to {new_marks}.")
                return
        print("Student Not Found")

manager = StudentManager()
manager.add_student(Student("Het",85))
manager.add_student(Student("Raj",92))
manager.add_student(Student("Jay",70))



while True:

    print("1. Show All Students", "\n", "2. Search Student", "\n", "3. Average", "\n",
          "4. Topper", "\n", "5. Update Marks", "\n", "6. Exit", "\n")

    try:
        in_choice = False
        choice = int(input("Enter menu choice (1-6):"))
        if 1<= choice <= 6:
            in_choice = True
        if not in_choice:
            print("choice not in menu")
            continue
    except ValueError:
        print("Enter valid input in integer (1-6).")
        continue

    match choice:

        case 1:
            manager.show_all()

        case 2:
            name = input("Enter student name to search :")
            manager.search_student(name)

        case 3:
            manager.average()

        case 4:
            manager.topper_student()

        case 5:
            name = input("Enter student name to update: ")
            try:
                new_marks = int(input("Enter new marks: "))
                manager.update_student_marks(name, new_marks)
            except ValueError:
                print("Invalid input. Marks must be a number.")
        
        case 6:
            print("Exiting program...")
            break
    

