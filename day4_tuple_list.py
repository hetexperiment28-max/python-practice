

#-----tuple is immutable data type
a = (1,45,46,45, "het")
print(type(a)) #tuple never be changed

#TUPLE METHODS

no = a.count(45)
print(no) #count whole tuple then give answer

i = a.index(45)
print(i)  #only count till he gets required element




#------list is mutable data type

friends = ["Het","hetanshi","ayush","rohan"]
print(friends[0])
friends[0] = "nishi"
print(friends[0])
print(friends[0:3])

##methods of Lists 
friends.append("het")
print(friends)
##append means to add in last and list can modify not like string

l1 = [28, 22, 39, 42, 12]
l1.sort() #ascending order
l1.reverse() #descending order
l1.insert(1, 23)
l1.pop(1) # to show pop value use :  print(l1.pop(1))
l1.remove(22)
print(l1)

