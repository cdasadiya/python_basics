# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: try except
# Learning Objective: Handle runtime errors gracefully.
# Short Explanation: try except lets a program continue instead of crashing.
# Expected Output:
# Cannot divide by zero.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is try except?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
