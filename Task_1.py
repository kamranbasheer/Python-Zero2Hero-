#Task 1: Temperature Converter
#Objective: Create a script to convert temperatures from Celsius to Fahrenheit.

temp = float(input("Please enter a temperature in Celsius: "))

# Correct the multiplication operator
temp_in_F = (temp * 9/5) + 32

# Convert temp_in_F to string for concatenation
print("Temperature in Fahrenheit is: " + str(temp_in_F))