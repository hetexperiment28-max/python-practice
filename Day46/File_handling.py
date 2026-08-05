#Daay46 - Craft Labs Inventory Manager

import csv

FILENAME = "inventory.csv"

def load_inventory():
    inventory = []
    try:
        with open(FILENAME, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory.append(
                    {
                        "Material": row["Material"],
                        "Color": row["Color"],
                        "Stock": int(row["Stock"]),
                        "Price": int(row["Price"]),
                    }
                )
    except FileNotFoundError:
        print(f"'{FILENAME}' not found! Make sure it's in the same folder.")

    return inventory


def save_inventory(inventory):
    fieldnames = ["Material", "Color", "Stock", "Price"]
    with open(FILENAME, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(inventory)


def show_inventory(inventory):
    print("\n--- CURRENT INVENTORY ---")
    if not inventory:
        print("Inventory is empty or file not loaded.")
        return

    for item in inventory:
        print(f"{item['Material']}")
        print(f"{item['Color']}")
        print(f"Stock : {item['Stock']}")
        print(f"Price : {item['Price']}")
        print("-" * 20)

def search_material(inventory):
    search_term = input("Enter Material to Search (e.g. PETG): ").strip()
    found = False

    for item in inventory:
        if item["Material"].lower() == search_term.lower():
            if not found:
                print(f"\nFound '{item['Material']}':")
                found = True
            print(f"\n{item['Color']}")
            print(f"Stock : {item['Stock']}")
            print(f"Price : {item['Price']}")
            print("-" * 20)

    if not found:
        print(f"Material '{search_term}' not found in inventory.")

# 4. Low Stock Alert (Stock < 3)
def low_stock_alert(inventory):
    print("\n--- LOW STOCK ALERT (Stock < 3) ---")
    low_stock_items = [item for item in inventory if item["Stock"] < 3]

    if not low_stock_items:
        print("✅ All stock levels are sufficient (no items below 3).")
        return

    for item in low_stock_items:
        print(f"{item['Material']} ({item['Color']})")
        print(f"Stock : {item['Stock']}")
        print(f"Price : {item['Price']}")
        print("-" * 20)


# 5. Add Material
def add_material(inventory):
    print("\n--- ADD NEW MATERIAL ---")
    material = input("Material : ").strip()
    color = input("Color : ").strip()

    try:
        stock = int(input("Stock : "))
        price = int(input("Price : "))
    except ValueError:
        print("❌ Invalid input! Stock and Price must be numbers.")
        return

    new_item = {
        "Material": material,
        "Color": color,
        "Stock": stock,
        "Price": price,
    }
    inventory.append(new_item)
    save_inventory(inventory)
    print(f"✅ Added {material} ({color}) to CSV successfully!")


# 6. Update Stock
def update_stock(inventory):
    print("\n--- UPDATE STOCK ---")
    mat_input = input("Enter Material (e.g. PLA): ").strip()
    color_input = input("Enter Color (e.g. White): ").strip()

    for item in inventory:
        if (
            item["Material"].lower() == mat_input.lower()
            and item["Color"].lower() == color_input.lower()
        ):
            try:
                change = int(
                    input(f"Enter quantity change for {item['Material']} {item['Color']}: ")
                )
            except ValueError:
                print("❌ Invalid number.")
                return

            item["Stock"] = max(0, item["Stock"] + change)
            save_inventory(inventory)
            print(f"New Stock = {item['Stock']}")
            print("CSV updated successfully!")
            return

    print(f"Material '{mat_input}' with color '{color_input}' not found.")


# --- Main Menu Loop ---
def main():
    while True:
        inventory = load_inventory()

        print("\n=== 3D PRINTING FILAMENT INVENTORY ===")
        print("1. Show Inventory")
        print("2. Search Material")
        print("3. Low Stock Alert (< 3)")
        print("4. Add Material")
        print("5. Update Stock")
        print("6. Exit")

        try:
            choice = int(input("\nEnter choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number 1-6.")
            continue

        if choice == 1:
            show_inventory(inventory)
        elif choice == 2:
            search_material(inventory)
        elif choice == 3:
            low_stock_alert(inventory)
        elif choice == 4:
            add_material(inventory)
        elif choice == 5:
            update_stock(inventory)
        elif choice == 6:
            print("Exiting Inventory Manager. Goodbye!")
            break
        else:
            print("Pick a number between 1 and 6.")


if __name__ == "__main__":
    main()
