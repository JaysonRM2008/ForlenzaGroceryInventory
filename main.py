from readline import remove_history_item

# Dictionary to store inventory
# 2 examples
inventory = { "apple": 100, "banana": 150}

def add_item(inventory, name, quantity):
    


def  display_inventory(inventory):
    print("Current Inventory:")  # Prints a header indicating the inventory display

    # Checks if the inventory dictionary is empty
    if len(inventory) == 0:
        print("Inventory is empty.")  # If empty, prints a message
    else:
        # If not empty, iterates through each item in the inventory
        for name in inventory:
            quantity = inventory[name]  # Retrieves the quantity for the current item
            print(f"{name}: Quantity: {quantity}")  # Prints the item name and its quantity

    """
    Add a new item to the inventory.
    
    Args:
    inventory (dict): The current inventory
    name (str): The name of the item
    price (str): The price of the item
    quantity (str): The quantity of the item
    """
    inventory[name] = quantity
    print(f"{name} added to the inventory.")

def update_quantity(inventory, item_name, new_quantity):
    """
    Update the quantity of an item in the inventory.
    
    Args:
    inventory (dict): The current inventory
    item_name (str): The name of the item to update
    new_quantity (str): The new quantity of the item
    """
    inventory[item_name] == new_quantity
    print(f"{item_name} quantity updated to {new_quantity}.")


while True:
    print("\n1. Add item\n2. Remove item\n3. Update quantity\n4. Display inventory\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter item name: ")
        quantity = int(input("Enter item quantity: "))
        add_item(inventory, name, quantity)

    elif choice == "2":
    # Delete an item from the inventory.
        del_inventory = input("Enter item name to remove: ")
    
    if del_inventory in inventory:
        confirm = input(f"Are you sure you want to delete '{del_inventory}'? (y/n): ")
        if confirm.lower() == 'y':
            del inventory[del_inventory]
            print(f"'{del_inventory}' removed from the inventory.")
        else:
            print("Deletion cancelled.")
    else:
        print(f"'{del_inventory}' not found in the inventory.")

    
    elif choice == "3":
        name = input("Enter item name to update: ")
        quantity = input("Enter new quantity: ")
        update_quantity(inventory, name, quantity)
    elif choice == "4":
        display_inventory(inventory)

    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")