#day25 : ESP32 Sensor Monitoring System\
# task1 : print all neatly
# task2 : find highest temperature & average humidity
# task3 : print only device : battery < 20%
#task 4 : count : online device & offline device
# task5 : print only device with temperature > 40 
devices = [
    {"id": "ESP01", "temperature": 32, "humidity": 58, "battery": 92, "online": True},
    {"id": "ESP02", "temperature": 45, "humidity": 42, "battery": 18, "online": True},
    {"id": "ESP03", "temperature": 29, "humidity": 65, "battery": 76, "online": False},
    {"id": "ESP04", "temperature": 38, "humidity": 51, "battery": 54, "online": True},
    {"id": "ESP05", "temperature": 48, "humidity": 39, "battery": 12, "online": False}
]

#task1
for device in devices:
    print("ID :", device["id"], "\n", "Temperature :", device["temperature"], "\n", "Humidity :", device["humidity"], "\n", "Battery Percentage :", device["battery"], "\n", "online status :", device["online"], "\n")

#task2
highest_temperature = max(device["temperature"] for device in devices)
print("Highest temperature :", highest_temperature)

average_humidity = sum(device["humidity"] for device in devices)/len(devices)
#task3
for device in devices:
    if device["battery"] < 20 :

        print("Device status with battery less than 20 :", device["id"], "\n", "Temperature :", device["temperature"], "\n", "Humidity :", device["humidity"], "\n", "Battery Percentage :", device["battery"], "\n", "online status :", device["online"], "\n")

#task4
online_device = 0
offline_device = 0
for device in devices:
    if device["online"] == True :
        online_device += 1
    else:
        offline_device +=1

print("Device status count :", "\n", "Online device :", online_device, "\n", "Offline device :", offline_device, "\n")

#task 5
low_battery = []
for device in devices:
    if device["battery"] > 40 :

        print("Device status with battery greater than 40 :", device["id"], "\n", "Temperature :", device["temperature"], "\n", "Humidity :", device["humidity"], "\n", "Battery Percentage :", device["battery"], "\n", "online status :", device["online"], "\n")

#task 6 

def find_device(name):
    for device in devices:

        if name.strip() == device["id"].strip():
            return("Found")
    else:
        return("Not Found")
    
print(find_device("ESP05"))
    
#task7 save

with open("fdevice_report.txt", "w") as file:
    file.write(f"ESP device report data:\n\n")
    file.write(f"Highest Temperature : {highest_temperature} \n")
    file.write(f"Average humidity : {average_humidity} \n")
    file.write(f"Online device count : {online_device} \n")
    file.write(f"Offline device count : {offline_device} \n")
    file.write(f"Low battery devices : {low_battery} \n")


#challenge device id with highest number

for device in devices:
    if device["temperature"] == highest_temperature:
        print("Device with Highest temperature :", "\n", device["id"], "\n", device["temperature"] )