#Day44 smarrt parking management
# for car = 30 , bike = 15 / hour

class Vehicle:

    def __init__(self, vehicle_number, owner_name, entry_time):
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.entry_time = entry_time

    def get_vehicle_type(self):
        return "Vehicle"

    def calculate_fee(self, exit_time):
        hours = max(1, exit_time - self.entry_time)
        return hours * 20
    

class Car(Vehicle):

    def __init__(self, vehicle_number, owner_name, entry_time):
        super().__init__(vehicle_number, owner_name, entry_time)

    def get_vehicle_type(self):
        return "Car"

    def calculate_fee(self, exit_time):
        hours = max(1, exit_time - self.entry_time)
        return hours * 30


class Bike(Vehicle):

    def __init__(self, vehicle_number, owner_name, entry_time):
        super().__init__(vehicle_number, owner_name, entry_time)

    def get_vehicle_type(self):
        return "Bike"

    def calculate_fee(self, exit_time):
        hours = max(1, exit_time - self.entry_time)
        return hours * 15


class ParkingLot:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.parked_vehicles = []  # FIXED: plural name match

    def park_vehicle(self, vehicle_obj):
        if len(self.parked_vehicles) >= self.capacity:
            print("Parking Lot Full! cannot park Vehicle")
            return False

        for v in self.parked_vehicles:
            if v.vehicle_number.lower() == vehicle_obj.vehicle_number.lower():
                print(f"Vehicle '{vehicle_obj.vehicle_number}' already parked.")  # FIXED: readable output
                return False

        self.parked_vehicles.append(vehicle_obj)
        print(vehicle_obj.get_vehicle_type(), vehicle_obj.vehicle_number, "parked successfully!")
        return True

    def remove_vehicle(self, vehicle_number, exit_time):
        # Searching vehicle by number
        for v in self.parked_vehicles:
            if v.vehicle_number.lower() == vehicle_number.lower():
                if exit_time < v.entry_time:
                    print("Exit time cannot be earlier than entry time!")
                    return

                hours = exit_time - v.entry_time
                fee = v.calculate_fee(exit_time)
                
                self.parked_vehicles.remove(v)
                
                print("\n==================================")
                print("      PARKING RECEIPT             ")
                print("==================================")
                print(f" Owner Name    : {v.owner_name}")
                print(f" Vehicle No.   : {v.vehicle_number}")
                print(f" Vehicle Type  : {v.get_vehicle_type()}")
                print(f" Entry Time    : {v.entry_time}:00 hrs")
                print(f" Exit Time     : {exit_time}:00 hrs")
                print(f" Duration      : {hours} hr(s)")
                print(f" Total Fee     : ₹{fee}")
                print("==================================\n")
                return

        print("Vehicle", vehicle_number, "not found in the parking lot.")

    def show_parked_vehicles(self):
        print("CURRENTLY PARKED VEHICLES")
        if not self.parked_vehicles:
            print("No vehicles are currently parked.")
            print("=================================\n")
            return

        print(f"{'Type':<8} | {'Vehicle No.':<12} | {'Owner Name':<15} | {'Entry Time':<10}")
        print("-" * 52)
        for v in self.parked_vehicles:
            print(f"{v.get_vehicle_type():<8} | {v.vehicle_number:<12} | {v.owner_name:<15} | {v.entry_time}:00 hrs")
        print("-" * 52)
        print(f"Available Slots: {self.capacity - len(self.parked_vehicles)} / {self.capacity}\n")


def main():
    lot = ParkingLot(capacity=5)

    while True:
        print("--- SMART PARKING SYSTEM ---")
        print("1. Park Vehicle")
        print("2. Remove Vehicle (Calculate Charges)")
        print("3. Show Parked Vehicles")
        print("4. Exit")

        try:
            choice = int(input("\nEnter choice (1-4): "))
        except ValueError:
            print("❌ Invalid input! Please enter a number between 1 and 4.\n")
            continue

        if choice == 1:
            print("\nSelect Vehicle Type:")
            print("1. Car (₹30/hr)")
            print("2. Bike (₹15/hr)")
            try:
                v_type = int(input("Enter choice (1 or 2): "))
            except ValueError:
                print("❌ Invalid input.\n")
                continue

            v_no = input("Enter Vehicle Number (e.g. GJ01AB1234): ").strip()
            owner = input("Enter Owner Name: ").strip()
            
            try:
                entry = int(input("Enter Entry Time in Hours (0-23): "))
                if not (0 <= entry <= 23):
                    print("❌ Entry time must be between 0 and 23.\n")
                    continue
            except ValueError:
                print("❌ Invalid time format.\n")
                continue

            if v_type == 1:
                lot.park_vehicle(Car(v_no, owner, entry))
            elif v_type == 2:
                lot.park_vehicle(Bike(v_no, owner, entry))
            else:
                print("❌ Invalid vehicle choice.\n")

        elif choice == 2:
            v_no = input("\nEnter Vehicle Number to exit: ").strip()
            try:
                exit_t = int(input("Enter Exit Time in Hours (0-23): "))
                if not (0 <= exit_t <= 23):
                    print("❌ Exit time must be between 0 and 23.\n")
                    continue
            except ValueError:
                print("❌ Invalid time format.\n")
                continue

            lot.remove_vehicle(v_no, exit_t)

        elif choice == 3:
            lot.show_parked_vehicles()

        elif choice == 4:
            print("Exiting Smart Parking System. Have a great day!")
            break

        else:
            print("❌ Choice must be between 1 and 4.\n")


if __name__ == "__main__":
    main()


    

    