# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: zip()
# Learning Objective: Loop through two collections together.
# Short Explanation: zip() pairs items, like names with marks.
# Expected Output:
# Alex scored 90
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is zip()?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

names = ["Alex", "Maya"]
marks = [90, 85]
for name, mark in zip(names, marks):
    print(f"{name} scored {mark}")
