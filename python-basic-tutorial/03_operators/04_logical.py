# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Logical Operators
# Learning Objective: Combine Boolean conditions.
# Short Explanation: and, or, and not help make decisions with multiple rules.
# Expected Output:
# Can enter: True
# Needs permission: False
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Logical Operators?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

age = 16
has_ticket = True
can_enter = age >= 13 and has_ticket
needs_permission = not can_enter
print("Can enter:", can_enter)
print("Needs permission:", needs_permission)
