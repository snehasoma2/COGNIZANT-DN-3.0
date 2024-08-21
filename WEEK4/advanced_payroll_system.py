class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hours_worked * self.hourly_rate
        else:
            overtime_hours = self.hours_worked - 40
            regular_pay = 40 * self.hourly_rate
            overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
            return regular_pay + overtime_pay

class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus

    def calculate_pay(self):
        base_pay = super().calculate_pay()
        return base_pay + self.bonus

if __name__ == "__main__":
    # Employee instance
    employee = Employee("John Doe", 45, 20)  # 45 hours worked, $20 hourly rate
    print(f"{employee.name}'s total pay: ${employee.calculate_pay()}")

    # Manager instance
    manager = Manager("Jane Smith", 50, 30, 500)  # 50 hours worked, $30 hourly rate, $500 bonus
    print(f"{manager.name}'s total pay: ${manager.calculate_pay()}")

class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        if self.hours_worked <= 40:
            return self.hours_worked * self.hourly_rate
        else:
            overtime_hours = self.hours_worked - 40
            regular_pay = 40 * self.hourly_rate
            overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
            return regular_pay + overtime_pay

class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus

    def calculate_pay(self):
        base_pay = super().calculate_pay()
        return base_pay + self.bonus

if __name__ == "__main__":
    # Employee instance
    employee = Employee("John Doe", 45, 20)
    print(f"{employee.name}'s total pay: ${employee.calculate_pay()}")

    # Manager instance
    manager = Manager("Jane Smith", 50, 30, 500)
    print(f"{manager.name}'s total pay: ${manager.calculate_pay()}")
