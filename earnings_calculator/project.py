# day-3 project

employee_name = input("Type the employee name: ").title().strip()
hourly_wage = int(input("type the hourly wage: "))
hours_worked = int(input("type the hours worked: "))

print(f"Employee {employee_name}, has earned ${hourly_wage * hours_worked} this week!")
