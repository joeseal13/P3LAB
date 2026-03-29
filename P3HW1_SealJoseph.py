# Joseph Seal
# 03/29/2026
# P3HW1
# This program collects six module grades, removes the lowest grade,
# calculates the modified average, and displays the letter grade.

# Create empty list for grades
grades = []

# Get grades from user
grade1 = float(input("Enter grade for Module 1: "))
grades.append(grade1)

grade2 = float(input("Enter grade for Module 2: "))
grades.append(grade2)

grade3 = float(input("Enter grade for Module 3: "))
grades.append(grade3)

grade4 = float(input("Enter grade for Module 4: "))
grades.append(grade4)

grade5 = float(input("Enter grade for Module 5: "))
grades.append(grade5)

grade6 = float(input("Enter grade for Module 6: "))
grades.append(grade6)

# Calculations
lowest = min(grades)
highest = max(grades)
grade_sum = sum(grades)
avg = grade_sum / len(grades)

# Determine letter grade
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n------------Results------------")
print(f"Lowest Grade:   {lowest}")
print(f"Highest Grade:  {highest}")
print(f"Sum of Grades:  {grade_sum}")
print(f"Average:        {avg:.2f}")
print(f"Letter Grade:   {letter_grade}")
