orders = [
    {"customer": "Amit", "material": "PLA", "qty": 2, "price": 300},
    {"customer": "Raj", "material": "PETG", "qty": 1, "price": 800},
    {"customer": "Het", "material": "PLA", "qty": 3, "price": 320},
    {"customer": "Jay", "material": "ABS", "qty": 2, "price": 600}
]

#bug 1 
total = 0

for order in orders:
    # total += order["price"]  (qty missing to multiply to count revenue)
    total += order["price"]*order["qty"]

print(total)


#bug 2
highest = 0
for order in orders:
    if order["price"]*order["qty"] > highest:
        highest = order["price"]*order["qty"]
        customer = order["customer"]

print(customer, highest)


#bug 3
def find_customer(name):

    for order in orders:
        if name.lower() == order["customer"].lower():
            return "Found"

    
    return "Not Found"
    
print(find_customer("RAJ"))


#bug 4 : solved  material_count = {}
material_count = {"PLA": 0,"PETG": 0,"ABS": 0}

for order in orders:
    
    if order["material"] in material_count.keys():
         material_count[order["material"]] += 1
        
for material, count in material_count.items():
    print(material, ":", count)


#New feature add print name of customer buys above 2qty
for order in orders:
    if order["qty"] > 2 :
        print("Customer who bought more than 2qty :",order["customer"])

#challenge : without sum() print avg revenue per order
avg_revenue = int(total/len(orders))
print("Average revenue per order:", avg_revenue)