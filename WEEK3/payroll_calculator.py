# payroll_calculator.py

# Step 2: Define variables for hours worked and hourly rate
hours_worked = 40
hourly_rate = 15.00

# Step 3: Define the function to calculate total pay
def calculate_pay(hours, rate):
    total_pay = hours * rate
    return total_pay

# Step 4: Calculate the pay for an example employee
employee_pay = calculate_pay(hours_worked, hourly_rate)

# Step 5: Print the total pay
print(f"The total pay for the employee is: ${employee_pay:.2f}")
