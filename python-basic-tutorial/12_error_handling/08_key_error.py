# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: KeyError
# Learning Objective: Handle missing dictionary keys.
# Short Explanation: KeyError happens when a dictionary key is missing.
# Expected Output:
# Key was not found.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is KeyError?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

student = {"name": "Alex"}
try:
    print(student["age"])
except KeyError:
    print("Key was not found.")
