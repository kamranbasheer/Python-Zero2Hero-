#Task 4: Guessing Game
#Objective: Create a number guessing game where the user has to guess a randomly generated number within a certain range.

import random

min_value = 1
max_value = 100

random_number = random.randint(min_value, max_value)

print(f"Guess the number between {min_value} and {max_value}")

attempts = 0
correct_guess = False

while not correct_guess:
    try:

        user_guess = int(input("Your guess: "))
        attempts += 1

        if user_guess == random_number:
            correct_guess = True
            print("Congratulations! You guessed the number correctly.")
        elif user_guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")