#day 27 : fleet manager (make project according to requirement.)
#menu option for customer


drones = [
    {"id": "DR01", "battery": 85, "status": "Ready"},
    {"id": "DR02", "battery": 18, "status": "Charging"},
    {"id": "DR03", "battery": 62, "status": "Flying"},
    {"id": "DR04", "battery": 95, "status": "Ready"}
]



while True :
    print("choose from menu by pressing (1-6)", "\n", "1. Show All Drones:", "\n", 
          "2. Search Drone", "\n", "3. Show Low Battery Drones:", "\n", "4. Show Ready Drones :", "\n",
          "5. Add New Drone :", "\n", "6. Update Drone Status :", "\n", "7. Exit", "\n")
    
    try:
        choice = int(input("Enter your choice (1-7): "))
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
            def search_drone(name):
                for drone in drones:
                    if name.lower() == drone["id"].lower():
                        return("Found")
                
                return("Not Found")
            print(search_drone(name)) 

        case 3:
            
            low_battery_devices = []
            for drone in drones:
                if drone["battery"] < 20:
                    text = f"Device with low battery: {drone['id']} ({drone['battery']}%)\n"
                    low_battery_devices.append(text)

            
            print("".join(low_battery_devices))
        
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

            try:
                new_batt = int(input("Enter Battery Percentage(0-100%): "))
                new_status = str(input("Enter Status: ")).strip().capitalize()

                new_drone = {"id": new_id, "battery" : new_batt, "status" : new_status}
                drones.append(new_drone)
                print("Added Succesful to fleet.")
                print("Total fleet size after adding :", len(drones))

            except ValueError:
                print("Adding fail provide battery details in number.") 

        case 6:
            #update status
            print("Update Drone Status:", "\n")
            target_id = input("Enter drone id to update its status :")

            for drone in drones:
                if target_id == drone["id"] :
                    print("Current status of drone :", drone["id"], "status :", drone["status"])
                    new_status = input("Enter new status :").strip().capitalize()
                    drone["status"] = new_status
                    print("Update Successfull.")

        case 7:
            print("Exiting program...")
            break

        case _ :
            print("Invalid option enter menu choice again.")




                

    


