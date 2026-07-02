students = [
    {"name": "Het", "marks": 85},
    {"name": "Raj", "marks": 90},
    {"name": "Amit", "marks": 70}
]
#task1 print names
for student in students:
    name = student["name"]
    print(name)

#task2 print all student with makes
for student in students:
    name_marks = student["name"], student["marks"]
    print(name_marks)

#task3 search
search = "Raj"
found = False
for student in students:
    if student["name"] == search:
     found = True
     break
if found == True:
 print("found")
     
else :
 print("Not Found")

# found = False

# for student in students:
#     if student["name"] == search:
#         found = True
#         break

# if found:
#     print("Found")
# else:
#     print("Not Found")

#task4 highest marks 
highest_marks = 0

for student in students:
   current_marks = student["marks"]
   if current_marks > highest_marks :
      highest_marks = current_marks
   

print(highest_marks)
   
