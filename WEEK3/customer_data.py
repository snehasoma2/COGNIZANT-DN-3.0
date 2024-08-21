# customer_data.py

# Step 2: Define a dictionary to store customer names and their purchase amounts
customer_data = {'Alice': 120, 'Bob': 75, 'Charlie': 90}

# Step 3: Define the function to update the purchase amount for a customer
def update_purchase(customer_data, name, amount):
    if name in customer_data:
        customer_data[name] = amount
        print(f"Updated {name}'s purchase amount to {amount}.")
    else:
        print(f"Customer {name} not found in the data.")

# Step 4: Use the function to update Bob's purchase amount to 100
update_purchase(customer_data, 'Bob', 100)

# Step 5: Print the updated customer data
print("Updated customer data:", customer_data)
