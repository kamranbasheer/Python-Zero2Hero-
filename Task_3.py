#Task 3: List Sorting
#Objective: Ask the user for a list of numbers and then sort and print the list in ascending order.

# Step 1: Prompt the user for input
numbers_input = input("Please enter a list of numbers separated by spaces: ")

# Step 2: Convert the input string to a list of integers
numbers_list = [int(num) for num in numbers_input.split()]

# Step 3: Sort the list
sorted_numbers = sorted(numbers_list)

# Step 4: Print the sorted list
print("The sorted list of numbers is:", sorted_numbers)