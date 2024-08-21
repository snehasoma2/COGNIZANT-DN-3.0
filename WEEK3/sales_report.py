# sales_report.py

# Step 2: Define a list of sales amounts
sales = [200, 600, 150, 800, 300]

# Step 3: Define the function to generate the report
def generate_report(sales):
    total_sales = 0
    print("Sales Report for the Previous Month:")
    print("-" * 35)
    for sale in sales:
        if sale > 500:
            print(f"Sale amount: ${sale} - Highlighted (Over $500)")
        else:
            print(f"Sale amount: ${sale}")
        total_sales += sale
    print("-" * 35)
    return total_sales

# Step 4: Call the function to generate a report for the example sales list
total_sales = generate_report(sales)

# Step 5: Print the total sales for the month
print(f"Total sales for the month: ${total_sales}")
