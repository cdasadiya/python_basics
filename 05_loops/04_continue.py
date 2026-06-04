# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: continue Statement
# Learning Objective: Skip one loop step.
# Short Explanation: continue skips the rest of the current loop cycle.
# Expected Output:
# 1
# 3
# 5
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is continue Statement?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

for number in range(1, 6):
    if number % 2 == 0:
        continue
    print(number)
