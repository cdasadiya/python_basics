# Author: YOUR_NAME
# LinkedIn: YOUR_LINKEDIN_PROFILE
# Topic Name: Variable Arguments
# Learning Objective: Accept many arguments.
# Short Explanation: *args collects many positional values in a tuple.
# Expected Output:
# Total: 15
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is Variable Arguments?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

def add_all(*numbers):
    return sum(numbers)
print("Total:", add_all(1, 2, 3, 4, 5))
