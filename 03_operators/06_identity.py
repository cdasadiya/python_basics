# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: Identity Operators
# Learning Objective: Compare whether variables point to the same object.
# Short Explanation: is checks object identity, not just equal value.
# Expected Output:
# Same object: True
# Same value: True
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Identity Operators?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

first = [1, 2, 3]
second = first
third = [1, 2, 3]
print("Same object:", first is second)
print("Same value:", first == third)
