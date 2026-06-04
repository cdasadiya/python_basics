# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: ZeroDivisionError
# Learning Objective: Handle division by zero.
# Short Explanation: Math does not allow dividing by zero.
# Expected Output:
# Use a non-zero divisor.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is ZeroDivisionError?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

divisor = 0
try:
    print(10 / divisor)
except ZeroDivisionError:
    print("Use a non-zero divisor.")
