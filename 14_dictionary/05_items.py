# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Dictionary items()
# Learning Objective: Get keys and values together.
# Short Explanation: items() returns key-value pairs for looping.
# Expected Output:
# name Alex
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Dictionary items()?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

student = {"name": "Alex", "age": 16}
for key, value in student.items():
    print(key, value)
