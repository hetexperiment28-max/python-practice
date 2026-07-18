#Day 30 is about practice of making inventory management system for my own business
inventory = [
    {"id": 1, "material": "PLA", "color": "White", "stock": 8},
    {"id": 2, "material": "PETG", "color": "Black", "stock": 3},
    {"id": 3, "material": "ABS", "color": "Gray", "stock": 1},
    {"id": 4, "material": "TPU", "color": "Blue", "stock": 5}
]

material_allowed = ["PLA","ABS","PETG","TPU","ASA"]

#menu2 : search
def find_item(find):
    for item in inventory:
        if find == str(item["id"]):
            return("Found")
        
        elif find.upper().strip() == item["material"].upper().strip() :
            return("Found")

    return("Not Found")  


#menu4 : update stock
def update_stock_find(find):
    for item in inventory:
        if find == str(item["id"]):
            return item
        
        elif find.upper().strip() == item["material"].upper().strip():
            return item
            
    return None
    
        

while True:
    print("MENU :", "\n")
    print("1. Show Inventory","\n", "2. Search Material", "\n", "3. Add New Roll", "\n"
        ,"4. Update Stock", "\n", "5. Low Stock Alert (<3)", "\n", "6. Inventory Summary", "\n"
        ,"7. Exit)", "\n")
    
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

    match choice :

        case 1:
            #show all inventory
            for item in inventory:
                print(" ID:", item["id"], "\n","Material :",item["material"] 
                      ,"\n","Color :" ,item["color"], 
                      "\n","Stock :" ,item["stock"], "\n")
                
        case 2:
            #Search material
            
            find = input("Enter id or material to Search Filament :")
            print(find_item(find))

        case 3:
            #Add new roll
            print("Add New roll")
            
            try:
                new_roll_id = int(input("Enter unique id of material:"))
                
                # Setup a flag variable to track duplicates cleanly before proceeding
                id_exists = False
                for item in inventory:
                    if new_roll_id == item["id"]:
                        id_exists = True
                        print("ID is already in use.please provide different id.\n") 
                        break
                
                if id_exists:
                    continue # Restarts the main menu loop directly if a duplicate is found
                
                new_material = str(input("Enter material :")).upper().strip()
                                              
                if new_material not in material_allowed:
                    print("Entered material was not allowed. Enter from:", material_allowed, "\n")
                    continue
                
                new_color = str(input("Enter color:"))

                try:
                    new_stock = int(input("Enter stock of roll(in kg):"))
                    if new_stock < 0:
                        print("Stock cannot be negative.\n")
                        continue
                                
                except ValueError:
                    print("Invalid stock Input type.\n")
                    continue
                
                # Handled the dict generation outside of the loop structure
                new_roll = {"id": new_roll_id, "material": new_material, "color": new_color, "stock": new_stock}
                inventory.append(new_roll)
                print("New Roll Added Successfully...")
                print("Total material available after adding:", len(inventory), "\n")
                            
            except ValueError:
                print("Enter valid id type. (EX: 1,2,3)\n")
                continue

        case 4:
            # update stock
            print("Stock update", "\n")
            find = input("Enter id or material to update stock: ")
            
            item = update_stock_find(find)
            
            if item == None:
                print("Item Not Found\n")
            else:
                print("Found:", item["material"], f"({item['color']})", "| Current Stock:", item["stock"])
                try:
                    new_stock = int(input("Enter new stock level (in kg): "))
                    if new_stock < 0:
                        print("Stock cannot be negative.\n")
                    else:
                        item["stock"] = new_stock
                        print("Stock updated successfully!\n")
                except ValueError:
                    print("Invalid input. Stock must be a number.\n")


        case 5:
            #Low Stock Filaments <3
            
            print("Low Stock Filaments having less than 3kg :","\n")
            for item in inventory:
                if item["stock"] < 3 :
                    
                    print("ID:", item["id"],"\n", "Material:",item["material"], "\n", "Color:", item["color"], "\n", "Stock:",item["stock"], "\n")
            else:
                print("All filaments are available in good stock.")

        case 6:
            #Inventory Summary
            print("Inventory Summary:", "\n")
            total_unique_items = len(inventory)
            total_kilograms = sum(item["stock"] for item in inventory)
            print(f"1. Total unique material variants: {total_unique_items}")
            print(f"2. Total weight of production asset stock: {total_kilograms} kg\n")
            
                

        case 7: 
            #exit program
            print("Exiting program...")
            break



            

            

    
    
    