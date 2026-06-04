# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: ValueError
# Learning Objective: Handle invalid values.
# Short Explanation: ValueError happens when a value has the wrong format.
# Expected Output:
# Please enter a valid number.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is ValueError?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

text = "abc"
try:
    number = int(text)
except ValueError:
    print("Please enter a valid number.")
