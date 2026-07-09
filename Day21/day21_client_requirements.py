sales = [
    {"order": 201, "customer": "Amit", "material": "PLA", "qty": 2, "price": 300, "city": "Ahmedabad"},
    {"order": 202, "customer": "Raj", "material": "PETG", "qty": 1, "price": 800, "city": "Surat"},
    {"order": 203, "customer": "Het", "material": "PLA", "qty": 3, "price": 320, "city": "Ahmedabad"},
    {"order": 204, "customer": "Jay", "material": "ABS", "qty": 2, "price": 600, "city": "Vadodara"},
    {"order": 205, "customer": "Harvis", "material": "PLA", "qty": 1, "price": 280, "city": "Ahmedabad"}
]

#Task by Manager : "Please prepare today's sales summary. Marketing needs it in 20 minutes."
#Requirements :-
#1. Display every order neatly.
#2. Calculate total sales amount.
#3. Find the customer who spent the most.
#4. Count orders by city.
#5. Display only customers from Ahmedabad.
#6. customer search option

print("Total order Summary :")

#task1
for sale in sales:
    order = sale["order"]
    cus = sale["customer"]
    mat = sale["material"]
    qty = sale["qty"]
    price = sale["price"]
    city = sale["city"]

    print(" order number:",order, "\n", "customer name :", cus, "\n", "Material requirement :", mat, "\n", "Quantity :", qty, "\n", "price :", price, "\n", "city :", city, "\n")

#task2 : total sales amount
sales_amount = 0
for sale in sales:
    qty = sale["qty"]
    price = sale["price"]
    sales_amount += qty*price

print("Total sales amount:", sales_amount)

#task3 highest spent
highest_spent = {}
for sale in sales:
    qty = sale["qty"]
    price = sale["price"]
    cus = sale["customer"]
    highest_spent[cus] = highest_spent.get(cus, 0) + (qty * price) #suggested by google to avoid previous order

print("Highest spent customer :", max(highest_spent.items()))

#Task4: count orders by city
city_names = {"Ahmedabad" : 0, "Surat" : 0,"Vadodara" : 0}
for sale in sales:
    city = sale["city"]
    if city in city_names :
        city_names[city] += 1

for city, count in city_names.items() :
    print(f"{city} : {count}") 

#task5: print ahmedabad customer only
amd_cus = set()
for sale in sales:
    if sale["city"] == "Ahmedabad":
        amd_cus.add(sale["customer"])
        
for customer in amd_cus:
    print(customer, "From Ahmedabad")

#task6 : search
def find_item(search):
    for sale in sales:
        cus = sale["customer"]
        if search.lower() == cus.lower():
            return("Found")
    else:
        return("Not Found")
    
print(find_item("Het"))

#SAVE

with open("daily_sales.txt", "w") as file:
    file.write(f"Craft Labs Sales Summary :\n\n")
    file.write(f"Total sales: {sales_amount}\n")
    file.write(f"Highest customer : {max(highest_spent.items())}\n")
    file.write(f"Ahmedabad orders: {amd_cus}\n")

#bonus
highest_qty = 0
for sale in sales:
    if sale["qty"] > highest_qty:
        highest_qty = sale["qty"]

print("highest qty:", highest_qty)
   