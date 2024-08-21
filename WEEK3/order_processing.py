# order_processing.py

# Step 2: Define a variable for the order amount
order_amount = 150.00

# Step 3: Define the function to apply a discount
def apply_discount(order_amount):
    if order_amount > 100:
        discount = order_amount * 0.10
        final_price = order_amount - discount
    else:
        final_price = order_amount
    return final_price

# Step 4: Calculate the final price for an example order
final_price = apply_discount(order_amount)

# Step 5: Print the final price after applying the discount
print(f"The final price after applying the discount is: ${final_price:.2f}")
