# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]

# Calculate the sum
total = 0
for grade in grades:
    total += grade

# Calculate the average (using int() to drop decimals like in your example)
avg = int(total / len(grades))

# Determine the letter grade
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

# Print results
print(f"Exams: {exam_one}, {exam_two}, {exam_three}")
print(f"Average: {avg}")
print(f"Grade: {letter_grade}")

# Determine if passing or failing
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
