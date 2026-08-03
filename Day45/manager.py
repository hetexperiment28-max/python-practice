from drone import Drone
import utils
class FleetManager :

    def __init__(self):
        self.drones = []

    def add_drone(self, drone_obj):
        for d in self.drones:
            if d.drone_id.lower() == drone_obj.drone_id.lower():
                print("ID already exists.")
                return False

        self.drones.append(drone_obj)
        print("Done", drone_obj.drone_id, "Added Successfully.")
        return True

    def search_drone(self, drone_id):
        for d in self.drones:
            if d.drone_id.lower() == drone_id.lower():
                return d
        return None

    def show_all(self):
        if not self.drones:
            print("No drones in fleet.")
            return

        for d in self.drones:
            d.show_info()
            utils.line()
