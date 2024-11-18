#Task 2: Simple Calculator
#Objective: Write a program that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

# Take input for the first number
Num1 = int(input("Please enter 1st Number: "))

# Correct input conversion for the second number
Num2 = int(input("Please enter 2nd Number: "))

# Perform arithmetic operations
addition = Num1 + Num2
subtraction = Num2 - Num1
multiplication = Num1 * Num2

# Use the correct function for output
print("Sum of both numbers is: " + str(addition) + ". Product of both numbers is: " + str(multiplication))