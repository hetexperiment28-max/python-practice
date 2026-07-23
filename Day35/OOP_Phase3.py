class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


#task1
    def show_info(self):
       
        print("Name :", self.name)
        print("Marks :", self.marks)
        print("Grade :", self.grade())
        print("--" * 20)


#task2
    def marks_above(self):
        if self.marks > 75:
            return(self.show_info())

        else:
            return("Not found")

#task3
    def search_student(self, search):
            for s in students:
                if search == s.name:
                    s.show_info
                    print("Found")
                    break
            else:
                print("Name Not Found")


#task4
    def topper_student(self):
        if self.marks >= 90:
            print("Name:", self.name)
            print("Marks:", self.marks)
            
        print("--" * 20)

#task5
    def average(students_list):
        total_marks_count = 0
        
        for s in students:
            total_marks_count += s.marks

        avg = total_marks_count/len(students)
        
        print("Average of marks :", avg)
        print("--" * 20)

#task6
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
        
    
students = [
    Student("Het", 85),
    Student("Raj", 90),
    Student("Jay", 50),
    ]   

     

for s in students:
    s.show_info()


students[1].update_marks(98)

for s in students:
    s.show_info()

print("mARKS ABOVE:", "\n")
for s in students:    
    print(s.marks_above())


for s in students:
    s.topper_student()


Student.average(Student)
Student.search_student(Student, "Het")

