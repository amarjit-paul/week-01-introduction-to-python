"""
File: input_output.py
Description: Demonstrates user input and output in Python.
"""

# Taking input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Displaying the output
print("\nUser Information")
print("----------------")
print("Name:", name)
print("Age:", age)

# Using formatted strings
print(f"\nHello {name}! You are {age} years old.")