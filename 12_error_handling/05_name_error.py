# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: NameError
# Learning Objective: Handle missing variable names.
# Short Explanation: NameError happens when a name is used before it exists.
# Expected Output:
# The variable was not defined.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is NameError?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

try:
    print(unknown_name)
except NameError:
    print("The variable was not defined.")
