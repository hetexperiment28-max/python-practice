#Day 34 : Phase 2

class Drone:

    def __init__(self, drone_id, battery, status):
        self.drone_id = drone_id
        self.battery = battery
        self.status = status

   
    def show_info(self):
        print("Drone id:", self.drone_id)
        print("Battery:", self.battery)
        print("Status:", self.status)

  
    def charge(self):
        if self.battery < 100:
            self.battery = self.battery + 10

            if self.battery > 100:
                self.battery = 100
  

    def fly(self):
        if self.battery < 20:
            return("Battery too low to fly")
        else:
            self.status = "Flying"
            return("Drone is flying")
            

my_drone = Drone(drone_id="ccl-1", battery=15, status="Idle")
my_drone.show_info()
print(my_drone.fly())

my_drone.charge()

print(my_drone.fly())

my_drone.show_info()



#Task2
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        
        if self.marks > 90:
            return("A")
        
        elif 90 >= self.marks > 75:
            return("B")
    
        elif 75 >= self.marks > 50:
            return("C")
        
        else:
            return("F")
        
student_ = Student(name = "Het", marks = 90)
print(student_.grade())