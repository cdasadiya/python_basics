# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Recursion
# Learning Objective: Call a function from itself safely.
# Short Explanation: Recursion solves problems by breaking them into smaller versions.
# Expected Output:
# Factorial: 120
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Recursion?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)
print("Factorial:", factorial(5))
