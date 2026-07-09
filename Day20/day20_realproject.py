inventory = [
    {"item": "PLA White", "category": "PLA", "stock": 8, "price": 550},
    {"item": "PLA Black", "category": "PLA", "stock": 2, "price": 600},
    {"item": "PETG Red", "category": "PETG", "stock": 5, "price": 850},
    {"item": "ABS Gray", "category": "ABS", "stock": 1, "price": 700},
    {"item": "PLA Blue", "category": "PLA", "stock": 0, "price": 580}
]

#task 1 : display all inventory neatly
order_no = 1
for stocks in inventory:
    item = stocks["item"]
    cat = stocks["category"]
    stock = stocks["stock"]
    price = stocks["price"]

    print(order_no ,"\n", "Item name :",item,"\n", "category :", cat, "\n","stock qty :",stock, "\n", "price: ",price,"\n")
    order_no += 1

#task 2 : total inventory value
total_stock = 0
total_price = 0
for stocks in inventory:
    stock = stocks["stock"]
    price = stocks["price"]
    total_stock += stock
    total_price += price

inventory_value = total_stock*total_price
print("Total inventory value:",inventory_value)


#task3: product below each category
cate = str(input("Type category name to find products:"))
for stocks in inventory:
    if cate.lower() == stocks["category"].lower():
        print(stocks["item"])

        
#task4: out of stock items display
#task5: display only items with low stock(less than 3)
out_of_stock = ""
for stocks in inventory:
    stock = stocks["stock"]
    item = stocks["item"]
    if stock == 0:
        out_of_stock = item
        print(item,"is out of stock")
    elif stock < 3 :
        print(item,"have low stock")

    
#task6: find most expensive product 
expensive = 0
expensive_pr = ""
for stocks in inventory:
    price  = stocks["price"]
    if expensive < price:
        expensive = price
print(expensive)
for stocks in inventory:
    price = stocks["price"]
    item = stocks["item"]
    if expensive == price:
        expensive_pr = item
        print(item,"is most expensive")



def find_item(search):
    for stocks in inventory:
        item = stocks["item"]
        if search.lower() == item.lower():
            return("Found")
    else:
        return("Not Found")
    
print(find_item("pla white"))

#save 
with open("inventory_report.txt", "w") as file:
    file.write("Craft Labs Report\n\n")
    file.write(f"most expensive item: {expensive_pr}\n")
    file.write(f"total inventory value: {inventory_value}\n")
    file.write(f"out of stock items: {out_of_stock}\n")


#bonus : highest stock without max()
highest_stock = 0
for stocks in inventory:
    stock = stocks["stock"]
    if highest_stock < stock:
        highest_stock = stock
print(highest_stock,"is highest stock")
        