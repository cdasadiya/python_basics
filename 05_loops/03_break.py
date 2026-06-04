# Author: Chaitanya Dasadiya
# LinkedIn: https://www.linkedin.com/in/chaitanya-dasadiya
# Topic Name: break Statement
# Learning Objective: Stop a loop early.
# Short Explanation: break exits a loop immediately.
# Expected Output:
# 1
# 2
# Found 3, stopping.
# Common Mistakes:
# - Do not memorize code only; understand what each line does.
# - Watch spelling, indentation, and matching brackets.
# Interview Questions:
# - What is break Statement?
# - Can you give one real-world example?
# Best Practices:
# - Use clear variable names.
# - Run the file after every small change.

for number in range(1, 6):
    if number == 3:
        print("Found 3, stopping.")
        break
    print(number)
