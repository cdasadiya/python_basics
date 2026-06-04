# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Dictionary Loop
# Learning Objective: Loop through a dictionary.
# Short Explanation: Looping helps process each key and value.
# Expected Output:
# name -> Alex
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Dictionary Loop?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

student = {"name": "Alex", "age": 16}
for key, value in student.items():
    print(f"{key} -> {value}")
