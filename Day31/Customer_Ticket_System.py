# day31 : Cuustomer support ticket system
# Task : Build a Customer Support Ticket Manager.
import random

tickets = [
    {"id": 1, "customer": "Amit", "issue": "Broken Part", "status": "Open"},
    {"id": 2, "customer": "Het", "issue": "Late Delivery", "status": "Closed"},
    {"id": 3, "customer": "Raj", "issue": "Wrong Color", "status": "Open"},
    {"id": 4, "customer": "Jay", "issue": "Missing Item", "status": "In Progress"}
]


status_allowed = ["Open","Closed","In Progress"]

#Menu1 : show all tickets
def all_tickets():
    print("All Tickets :", "\n")
    for t in tickets:
        print(" ID :", t["id"], "\n",
                "Customer :", t["customer"], "\n",
                "Issue :", t["issue"], "\n", 
                "Status :", t["status"], "\n")
            


#Menu2 : Search ticket
def search_ticket():
    print("Search Ticket:", "\n")
    search = input("Enter ID or Customer Name to search :").capitalize().strip()

    if any(search == str(t["id"]) or search == t["customer"].capitalize().strip() for t in tickets):
        return("Found")
        
    else:
        return("Not Found")

        
#menu3 : Add Ticket
def add_ticket():
    print("Add ticket :", "\n")
    
    #customer name
    try:
        new_customer = str(input("Enter customer name :")).capitalize().strip()
        print("Hello", new_customer, "\n")

    except ValueError:
        print("Enter valid customer name without any special character")
        

    #id insert
    while True:
        new_id = random.randint(1,1000)

        if not any(new_id == t["id"] for t in tickets):
            break
        

    #issues
    new_issues = input("Please enter your issue :").capitalize()

    #Status
    try:
        new_status = str(input("Enter status of ticket :")).capitalize().strip()
        if new_status not in status_allowed:
            print("Invalid input please enter status from options :", status_allowed)

    except ValueError:
        print(f"Enter valid status type from : {status_allowed} without integer or special character")

    new_ticket = {"id" : new_id, "customer" : new_customer, "issue" : new_issues, "status" : new_status}
    tickets.append(new_ticket)
    print("Ticket added successfully.")


#menu 4 : update status
def update_status() :
    print("Update Ticket Status.", "\n")

    try:
        ask_id = int(input("Enter Ticket id:"))
        for t in tickets:
            if ask_id == t["id"] :
                print("Current status of id :",ask_id, " is", t["status"], "\n")
        
                new_status = str(input("Enter new status to update: "))
                
                if new_status in status_allowed:
                    t["status"] = new_status
                    print("Status Update Succesfull")

                else:
                    print("Enter valid status from :", status_allowed)
                    continue
            
    except ValueError:
        print("Enter valid ID")
        


#menu 5 : Show open tickets
def open_ticket():
    print("Tickets which are in Open status:", "\n")
    
    for t in tickets:
        if t["status"] == "Open":

            print(" ID :", t["id"], "\n",
                "Customer :", t["customer"], "\n",
                "Issue :", t["issue"], "\n", "\n")
            
#menu 6 : Ticket Statistics
def ticket_stats():
    print("Ticket statistics:", "\n")

    print("Total Tickets :", len(tickets), "\n")
    
    print("Open Tickets :", "\n")
    for t in tickets:
        if t["status"] == "Open":

            print(" ID :", t["id"], "\n",
                "Customer :", t["customer"], "\n",
                "Issue :", t["issue"], "\n", "\n")
    
    print("Closed Tickets", "\n")
    for t in tickets:
        if t["status"] == "Closed":

            print(" ID :", t["id"], "\n",
                "Customer :", t["customer"], "\n",
                "Issue :", t["issue"], "\n", "\n")

    
    print("In Progress Tickets", "\n")
    for t in tickets:
        if t["status"] == "In Progress":

            print(" ID :", t["id"], "\n",
                "Customer :", t["customer"], "\n",
                "Issue :", t["issue"], "\n", "\n")
  

while True :
    print("====== SUPPORT TICKET MANAGER ======", "\n", "\n"

        " 1. Show All Tickets", "\n", "2.  Search Ticket", "\n"

        , "3.  Add Ticket", "\n", "4.  Update Ticket Status", "\n", "5.  Show Open Tickets", "\n"

        , "6. Ticket Statistics", "\n", "7. Exit", "\n")
    

    choice = int(input("Enter choice from menu (1-7) :"))

    
    match choice :

        case 1 :
            all_tickets()
        
        case 2 :
            print(search_ticket())
        
        case 3 :
            print(add_ticket())
        
        case 4 :
            print(update_status())
        
        case 5 :
            print(open_ticket())
        
        case 6 :
            print(ticket_stats())

        case 7 :
            print("Exiting program..")
            break
        
        case _:
            print("Invalid option. Choose a number between 1 and 7.\n")