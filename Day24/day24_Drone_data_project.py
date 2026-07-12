telemetry = [
    {"time": "10:00", "altitude": 15, "speed": 12, "battery": 98, "gps": True},
    {"time": "10:01", "altitude": 28, "speed": 18, "battery": 92, "gps": True},
    {"time": "10:02", "altitude": 42, "speed": 22, "battery": 84, "gps": True},
    {"time": "10:03", "altitude": 37, "speed": 15, "battery": 76, "gps": False},
    {"time": "10:04", "altitude": 20, "speed": 10, "battery": 68, "gps": True}
]

#task1 : quick data display
print("Telemetry data:","\n")
for data in telemetry:
    print(" Time:", data["time"], "\n","Altitude :", data["altitude"], "\n","Speed :", data["speed"], "\n", "Battery :", data["battery"], "\n", "GPS :", data["gps"],"\n" )


#task 2 find max alt, avg speed
max_altitude = max(data["altitude"] for data in telemetry)
print("Max Altitude :", max_altitude)

speed_avg = sum(data["speed"] for data in telemetry) / len(telemetry)
print("Average Speed :", speed_avg)

#task 3 print all above 80% records
for data in telemetry:
    if data["battery"] > 80 :
         print(" Time:", data["time"], "\n","Altitude :", data["altitude"], "\n","Speed :", data["speed"], "\n", "Battery :", data["battery"], "\n", "GPS :", data["gps"],"\n" )

#task 4 count:
gps_true = 0
gps_false = 0
for data in telemetry:
    if data["gps"] == True:
        gps_true += 1
    else:
        gps_false += 1
print("GPS Diagnosis:", "\n")
print(" GPS Available:", gps_true, "\n", "GPS Lost :", gps_false, "\n")

def find_time(time):
    for data in telemetry:
        if time == data["time"] :
            return("Found")
    else:
        return("Not Found")
print(find_time("10:03"))

#file save
with open("flight_report.txt", "w") as file:
    file.write(f"flight report data:\n\n")
    file.write(f"Max altitude :{max_altitude}\n")
    file.write(f"Average speed :{speed_avg}\n")
    file.write(f"GPS Lost count : {gps_false}\n")


#Challenge
for data in telemetry:
    if data["altitude"] == max_altitude:
        print("Time at max altitude of",max_altitude,"at", data["time"])

