"""
File: average_temperature.py
Description: Calculates the average, highest, and lowest temperatures entered by the user.
"""

print("Average Temperature Calculator")
print("-" * 30)

# Store temperatures in a list
temperatures = []

# Take input for 5 days
for day in range(1, 6):
    temperature = float(input(f"Enter temperature for Day {day}: "))
    temperatures.append(temperature)

# Perform calculations
average_temperature = sum(temperatures) / len(temperatures)
highest_temperature = max(temperatures)
lowest_temperature = min(temperatures)

# Display results
print("\nTemperature Report")
print("-" * 30)
print("Temperatures:", temperatures)
print(f"Average Temperature: {average_temperature:.2f}°C")
print(f"Highest Temperature: {highest_temperature:.2f}°C")
print(f"Lowest Temperature: {lowest_temperature:.2f}°C")