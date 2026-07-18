"""
File: if_else.py
Description: Demonstrates the use of if, elif, and else statements in Python.
"""

# Taking user input
marks = int(input("Enter your marks: "))

# Checking the grade
if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

# Displaying the result
print("\nResult")
print("------")
print("Marks:", marks)
print("Grade:", grade)