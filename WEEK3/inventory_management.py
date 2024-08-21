# inventory_management.py

# Step 2: Define a list of items with their quantities
inventory = [('item1', 10), ('item2', 0), ('item3', 5)]

# Step 3: Define the function to check the inventory
def check_inventory(inventory):
    for item, quantity in inventory:
        if quantity == 0:
            print(f"Alert: {item} is out of stock!")
        else:
            print(f"{item} is in stock with {quantity} units.")

# Step 4: Iterate over the list and use the function to check the inventory
check_inventory(inventory)

# Step 5: Print the results
# The function itself already prints the results as part of its process
