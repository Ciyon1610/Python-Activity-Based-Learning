# Student Marks and Grade Calculator
# Beginner Python project using input, variables, arithmetic, and if/elif/else.

print("Student Marks and Grade Calculator")
print("Enter marks from 0 to 100.\n")

student_name = input("Student name: ")

subject_1 = float(input("Marks for Subject 1: "))
subject_2 = float(input("Marks for Subject 2: "))
subject_3 = float(input("Marks for Subject 3: "))
subject_4 = float(input("Marks for Subject 4: "))
subject_5 = float(input("Marks for Subject 5: "))

total_marks = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average_marks = total_marks / 5

if average_marks >= 90:
    grade = "A"
elif average_marks >= 80:
    grade = "B"
elif average_marks >= 70:
    grade = "C"
elif average_marks >= 60:
    grade = "D"
elif average_marks >= 50:
    grade = "E"
else:
    grade = "F"

print("\n--- Result ---")
print("Student:", student_name)
print("Total marks:", total_marks, "out of 500")
print("Average:", round(average_marks, 2))
print("Grade:", grade)
