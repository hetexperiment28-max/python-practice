students = [
    {"name": "Het", "marks": 85},
    {"name": "Raj", "marks": 90},
    {"name": "Amit", "marks": 70},
    {"name": "Jay", "marks": 95},
    {"name": "Harvis", "marks": 30}
]
#Task1 : grade system
def gradesystem(m) :
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

for student in students:
    name = student["name"] 
    marks = student["marks"]
    
    grade = gradesystem(marks)
    print(name , grade)

#Task 2 : count grade category
grade_count = {"A":0 , "B":0 , "C":0 , "D":0 , "F":0}

for student in students:
    marks = student["marks"]
    grade_C = gradesystem(marks)
     
    if grade_C in grade_count:
        grade_count[grade_C] += 1

print("grade category:")
for grade, count in grade_count.items() :
    
    print(f"{grade} : {count}")
   

    
#Task 3 : top3 highest marks  print
first = 0
second = 0
third = 0

unique = sorted(students, key=lambda x: x["marks"], reverse=False)
first = unique[-1]["marks"]
second = unique[-2]["marks"]
third = unique[-3]["marks"]
print(f"{"1st"} : {first}")
print(f"{"2st"} : {second}")
print(f"{"3st"} : {third}")

    
#Task 4 : Search Student Function
search = str(input("enter student name for search:"))
found = False
for student in students :
    if search.lower() == student["name"].lower() :
        print("Found")
        found = True
        break

else :
        print("Not Found")

#Task 5 : Student scoring above everage

total = len(students)

total_marks = 0
for student in students :
    total_marks += student["marks"]

average = total_marks/total
print("Average of total marks :", average) 

above_avg = []
for student in students:
    
    if student["marks"] > average :
        above_avg.append(student["name"])
print(f"{above_avg}")