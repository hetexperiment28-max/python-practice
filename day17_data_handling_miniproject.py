students = [
    {"name": "Het", "marks": 85},
    {"name": "Raj", "marks": 90},
    {"name": "Amit", "marks": 70}
]
#Task1: print all students
for student in students:
    print(student["name"] , student["marks"])

#Task2: GRADE

def get_grade(m):
        
    if m >= 90 :
        return ("A")

    if 75 <= m <= 89 :
        return ("B")
   
    if 50 <= m <= 74 :
        return ("C")
     
    if 35 <= m <= 49 :
        return ("D")
     
    else:
        return ("F")
        
print(get_grade(79))
             
#Task3: 
for student in students:
    mark = get_grade(student["marks"])
    name = student["name"]
    print(name, ":" , mark)
       
#Task4: count grades
grade_count = {"A" : 0 , "B" : 0 , "C" : 0 , "D" : 0 , "F" : 0}

for student in students :
    marks = student["marks"]
    grade_c = get_grade(marks)
    if grade_c in grade_count :
        grade_count[grade_c] += 1

for grade, count in grade_count.items() :
    print(f"{grade} : {count}")

#Task5: file store

with open("students.txt", "w") as file :
    for student in students:
        file.write(student["name"])
        
#Task6:
found = False
def find_student(search) :

    for student in students :
        n = student["name"].lower()
        
        if n == search.lower() :
            return("Found")
            found = True
            break
        
    return("Not Found")

print(find_student("Amit"))
