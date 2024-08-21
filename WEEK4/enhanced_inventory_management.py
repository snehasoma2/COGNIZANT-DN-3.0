import threading
import time
import json

class Inventory:
    def __init__(self):
        self.stock = {}
        self.lock = threading.Lock()

    def add_item(self, item_name, quantity):
        with self.lock:
            if item_name in self.stock:
                self.stock[item_name] += quantity
            else:
                self.stock[item_name] = quantity
            print(f"Added {quantity} of {item_name} to inventory.")

    def remove_item(self, item_name, quantity):
        with self.lock:
            if item_name in self.stock and self.stock[item_name] >= quantity:
                self.stock[item_name] -= quantity
                print(f"Removed {quantity} of {item_name} from inventory.")
            else:
                print(f"Unable to remove {quantity} of {item_name}. Not enough stock or item does not exist.")

    def check_stock(self, item_name):
        with self.lock:
            return self.stock.get(item_name, 0)

    def save_to_file(self, filename):
        with self.lock:
            try:
                with open(filename, 'w') as file:
                    json.dump(self.stock, file)
                print(f"Inventory saved to {filename}.")
            except Exception as e:
                print(f"Error saving inventory to file: {e}")

    def load_from_file(self, filename):
        with self.lock:
            try:
                with open(filename, 'r') as file:
                    self.stock = json.load(file)
                print(f"Inventory loaded from {filename}.")
            except Exception as e:
                print(f"Error loading inventory from file: {e}")

        def restock_alerts(self, threshold=10, interval=5):
        def check_stock_levels():
            while True:
                with self.lock:
                    for item, quantity in self.stock.items():
                        if quantity < threshold:
                            print(f"Restock Alert: {item} is low in stock with only {quantity} left.")
                time.sleep(interval)
        
        threading.Thread(target=check_stock_levels, daemon=True).start()


if __name__ == "__main__":
    inventory = Inventory()

    # Add and remove some items
    inventory.add_item("Apples", 50)
    inventory.add_item("Oranges", 20)
    inventory.remove_item("Apples", 5)

    # Save the state to a file
    inventory.save_to_file("inventory.json")

    # Load the state from the file
    inventory.load_from_file("inventory.json")

    # Start the restocking alert thread
    inventory.restock_alerts()

    # Simulate some operations to see alerts
    time.sleep(10)
    inventory.remove_item("Oranges", 15)
    inventory.remove_item("Oranges", 4)


    inventory.load_from_file("inventory.json")
    print("Current Inventory:", inventory.stock)
