#using day27 code as it is and trying to improve bugs and Bottle necks
#new requirement : duplicate id add prevention , allow only 4 status option , bonus : after any add/remove display total drones 
#new options in menu : 6. Remove drone , 7. Update drone status, 8. Exit


drones = [
    {"id": "DR01", "battery": 85, "status": "Ready"},
    {"id": "DR02", "battery": 18, "status": "Charging"},
    {"id": "DR03", "battery": 62, "status": "Flying"},
    {"id": "DR04", "battery": 95, "status": "Ready"}
]

#menu option 2 : search drone
def search_drone(name):
                for drone in drones:
                    if name.upper().strip() == drone["id"].strip():
                        return("Found")
                
                return("Not Found")
 
allowed_status = ["Ready", "Flying", "Maintenance", "Charging"]


while True :
    print("choose from menu by pressing (1-8)", "\n", "1. Show All Drones:", "\n", 
          "2. Search Drone", "\n", "3. Show Low Battery Drones:", "\n", "4. Show Ready Drones :", "\n",
          "5. Add New Drone :", "\n", "6. Remove Drone :", "\n","7. Update Drone Status :", "\n", "8. Exit", "\n")
    
    try:
        choice = int(input("Enter your choice (1-8): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    match choice :

        case 1:
            # show all drone
            print("List of all Drone")
            for drone in drones:
                print( " id :", drone["id"], "\n", "Battery level :", drone["battery"], "\n", "Status :", drone["status"], "\n")

        case 2:
            #search
            name = (input("Enter drone id to search (EX: DR01) : "))
            print(search_drone(name))

        case 3:
            
            low_battery_drones = []
            for drone in drones:
                if drone["battery"] < 20:
                    text = f"Device with low battery: {drone['id']} ({drone['battery']}%)\n"
                    low_battery_drones.append(text)

            
            print("".join(low_battery_drones))
        
        case 4:
            #print Ready status drones
            ready = False
            print("Drones currently in status : Ready", "\n")
            for drone in drones:
                if drone["status"] == "Ready" :
                    print("id:", drone["id"],"\n", "Battery :", drone["battery"], "\n" )
                    ready = True

            if not ready :
                print("No drone in status ready right now.")

        case 5:
            print("Add new Drone","\n")
            new_id = input("Enter new Drone ID:").strip().upper()
            
            id_found = False

            for drone in drones:
                if new_id == drone["id"]:
                    id_found = True
                    print("Provided Drone Id is already in Fleet. Use different ID")
                    break

            if not id_found :
                

                try:
                    new_batt = int(input("Enter Battery Percentage(0-100%): "))
                    new_status = str(input("Enter Status: ")).strip().capitalize()

                    if new_status in allowed_status:

                        new_drone = {"id": new_id, "battery" : new_batt, "status" : new_status}
                        drones.append(new_drone)
                        print("Added Succesful to fleet.")
                        print("Total fleet size after adding :", len(drones))
                
                    else :
                        print("enter valid status from list :", allowed_status)

                except ValueError:
                    print("Adding fail provide battery details in number.")
                    continue 

        case 6:
            #remove drone
            id_found = False
            print("Drone Remove", "\n")
            remove_id = input("Enter Drone ID to remove :").upper()
            for drone in drones:
                if remove_id == drone["id"] :
                    drones.remove(drone)
                    print("Drone with id",remove_id," Removed succesfully from fleet.")
                    print("Total fleet size after removing: ",len(drones))
                    id_found = True
                    break
            
            if not id_found:
                print("Invalid input : Enter valid ID")


        case 7:
            #update status
            id_found = False
            print("Update Drone Status:", "\n")
            target_id = input("Enter drone id to update its status :").upper().strip()

            

            for drone in drones:
                if target_id == drone["id"] :
                    id_found = True
                    print("Current status of drone :", drone["id"], "status :", drone["status"])
                    new_status = input("Enter new status :").strip().capitalize()
                    
                    
                    if new_status in allowed_status:
                        drone["status"] = new_status
                        print("Update Successfull.")

                    else:
                        print(f"Invalid status input choose from : {allowed_status}")
                        
            if not id_found:
                print("Drone not Found.")

        case 8:
            print("Exiting program...")
            break

        case _ :
            print("Invalid option enter menu choice again.")
