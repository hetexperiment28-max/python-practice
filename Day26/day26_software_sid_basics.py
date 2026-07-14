#day26 different steps.. now diving into real software work(asking for user input)
#task1 : display all device
#task2 : search : 
# [show all , search device, show low battery devices, show highest battery device, add new device, exit]
#task 3 : device have <20% battery 
#task 4 : display highest temperature device id with temperature
#task 5 : ask for id, temperature, battery add device
devices = [
    {"id": "ESP01", "temperature": 32, "battery": 92},
    {"id": "ESP02", "temperature": 45, "battery": 18},
    {"id": "ESP03", "temperature": 29, "battery": 76},
    {"id": "ESP04", "temperature": 38, "battery": 54},
    {"id": "ESP05", "temperature": 48, "battery": 12}
]
#all menu logics
#menu: 1 all device info print
choice_1 = ()

#starting
name = str(input("please enter your good name :"))
print(f"Hello {name}") 

while True :

    print("MENU :", "\n", "1. Show all devices", "\n", "2. Search device", "\n", 
    "3. Show low battery temperature", "\n", "4. Show Highest battery temperature", "\n",
    "5. Add new device", "\n", "6. Exit", "\n")

    try:
        choice = int(input("Enter your choice (1-6): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    

    match choice :
        case 1:
            print("current devices", "\n")
         
            for device in devices:
                print("ID :", device["id"], "\n", "Temperature :", device["temperature"], "\n", "Battery :", device["battery"], "\n")

        case 2: 
            #menu : 2 search
            name = input("Enter device id to search :")
            def find_device(name):
                
                for device in devices:

                    if name.lower() == device["id"].lower():
                        return("Found")
                else:
                    return("Not Found")
            print(find_device(name))

        case 3:
            low_battery_devices = []
            for device in devices:
                if device["battery"] < 20:
                # Create a clean status string for each low battery device
                    text = f"Device with low battery: {device['id']} ({device['battery']}%)\n"
                    low_battery_devices.append(text)

                print("".join(low_battery_devices))
                    # Print the results cleanly
                
        case 4:
            choice_4_highest_temp = max(device["temperature"] for device in devices)
            for device in devices:
                if choice_4_highest_temp == device["temperature"]:
                    print("device with highest temperature:", device["id"], "with temperature :", choice_4_highest_temp)
            

        case 5:
            #menu : 5 add new
            def add_new() :
                print("Add new device :")
                new_id = input("Enter Device id : ").strip().upper()
                
                try:
                    new_temp = int(input("Input new temperature: "))
                    new_batt = int(input("Enter battery level : "))
                except ValueError:
                    print("ERROR (Device adding fail) : MUST BE IN NUMBERS")
                    
                
                new_device = {
                    "id": new_id,
                    "temperature": new_temp,
                    "battery": new_batt
                    }
                devices.append(new_device)

            add_new()
            #challenge option to add total device after adding
            print("total_device after adding :", len(devices))

        case 6:
            print("program exit")
            break






