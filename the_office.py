employee = list(map(int, input().split()))
factor = int(input())

employee_happiness = [emp * factor for emp in employee]
average = sum(employee_happiness) / len(employee_happiness)
happiest_employee = [people for people in employee_happiness if people >= average]

if len(happiest_employee) >= len(employee_happiness) / 2:
    print(f"Score: {len(happiest_employee)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happiest_employee)}/{len(employee_happiness)}. Employees are not happy!")
