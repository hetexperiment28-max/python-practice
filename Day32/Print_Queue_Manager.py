#Day 32 : Print Queue Manager for my craft labs business
import random

queue = [
    {"id": 101, "customer": "Amit", "material": "PLA", "hours": 6, "status": "Waiting"},
    {"id": 102, "customer": "Het", "material": "PETG", "hours": 12, "status": "Printing"},
    {"id": 103, "customer": "Raj", "material": "ABS", "hours": 5, "status": "Completed"},
    {"id": 104, "customer": "Jay", "material": "TPU", "hours": 8, "status": "Waiting"}
]

material_allowed = ["PLA", "PETG", "ABS", "TPU", "ASA"]
status_allowed = ["Waiting", "Printing", "Completed"]


#menu 1 : show queue
def print_queue():
    for q in queue:

        print(" ID :", q["id"], "\n", "Customer :", q["customer"], "\n", "Material :", q["material"], "\n",
              "Hours :", q["hours"], "\n", "Status :", q["status"], "\n")

#menu 2 : Search Job
def search_job():
    print("Job Search", "\n")
    search = input("Enter ID or Customer Name to search:").lower().strip()

    first_match = next(
        (q for q in queue if search == str(q["id"]) or search == q["customer"].lower()), None)
    
    if first_match is not None:
        # 1. Print the details right here so the user can see them!
        print("\n--- Match Found ---")
        print(f" ID       : {first_match['id']}")
        print(f" Customer : {first_match['customer']}")
        print(f" Material : {first_match['material']}")
        print(f" Hours    : {first_match['hours']}")
        print(f" Status   : {first_match['status']}\n")
         
        return "Found"
    else:
        print("\n No job found matching that ID or Customer Name.\n")
        return "Not Found"
    
    


#menu 3 : Add print job
def add_job():
    print("Add Print Job", "\n")
    
    try:
        add_customer = str(input("Enter Customer Name:")).capitalize().strip()
        
        while True:
            new_id = random.randint(100,1000)

            if not any(new_id == q["id"] for q in queue):
                print("Id for", add_customer, "is :", new_id)
                

            add_material = str(input("Enter material :")).upper().strip()
        
            if add_material not in material_allowed:
                print("Enter valid material type from", material_allowed)
                break
        
            try:
                add_hours = int(input("Enter printing hours :"))
        
            except ValueError:
                print("Enter valid Hours in integer")
                break

            add_status = str(input("Enter status :")).capitalize().strip()
            if add_status not in status_allowed:
                print("Enter valid status from", status_allowed)
                break

            add_queue = {"id": int(new_id), "customer" : add_customer, "material" : add_material, "hours" : add_hours, "status" : add_status}
            queue.append(add_queue)
            print("New Queue Added Successfully...", "\n")
            break

    except ValueError:
        print("Invalid input type.")
        


#menu4 : update job status
def update_status():
    
    print("Update status..", "\n")
    ask_id = input("Enter ID or Customer Name to update status:").lower().strip()

    for q in queue:
        if ask_id == str(q["id"]) or ask_id == q["customer"].lower().strip():
            print("Current status of", ask_id, "is", q["status"])
            
            update_status = str(input("Enter status to update :")).capitalize().strip()

            if update_status not in status_allowed:
                print("Invalid status type. enter from",status_allowed)
                continue

            else:
                q["status"] = update_status
                print("Status Update Succesfull")


#menu5: show waiting job

def job_status(status):

    print("Jobs which are in waiting status", "\n")
    
    for q in queue:
        if q["status"].capitalize().strip() == status.capitalize().strip():

            print(" ID :", q["id"], "\n", "Customer :", q["customer"], "\n", "Material :", q["material"], "\n",
              "Hours :", q["hours"], "\n","\n")

            
#menu6 : queue summary

def queue_summary():

    waiting_count = sum(1 for q in queue if q["status"].strip().capitalize() == "Waiting")
    printing_count = sum(1 for q in queue if q["status"].strip().capitalize() == "Printing")
    completed_count = sum(1 for q in queue if q["status"].strip().capitalize() == "Completed")
    print("Queue summary:", "\n")
    print("Total queue size :", len(queue), "\n")
    print("Waiting jobs :", waiting_count, "\n")
    print("Printing jobs :", printing_count, "\n")
    print("Completed jobs :", completed_count, "\n")

    total_hour = sum(q["hours"] for q in queue)
    print("Total hours :", total_hour)
     
    

#menu7 : Remove complete job
def remove_completed_job():
    
    for q in queue:
        if q["status"].capitalize().strip() == "Completed":
            queue.remove(q)
    print("Removed Completed jobs Successfully.")
    print("Updated Queue :", "\n")
    print_queue()


while True:

    print("====== PRINT QUEUE MANAGER ======", "\n",

        "1. Show Queue", "\n",

        "2. Search Job", "\n",

        "3. Add Print Job", "\n",

        "4. Update Job Status", "\n",

        "5. Show Waiting Jobs", "\n",

        "6. Queue Summary", "\n",

        "7. Remove Completed Job", "\n",

        "8. Exit", "\n")
    
    try:
        choice = int(input("Enter choice from menu (1-8) :"))

    except ValueError:
        print("Invalid input please enter valid input from (1-8).")
        continue


    match choice:
        case 1:
            print_queue()

        case 2:
            print(search_job())
        
        case 3:
            add_job()

        case 4:
            update_status()

        case 5: 
            status = "Waiting"
            job_status(status)

        case 6:
            queue_summary()

        case 7:
            remove_completed_job()

        case 8:
            print("Exiting peogram...")
            break