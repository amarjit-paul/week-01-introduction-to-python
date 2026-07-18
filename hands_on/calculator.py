"""
File: calculator.py
Description: A simple calculator that performs basic arithmetic operations.
"""

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Displaying results
print("\nCalculator Results")
print("------------------")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero.")