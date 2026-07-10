orders = [
    {"id": 301, "customer": "Amit", "product": "Drone Frame", "qty": 1, "price": 1800, "status": "Delivered"},
    {"id": 302, "customer": "Raj", "product": "PLA Filament", "qty": 2, "price": 550, "status": "Pending"},
    {"id": 303, "customer": "Het", "product": "GPS Module", "qty": 3, "price": 900, "status": "Delivered"},
    {"id": 304, "customer": "Jay", "product": "Battery", "qty": 1, "price": 2200, "status": "Cancelled"},
    {"id": 305, "customer": "Harvis", "product": "PETG Filament", "qty": 2, "price": 850, "status": "Delivered"}
]
#"Our customer support team needs a report of recent orders. Prepare something useful."

for order in orders:
    id_no = order["id"]
    cus = order["customer"]
    product = order["product"]
    qty = order["qty"]
    price = order["price"]
    status = order["status"]

    print(id_no, "\n", "Customer Name:", cus, "\n", "product :", product, "\n", "quantity:", qty, "\n", "Price:", price, "\n", "status", status, "\n")


#total revenue (ignore cancelled)
total_revenue = 0

for order in orders:
    status = order["status"]
    price = order["price"]
    qty = order["qty"]

    if status != "Cancelled" :  
        total_revenue += qty*price
    else :
        continue


print("Total Revenue:", total_revenue)

#COUNT ORDERS
order_Status = {"Delivered": 0,"Pending": 0,"Cancelled": 0}

for order in orders:
    if order["status"] in order_Status.keys() :
        order_Status[order["status"]] += 1

for key, value in order_Status.items():
    print(key, ":", value)

#highest revenue order

highest_revenue = 0
for order in orders:
    if order["status"] == "Cancelled":
        continue
    elif highest_revenue < order["price"]*order["qty"] :
        highest_revenue = order["price"]*order["qty"]

print("Highest revenue order:", highest_revenue)

#def

def find_product(name):
    for order in orders:
        product = order["product"]
        
        if name.lower() == product.lower():
            return("Found")

    else:
            return("Not Found")
        
print(find_product("petg filament"))

#save
with open("support_report.txt", "w") as file:
    file.write(f"Craft Labs Summary :\n\n")
    file.write(f"Revenue:{total_revenue}\n")
    file.write(f"Delivered order:{order_Status['Delivered']}\n")
    file.write(f" Highest Revenue order: {highest_revenue}\n")

#print above avg price product
product_price = {}
for order in orders:
    product_price[order["product"]] = order["price"]

total_cost = 0
for order in orders:
    total_cost += order["price"]

avg = total_cost/len(orders)

above_avg = {}
for key,value in product_price.items():
    if value > avg:
        above_avg[key] = value

print("Products above average cost:", above_avg)



