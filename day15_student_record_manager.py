students = [
    {"name": "Het", "marks": 85},
    {"name": "Raj", "marks": 90},
    {"name": "Amit", "marks": 70},
    {"name": "Jay", "marks": 95},
    {"name": "Harvis", "marks": 30}
]

#task1
for student in students :
    print(student["name"],student["marks"])

#task2
total_students = len(students)

print("Total Students:", total_students)

#task3 search
search = "Amit"
found = False
for student in students :
    if search == student["name"] :
        print("Found")
        found = True
        break

else :
        print("Not Found")

#task4 
highest_mark = 0
topper_name = None
for student in students :
     if highest_mark < student["marks"]:
          highest_mark = student["marks"]
          topper_name = student["name"]
print("Highest marks: ",highest_mark)

#task5 : lower
minimum =  min(student["marks"] for student in students)
print("Lowest marks:", minimum)


#TASK6 : avg
total_marks = 0

for student in students :
    total_marks += student["marks"]

average = total_marks/total_students
print("Average of total marks :", average) 

#task7
pass_student = 0
fail_student = 0
for student in students:
     if student["marks"] > 35:
          pass_student += 1
     else:
          fail_student += 1
print("pass students:", pass_student)
print("fail students:", fail_student)
 
 #TASK8
print("Topper name : ", topper_name)