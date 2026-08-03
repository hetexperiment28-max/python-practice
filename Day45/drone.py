

class Drone:

    def __init__(self, drone_id, battery=100, status="Idle"):
        self.drone_id = drone_id
        self.battery = battery
        self.status = status

    def show_info(self):
        print("DRONE ID :", self.drone_id)
        print("Battery :",self.battery,"%")
        print("Status :", self.status)

    def update_status(self, new_status, battery_used=0):
        self.status = new_status
        self.battery = max(0, self.battery - battery_used)
        print("Status Updated for", self.drone_id)

