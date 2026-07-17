#menu driven order management system
#requires : 1. show all order, 2. search by order ID, 3. Add New Order
# 4. Update order status, 5. Show Pending Orders, 6. Order Statistics, 7. Exit

orders = [
    {"id": 101, "customer": "Amit", "material": "PLA", "price": 550, "status": "Pending"},
    {"id": 102, "customer": "Raj", "material": "PETG", "price": 850, "status": "Completed"},
    {"id": 103, "customer": "Het", "material": "ABS", "price": 700, "status": "Printing"},
    {"id": 104, "customer": "Jay", "material": "PLA", "price": 600, "status": "Pending"}
]


#material allows
material_allowed =["PLA","PETG","ABS", "TPU"]
#status allowed
status_allowed =["Pending","Printing","Completed","Cancelled"]

#menu2_find_order
def search_order(id):

    for order in orders:
        if order["id"] == id:
            return("Found")
    else:
        return("Not Found")
    

while True:
    print(" 1. Display all Orders", "\n", "2. Search by Order ID", "\n",
           "3. Add New Order", "\n", "4. Update Order Status", "\n",
            "5. Show Pending Orders", "\n", "6. Order Statistics", "\n", "7. Exit","\n")
    
    try:
        in_choice = False
        choice = int(input("Enter menu choice (1-7):"))
        if 1<= choice <= 7:
            in_choice = True
        if not in_choice:
            print("choice not in menu")
            continue
    except ValueError:
        print("Enter valid input in integer (1-7).")
        continue

    match choice:

        case 1 :
            #show all orders
            for order in orders:
                print("ID:", order["id"], "\n", "Customer:",order["customer"], "\n"
                      ,"Material:", order["material"], "\n", "Price:", order["price"], "\n", "Status:", order["status"], "\n")
                
        case 2 :
            #search by order ID
            try:
                
                id = int(input("Enter order id to search (EX: 101,102) :"))
                print(search_order(id))
            except ValueError:
                print("Enter valid id type.(EX: 101,102)")


        case 3 :
            #Add new order
            print("Add new order.")

            try:
                add_id = int(input("Enter new order id to add:"))
                add_price = int(input("Enter price :"))

            except ValueError:
                print("Enter id and price should be in integer.")
                continue

            id_found = False

            for order in orders:
                if add_id == order["id"]:
                        id_found = True
                        print("Provided order Id is already exists. Use different ID")
                        break
            if not id_found:
             
                add_customer = str(input("Enter Customer Name to add in order id:"))

                try:
                    add_material = str(input("Enter Material :")).upper()

                    if add_material not in material_allowed:
                        print("Enter valid material option from", material_allowed)
                        continue  
                       

                except ValueError:
                        print("Invalid material input type. use only character. ")

                try :
                    add_status = str(input("Enter order status:")).strip().capitalize()
                    if add_status in status_allowed:
                        new_order = {"id": add_id,"customer": add_customer,"material": add_material,"price": add_price,"status": add_status}
                        orders.append(new_order)
                        print("Order added successfully.") 
                        print("Total order count after adding :", len(orders))

                    else:
                       print("Enter valid status from", status_allowed) 

                except ValueError:
                    print("Enter valid status")

                    
        case 4:
            #Update order status
            print("Order status update")
            id_found = False

            find_id = int(input("Enter order id to change its status:"))
            for order in orders:
                if find_id == order["id"]:
                    id_found = True
                    print("Current status of order id:", find_id,"is :",order["status"])
                    new_status = input("Enter new status :").strip().capitalize()

                    if new_status in status_allowed :
                        order["status"] = new_status
                        print("Update Sucessful")

                    else:
                        print("Invalid status input choose from :", status_allowed)
                
            if not id_found:
                print("Order ID not Found.")
            



        case 5:
            #print only pending order
            print("Order details which have status : Pending", "\n")
            for order in orders :
                if order["status"] == "Pending":
                    print("Order id:", order["id"], "\n", "Customer name:", order["customer"], "\n", "Material:", order["material"], "\n", "Price:", order["price"], "\n")

        case 6:
            #order statistics
            print("Order Statistics", "\n")
            print("Total orders:", len(orders),"\n") 

            status_count = {"Printing": 0,"Pending": 0,"Completed" : 0}
            for order in orders:
               if order["status"] in status_count:
                   status_count[order["status"]] += 1

            print("Pending Orders:", status_count["Pending"], "\n", "Completed order:", status_count["Completed"], "\n")

            revenue = sum(order["price"] for order in orders)
            print("Total Revenue:", revenue, "\n")
           
        case 7 :
            print("Exiting Program..")
            break


           


            

                            

                    
                            





            
