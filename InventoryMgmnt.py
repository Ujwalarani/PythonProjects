"""Project
You are tasked with creating a simple inventory management system for a market. The system should allow users to add,
update, view, and remove items from the inventory. Each item in the inventory will have a name, price, quantity, and category.
Functionality:
Add Item: Create a function add_item that allows users to add a new item to the inventory. Users should input the name,
price, quantity, and category of the item.
Update Item: Implement a function update_item that allows users to update the details of an existing item in the
inventory. Users should be able to update the price, quantity, and category of the item.
View Inventory: Develop a function view_inventory that displays all items in the inventory along with their details
(name, price, quantity, and category).
Remove Item: Create a function remove_item that allows users to remove an item from the inventory based on its name.
Search by Category: Implement a function search_by_category that allows users to search for items in the inventory
based on their category. The function should display all items belonging to the specified category.
Project Structure:
Define a list inventory to store the items in the market inventory. Each item should be represented as a dictionary
with keys for name, price, quantity, and category.
Implement the functions add_item, update_item, view_inventory, remove_item, and search_by_category to manage the
inventory. Create a main loop to interact with the user. The loop should prompt the user to choose from various options
such as adding, updating, viewing, removing items, or searching by category."""

# Inventory list to store items related to SmartCart Organization
smart_cart_inventory = []


# Function to add an item
def add_item():
    name = input("Enter item name: ")
    # Check if item already exists
    if not name:
        print("No item got added! Item name cannot be empty.")
        return

     # Check if item name contains only alphabets or follows the "word-number" format like "kiwi-1"
    if "-" in name:
        parts = name.split("-")
        if len(parts) != 2 or not parts[0].isalpha() or not parts[1].isdigit():
            print("Invalid item name! It must contain only alphabets OR "
                  "start with alphabets and have numbers with a hyphen (e.g., kiwi or kiwi-1).")
            return
    # Check if the first character is a letter
    elif not name.isalpha():
        print("Invalid item name! It must contain only alphabets (A-Z, a-z).")
        return

       # Validate price
    try:
        price = float(input("Enter item price: "))
        if price <= 0:
            print("Invalid price! Price must be a positive number.")
            return
    except ValueError:
        print("Invalid input! Price must be a numerical value.")
        return

    # Validate quantity (must be an integer)
    try:
        quantity = int(input("Enter item quantity: "))
        if quantity <= 0:
            print("Invalid quantity! Quantity must be a positive integer.")
            return
    except ValueError:
        print("Invalid input! Quantity must be a whole number (integer).")
        return
    # Validate category (must be only alphabets)
    category = input("Enter item category: ").strip()
    if not category.isalpha():
        print("Invalid category! Category must contain only letters (e.g., Fruits, Dairy).")
        return

    for item in smart_cart_inventory:
        if item["name"].lower() == name.lower():
            print(f"Item '{name}' already exists in inventory!")
            return

    # Creating a dictionary to represent the item
    item = {"name": name, "price": price, "quantity": quantity, "category": category}
    smart_cart_inventory.append(item)
    print(f"Item '{name}' added successfully!")


# Function to update an existing item
def update_item():
    name = input("Enter the name of the item to update: ")
    for item in smart_cart_inventory:
        if item["name"].lower() == name.lower():
            print(f"Current Details: {item}")
            try:
                item["price"] = float(input("Enter new price: "))
                item["quantity"] = int(input("Enter new quantity: "))
            except ValueError:
                print("Error: Price must be a number and quantity must be an integer.")
                return
            item["category"] = input("Enter new category: ")
            print(f"Item '{name}' updated successfully!")
            return
    print(f"Item '{name}' not found!")


# Function to view the entire inventory
def view_inventory():
    if not smart_cart_inventory:
        print("Inventory is empty!")
    else:
        print("\nMyMart Inventory List:")
        for item in smart_cart_inventory:
            print(f"- {item['name']} | ${item['price']} | {item['quantity']} units | Category: {item['category']}")


# Function to remove an item
def remove_item():
    name = input("Enter the name of the item to remove: ")
    for item in smart_cart_inventory:
        if item["name"].lower() == name.lower():
            smart_cart_inventory.remove(item)
            print(f"Item '{name}' removed successfully!")
            return
    print(f"Item '{name}' not found!")


# Function to search items by category
def search_by_category():
    category = input("Enter category to search: ")
    found_items = [item for item in smart_cart_inventory if item["category"].lower() == category.lower()]

    if found_items:
        print(f"\nItems in Category '{category}':")
        for item in found_items:
            print(f"- {item['name']} | ${item['price']} | {item['quantity']} units")
    else:
        print(f"No items found in category '{category}'!")

def search_by_item():
    item_name = input("Enter item name to search: ").strip()

    # Search for matching items in the inventory
    found_items = [item for item in smart_cart_inventory if item["name"].lower() == item_name.lower()]

    if found_items:
        print(f"\nDetails for Item '{item_name}':")
        for item in found_items:
            print(f"- Category: {item['category']} | Price: ${item['price']} | Quantity: {item['quantity']} units")
    else:
        print(f"No items found with name '{item_name}'!")

# Main loop for user interaction
def main():
    while True:
        print("\nSmartCart Inventory Management System")
        print("-------------------------------------")
        print("1️. Add Item\n2️. Update Item\n3️. View Inventory\n4️. Remove Item\n5️. Search by Category\n6. Search by Item\n7. Exit")

        choice = input("Choose an option (1-7): ")
        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            search_by_item()
        elif choice == "7":
            print("Your inventory is set and ready! Keep growing, keep organizing! Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 7.")


# Run the program
if __name__ == "__main__":
    main()


