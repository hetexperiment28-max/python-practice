
from drone import Drone
from manager import FleetManager
from mission import Mission
import utils


def main():
    manager = FleetManager()

    manager.add_drone(Drone("Udan-1", 100, "Idle"))
    manager.add_drone(Drone("Udan-2", 55, "Flying"))

    while True:
        utils.title("drone fleet manager")
        print("1. Show All Drones")
        print("2. Add New Drone")
        print("3. Search Drone")
        print("4. Create & Assign Mission")
        print("5. Exit")
        utils.line()

        try:
            choice = int(input("Enter choice (1-5): "))
        except ValueError:
            print("Invalid input! Enter valid choice number.")
            continue

        match choice:

            case 1:
                manager.show_all()

            case 2:
                utils.title("add new drone")
                d_id = input("Enter Drone ID (e.g. DRONE-01): ").strip()

                try:
                    battery = int(input("Enter Battery Level (0-100): "))
                    if not 0<= battery <=100:
                        print("Battery value must be in between 0-100")

                except ValueError:
                    print("Invalid number.")

                manager.add_drone(Drone(d_id, battery))

            case 3:
                utils.title("Search Drone")

                d_id = input("Enter Drone ID to search: ").strip()
                found_drone = manager.search_drone(d_id)
            
                if found_drone:
                    print("Drone Found:")
                    found_drone.show_info()
                else:
                    print("Drone",d_id,"not found.")

            case 4:
                utils.title("assign mission")
                d_id = input("Enter Drone ID for mission: ").strip()
                drone = manager.search_drone(d_id)

                if drone:
                    m_name = input("Enter Mission Name: ").strip()
                    m_loc = input("Enter Target Location: ").strip()

                    mission = Mission(m_name, m_loc)
                    utils.title("mission details")
                    mission.show_mission()

                    drone.update_status(f"On Mission: {m_name}", battery_used=15)
                else:
                    print(f"Drone",d_id,"not found.")

            case 5:
                print("Exiting Fleet system")
                break

            case _:
                print("Invalid menu input. choose from option (1-5)")
                continue



if __name__ == "__main__":
    main()
    
