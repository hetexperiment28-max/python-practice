#Day47 - order management
#menu : show order, search order, add order(id generate), update order(then save to json), show pending order, exit

import json

FILENAME = "orders.json"


# 1. Load Orders from JSON
def load_orders():
    try:
        with open(FILENAME, mode="r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"⚠️ '{FILENAME}' not found! Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("⚠️ Error reading JSON file! Corrupted format.")
        return []


# Helper: Save updated orders back to JSON
def save_orders(orders):
    with open(FILENAME, mode="w") as file:
        json.dump(orders, file, indent=4)


# Helper: Format and print a single order neatly
def print_order_card(order):
    print(f"Order ID : #{order['order_id']}")
    print(f"Customer : {order['customer']}")
    print(f"Product  : {order['product']} ({order['material']})")
    print(f"Quantity : {order['quantity']}")
    print(f"Status   : {order['status']}")
    print("-" * 30)


# 1. Show All Orders
def show_all_orders(orders):
    print("\n--- ALL CUSTOMER ORDERS ---")
    if not orders:
        print("No orders found.")
        return

    for order in orders:
        print_order_card(order)


# 2. Search Order by Order ID
def search_order(orders):
    try:
        search_id = int(input("\nEnter Order ID to Search: "))
    except ValueError:
        print("❌ Order ID must be a valid number.")
        return

    for order in orders:
        if order["order_id"] == search_id:
            print(f"\n✅ Order #{search_id} Found:")
            print_order_card(order)
            return

    print(f"❌ Order ID #{search_id} not found.")


# 3. Add Order (Auto-generate Order ID)
def add_order(orders):
    print("\n--- CREATE NEW ORDER ---")
    customer = input("Customer Name : ").strip()
    product = input("Product Name  : ").strip()
    material = input("Material      : ").strip()

    try:
        quantity = int(input("Quantity      : "))
        if quantity <= 0:
            print("❌ Quantity must be at least 1.")
            return
    except ValueError:
        print("❌ Quantity must be a number.")
        return

    # Generate Order ID: Highest existing ID + 1 (or 1001 if list is empty)
    if orders:
        new_id = max(o["order_id"] for o in orders) + 1
    else:
        new_id = 1001

    new_order = {
        "order_id": new_id,
        "customer": customer,
        "product": product,
        "material": material,
        "quantity": quantity,
        "status": "Pending",
    }

    orders.append(new_order)
    save_orders(orders)
    print(f"✅ Order #{new_id} added successfully with status 'Pending'!")


# 4. Update Status
def update_status(orders):
    print("\n--- UPDATE ORDER STATUS ---")
    try:
        target_id = int(input("Enter Order ID to Update: "))
    except ValueError:
        print("❌ Order ID must be a number.")
        return

    for order in orders:
        if order["order_id"] == target_id:
            print(f"\nCurrent Status for #{target_id}: {order['status']}")
            print("Select New Status:")
            print("1. Pending")
            print("2. Printing")
            print("3. Completed")

            choice = input("Enter choice (1-3): ").strip()
            status_map = {"1": "Pending", "2": "Printing", "3": "Completed"}

            if choice in status_map:
                old_status = order["status"]
                order["status"] = status_map[choice]
                save_orders(orders)
                print(
                    f"\n↓\nStatus Updated: {old_status} ➔ {order['status']}"
                )
                print("✅ Saved to JSON successfully!")
            else:
                print("❌ Invalid status choice.")
            return

    print(f"❌ Order ID #{target_id} not found.")


# 5. Show Pending Orders Only
def show_pending_orders(orders):
    print("\n--- PENDING ORDERS ONLY ---")
    pending_list = [o for o in orders if o["status"].lower() == "pending"]

    if not pending_list:
        print("✅ No pending orders currently!")
        return

    for order in pending_list:
        print_order_card(order)


# --- Main CLI Menu Loop ---
def main():
    while True:
        orders = load_orders()

        print("\n=== 3D PRINTING ORDER MANAGEMENT ===")
        print("1. Show Orders")
        print("2. Search Order")
        print("3. Add Order")
        print("4. Update Status")
        print("5. Show Pending Orders")
        print("6. Exit")

while True:

        try:
            choice = int(input("\nEnter choice (1-6): "))
        except ValueError:
            print("❌ Invalid input. Please enter a number 1-6.")
            continue

        match choice:
            case 1:
                show_all_orders(orders)
            case 2:
                search_order(orders)
            case 3:
                add_order(orders)
            case 4:
                update_status(orders)
            case 5:
                show_pending_orders(orders)
            case 6: 
                print("Exiting Order Manager. Goodbye!")
                break
            case _:
                print("Pick a number between 1 and 6.")

