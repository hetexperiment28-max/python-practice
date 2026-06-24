marks = {
    "het" : 100,
    "ayush" : 89,
    "nishi" : 90
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

marks.update({"het" : 99, "hetanshi" : 78})
print(marks)

#now 2 example below shows difference between two

print(marks["het"]) #this line gives error if gives wrong name
print(marks.get("het2")) #seems same but if we run this code then "none" shows if invalid name puts

# marks.clear() #clears dictionary
