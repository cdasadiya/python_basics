# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: enumerate()
# Learning Objective: Loop with index and value together.
# Short Explanation: enumerate() is useful when you need item numbers.
# Expected Output:
# 1. Python
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is enumerate()?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

courses = ["Python", "Data", "AI"]
for index, course in enumerate(courses, start=1):
    print(f"{index}. {course}")
