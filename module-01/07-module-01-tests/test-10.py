"""
Module 01 - Test 10

## Instructions

* Develop a script that requests the grades of 15 students, and based on that which of them approved/failed the subject 
* Show the result using print()

"""

# Define the passing grade threshold (e.g., 6)
passing_grade = 6.0

# Create empty lists to store student names and their grades
student_names = []
student_grades = []

# Input grades for 15 students
for student in range(15):
    student_name = input(f"Enter the name of student {student + 1}: ")
    student_grade = float(input(f"Enter the grade for {student_name}: "))

    student_names.append(student_name)
    student_grades.append(student_grade)

# Determine if each student passed or failed
results = []

for grade in range(15):
    if student_grades[grade] >= passing_grade:
        result = "Passed"
    else:
        result = "Failed"
    results.append(result)

# Print the results
print("\nResults:")
for result in range(15):
    print(
        f"{student_names[result]} - {student_grades[result]} - {results[result]}")
