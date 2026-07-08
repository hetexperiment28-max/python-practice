orders = [
    {"id": 101, "customer": "Amit", "material": "PLA", "price": 250, "status": "Completed"},
    {"id": 102, "customer": "Raj", "material": "PETG", "price": 450, "status": "Pending"},
    {"id": 103, "customer": "Het", "material": "PLA", "price": 300, "status": "Completed"},
    {"id": 104, "customer": "Jay", "material": "ABS", "price": 500, "status": "Completed"},
    {"id": 105, "customer": "Harvis", "material": "PLA", "price": 200, "status": "Pending"}
]


#all in on task break it -- print all orders in organized way  
order_no = 1
for order in orders:
    id = order["id"]
    cus = order["customer"]
    mat = order["material"]
    price = order["price"]
    status = order["status"]
    print(order_no,"id :" , id ,"\n" , "customer :" , cus ,"\n" ,"material :" , mat ,"\n" , "price :" , price , "\n" , "status :" , status)
    order_no += 1
#task2 : total revenue

curr_revenue = 0
for order in orders:
    curr_revenue += order["price"]

print("Total Revenue :", curr_revenue)


#task3 : order status counter
pending = 0
completed = 0

for order in orders:
    status = order["status"]
    if status.lower() == "pending":
        pending += 1
    else: 
        completed += 1


print("order status","\n","Completed :", completed,"\n","Pending :", pending)

#task4 :highest order
highest_order = 0
highest_cus = ""
for order in orders:
    cus = order["customer"]
    price = order["price"]
    if price > highest_order :
        highest_order = price
        highest_cus = cus
       
print("Highest order:" , highest_cus,"-", highest_order)

#task5 :custumer ordered pla
material_count = {"PLA": 0 , "PETG": 0 , "ABS": 0}

for order in orders :
    mat = order["material"]
    if mat in material_count :
        material_count[mat] += 1

print("customer orders PLA :", material_count["PLA"])

#CREATE FUNCTION
def find_order(order_id):
       
    for order in orders:
        id = order["id"]
        if order_id == id:
         return ("Found")
         

    else :
        return ("Not Found")
    
print(find_order(103))

with open("report.txt", "w") as file:
    file.write("Craft Labs Report\n\n")
    file.write(f"Completed Orders: {completed}\n")
    file.write(f"Pending Orders: {pending}\n")
    file.write(f"Revenue: {curr_revenue}\n")
    file.write(f"Highest Order: {highest_cus} - {highest_order}\n")


#bonus task: print above avg.

avg = curr_revenue/len(orders)
for order in orders:
    price = order["price"]
    cus = order["customer"]
    if avg < price :
        print(cus ,":", price)