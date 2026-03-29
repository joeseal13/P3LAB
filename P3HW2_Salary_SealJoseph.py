# Joseph Seal
# 03/29/2026
# P3HW2_Salary_SealJoseph.py
# This program calculates an employee's regular pay, overtime pay,
# and gross pay based on hours worked and pay rate.

"""
Pseudocode / Algorithm:
1. Ask the user to enter the employee's name.
2. Ask the user to enter the number of hours worked this week.
3. Ask the user to enter the employee's pay rate.
4. If hours worked is greater than 40:
      overtime hours = hours worked - 40
      regular hours = 40
   Else:
      overtime hours = 0
      regular hours = hours worked
5. Calculate overtime pay using 1.5 times the regular pay rate.
6. Calculate regular pay using regular hours times pay rate.
7. Calculate gross pay by adding regular pay and overtime pay.
8. Display employee name, pay rate, hours worked, overtime hours,
   overtime pay, regular pay, and gross pay.
"""

# Ask for employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Determine overtime and regular hours
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

# Calculate pay
overtime_pay = overtime_hours * (pay_rate * 1.5)
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Display results
print("-------------------------------------")
print("Employee name:", employee_name)
print()
print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("----------------------------------------------------------------------------")
print(f"{hours_worked:<14.1f}{pay_rate:<11.2f}{overtime_hours:<11.1f}{overtime_pay:<15.2f}{regular_pay:<14.2f}{gross_pay:.2f}")
