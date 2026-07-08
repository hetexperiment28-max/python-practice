orders = [
    {"customer": "Amit", "material": "PLA", "price": 250},
    {"customer": "Raj", "material": "PETG", "price": 450},
    {"customer": "Het", "material": "PLA", "price": 300},
    {"customer": "Jay", "material": "ABS", "price": 500},
    {"customer": "Harvis", "material": "PLA", "price": 200}
]

for order in orders:
    cus = order["customer"]
    mat = order["material"]
    price = order["price"]

    print(f"{cus} {mat} {price}")

#Task2 : Find total revenue

revenue = 0
for order in orders:
    price = order["price"]
    revenue += price 

print(revenue)

#Task3 : find highest order value

highest_order = 0


for order in orders:
    price = order["price"]
    if price > highest_order :
        highest_order = price
print(highest_order)

#Task4 : count material

material_count = {"PLA": 0 , "PETG": 0 , "ABS": 0}

for order in orders :
    mat = order["material"]
    if mat in material_count :
        material_count[mat] += 1
    
print("material count")
for key , value in material_count.items() :
    print(f"{key} : {value}")

#Task5 : find pla customer
cus_type = {"PLA" : [] , "ABS" : [] , "PETG" : []}


for order in orders :
    cus = order["customer"]
    mat = order["material"]
     
    if mat in cus_type:
        # # Prevent adding the same customer multiple times
        if cus not in cus_type[mat]:
         cus_type[mat].append(cus)


print("PLA customer" , ",".join(cus_type["PLA"]))
#NOW CAN FIND ANY MATERIAL ORDER CUSTOMER 


#Task6 :

def find_customer(name) :
    found = False
     
    for order in orders :
        cus = order["customer"]
        
        if cus.lower() == name.lower() :
            return("Found")
           
            
    else :
        return("Not Found")
        
print(find_customer("harvis"))
        
#task7 : save customer name in file

with open("customer.txt", "w") as file :
    for order in orders:
        file.write(order["customer"] + "\n")
with open("customer.txt", "r") as file :
    file.read()