# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: IndexError
# Learning Objective: Handle invalid list indexes.
# Short Explanation: IndexError happens when an index is outside the list.
# Expected Output:
# That index does not exist.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is IndexError?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

items = ["pen", "book"]
try:
    print(items[5])
except IndexError:
    print("That index does not exist.")
