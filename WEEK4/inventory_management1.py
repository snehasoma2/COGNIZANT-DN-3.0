# inventory_management.py

# List of product names
product_names = []

# Function to add a product
def add_product(product_name):
    product_names.append(product_name)
    print(f"Added product: {product_name}")

# Function to remove a product
def remove_product(product_name):
    if product_name in product_names:
        product_names.remove(product_name)
        print(f"Removed product: {product_name}")
    else:
        print(f"Product {product_name} not found.")

# Function to update a product
def update_product(old_name, new_name):
    if old_name in product_names:
        index = product_names.index(old_name)
        product_names[index] = new_name
        print(f"Updated product: {old_name} to {new_name}")
    else:
        print(f"Product {old_name} not found.")

# Dictionary to store product details
products = {}

# Function to add or update product details
def add_or_update_product_details(name, quantity, price):
    products[name] = {'quantity': quantity, 'price': price}
    print(f"Product details updated for: {name}")

# Function to delete a product
def delete_product(name):
    if name in products:
        del products[name]
        print(f"Deleted product: {name}")
    else:
        print(f"Product {name} not found.")


# Example product catalog using tuples
product_catalog = [
    ('Laptop', 1000),
    ('Smartphone', 500),
    ('Tablet', 300)
]

# Function to display product catalog
def display_catalog():
    print("Product Catalog:")
    for item in product_catalog:
        print(f"Product: {item[0]}, Price: ${item[1]}")


# Set to store unique product categories
product_categories = set()

# Function to add a category
def add_category(category):
    product_categories.add(category)
    print(f"Added category: {category}")

# Function to remove a category
def remove_category(category):
    if category in product_categories:
        product_categories.remove(category)
        print(f"Removed category: {category}")
    else:
        print(f"Category {category} not found.")


# Function to generate a report of products sorted by price
def generate_price_report():
    sorted_products = sorted(products.items(), key=lambda x: x[1]['price'])
    print("Products sorted by price:")
    for name, details in sorted_products:
        print(f"Product: {name}, Price: ${details['price']}, Quantity: {details['quantity']}")

# Function to find products within a certain price range using sets
def find_products_in_price_range(min_price, max_price):
    filtered_products = {name for name, details in products.items() if min_price <= details['price'] <= max_price}
    print(f"Products in the price range ${min_price} - ${max_price}: {', '.join(filtered_products)}")


if __name__ == "__main__":
    # Managing product names with a list
    add_product("Laptop")
    add_product("Smartphone")
    update_product("Smartphone", "Smartphone Pro")
    remove_product("Laptop")

    # Managing product details with a dictionary
    add_or_update_product_details("Smartphone Pro", 10, 800)
    add_or_update_product_details("Tablet", 5, 300)
    delete_product("Tablet")

    # Displaying the product catalog
    display_catalog()

    # Managing product categories with a set
    add_category("Electronics")
    add_category("Computers")
    remove_category("Computers")

    # Generating a price report
    generate_price_report()

    # Finding products within a price range
    find_products_in_price_range(500, 1000)
