 #Day33 : Basic OPP understanding class, __init__ , object , self


#EX1
class Drone:

    def __init__(self, drone_id, battery):
        self.drone_id = drone_id
        self.battery = battery

dr1 = Drone("DR01", 85)

# no need to use drone["id"] by replacing it with this method
print(dr1.drone_id) 
print(dr1.battery)



#EX2
# The Class (Blueprint)
class Car:
    def __init__(self, color, brand):
        self.color = color  # Attribute
        self.brand = brand  # Attribute

    def drive(self):       # Behavior
        print(f"The {self.color} {self.brand} is driving!")

# The Objects (Actual Instances)
car1 = Car("Red", "Tesla")
car2 = Car("Blue", "BMW")

car1.drive() # Output: The Red Tesla is driving!


#SELF TEST
#Task1
class student :

    def __init__(self, name,marks):
        self.name = name
        self.marks = marks 

student1 = student("Het",88)
student2 = student("Shrey",67)
student3 = student("Harvish",66)

print(student1.name)
print(student1.marks)
print(student2.name)
print(student2.marks)
print(student3.name)
print(student3.marks)


#Task2
class Drone:
    def __init__(self,id,battery,status):
        self.id = id
        self.battery = battery
        self.status = status
        
Drone1 = Drone(1,56,"Flying")
Drone2 = Drone(2,85,"Service")
Drone3 = Drone(3,65,"Idle")

print(Drone1.id)
print(Drone1.battery)
print(Drone1.status)

print(Drone2.id)
print(Drone2.battery)
print(Drone2.status)

print(Drone3.id)
print(Drone3.battery)
print(Drone3.status)


#Task3
class Filament:
    def __init__(self, material, color, stock):
        self.material = material
        self.color = color
        self.stock = stock

Filament1 = Filament("PLA", "White", 8)
Filament2 = Filament("PETG", "Black", 4)

print(Filament1.material)
print(Filament1.color)
print(Filament1.stock)

print(Filament2.material)
print(Filament2.color)
print(Filament2.stock)
