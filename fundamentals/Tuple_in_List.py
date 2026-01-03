employees = [("Alice", 50000), ("Bob", 60000), ("Charlie", 55000)]
Highest_Salary = int()
emp_count = len(employees)
i = 0

Highest_Salary = employees[1][1]

while( i < emp_count):
    emp = list(employees[i])
    if (emp[1] > Highest_Salary):
        Highest_Salary = emp[1]
    i = i+1
print(f"The highest salry of employee is {Highest_Salary}")