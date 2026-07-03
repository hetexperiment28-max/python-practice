students = [
    {"name": "Het", "marks": 85},
    {"name": "Raj", "marks": 90},
    {"name": "Amit", "marks": 70}
]

#task 1 : print name and marks
for student in students :
    a,b = student["name"], student["marks"]
    print(a,b)

#task2 : total length
size = len(students)
print("Total Students =",size)

#task3 : searching
search = "Raj"
found = False

for student in students :
    if student["name"] == search :
        print("Found")
        found = True
        break

    else :
        print("Not Found")

#task4 : highest marks

highest_mark = 0
for student in students:
    current_mark = student["marks"]
    if current_mark > highest_mark :
        highest_mark = current_mark
        
       
print(highest_mark)

#task5: avg marks
total_marks = 0

for student in students :
    total_marks += student["marks"]

average = total_marks/size
print("Average of total marks :", average)


#new student add
students.append({
    "name" : "Jay" ,
    "marks" : 95
})

for student in students:
    print(student["name"], student["marks"])